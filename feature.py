import librosa, librosa.display
import vamp

import matplotlib.pyplot as plt 
import numpy as np 

#name is the name with extension
def load_audio(name, location, sr=44100):
	y, sr = librosa.load(location +name, sr = sr)
	return y, sr;

def find_cqt(y= None, sr=44100, hop_length=512, fmin= librosa.midi_to_hz(36), n_bins=84,bins_per_octave=36, tuning=0.0, filter_scale=1, norm=1, sparsity=0.01, window='hann',scale=True, pad_mode='reflect'):
	cqt = librosa.core.cqt(y=y, sr=sr, hop_length=hop_length, fmin=fmin,n_bins = n_bins, bins_per_octave=bins_per_octave, tuning=tuning, filter_scale=filter_scale, norm=norm, sparsity=sparsity, window=window, scale=scale, pad_mode=pad_mode)
	return cqt; 


def find_stft(y= None, n_fft=2048, hop_length=512, win_length=None, window='hann', center=True, dtype=np.complex64, pad_mode='reflect'):
	stft = librosa.core.stft(y=y, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window, center=center, dtype=dtype, pad_mode=pad_mode)
	return stft;

class chroma_finder:	
	def from_cqt(self,y=None, sr=44100, C=None, hop_length=512, fmin=librosa.midi_to_hz(36), norm=np.inf, threshold=0.0, tuning=None, n_chroma=12, n_octaves=7, window=None, bins_per_octave=36, cqt_mode='full'):
		chromagram = librosa.feature.chroma_cqt(y=y, sr=sr, C=C, hop_length=hop_length, fmin=fmin, norm=norm, threshold=threshold, tuning=tuning, n_chroma=n_chroma, n_octaves=n_octaves, window=window, bins_per_octave=bins_per_octave, cqt_mode=cqt_mode)
		return chromagram;
	
	def from_stft(self,y=None, sr=44100, S=None, norm=np.inf, n_fft=2048, hop_length=512, tuning=None, **kwargs):
		chromagram = librosa.feature.chroma_stft(y=y, sr=sr, S=S, norm=norm, n_fft=n_fft, hop_length=hop_length, tuning=tuning, **kwargs)
		return chromagram;
 

class nnls:
	def __init__(self, parameters = {'useNNLS': 1, 'rollon': 5.0 ,'tuningmode': 0.0,  'whitening' : 1.0, 'chromanormalize' : 0.0, 's': 0.69999}):
		self.parameters = parameters

	def aligner(self,chromadata):
		finalChromagram = np.zeros(np.shape(chromadata))
		for x in range(0, len(chromadata)):
			finalChromagram[x][0:9] = chromadata[x][3:12]
			finalChromagram[x][9:12] = chromadata[x][0:3]
		finalChromagram = finalChromagram.T
		return finalChromagram

	def bass_chroma(self, data, sample_rate,hop_length, frame_length):
		chroma = vamp.collect(data= data,sample_rate= sample_rate, plugin_key ="nnls-chroma:nnls-chroma", parameters =self.parameters, output = 'basschroma',step_size = hop_length, block_size=frame_length)
		stepsize, chromadata = chroma["matrix"]
		return self.aligner(chromadata);

	def chroma(self,data, sample_rate,hop_length, frame_length):
		chroma = vamp.collect(data= data,sample_rate= sample_rate, plugin_key ="nnls-chroma:nnls-chroma", parameters =self.parameters, output = 'chroma',step_size = hop_length, block_size=frame_length)
		stepsize, chromadata = chroma["matrix"]
		return self.aligner(chromadata);

	def both_chroma(self, data, sample_rate,hop_length, frame_length):
		chroma = vamp.collect(data= data,sample_rate= sample_rate, plugin_key ="nnls-chroma:nnls-chroma", parameters =self.parameters, output = 'bothchroma',step_size = hop_length, block_size=frame_length)
		stepsize, chromadata = chroma["matrix"]
		return self.aligner(chromadata);


def silence_spectrogram(C):
	#The input C is the Spectrogram which needs to be silenced
	C = np.abs(C)
	c_red = np.copy(C)

	col = np.sum(C**2, axis = 0)
	ref = np.max(col)
	colM = np.copy(col)
	colM[10*np.log10(colM/ref)<= -30] = 0
	nz = colM[np.nonzero(colM)]
	z = np.where(colM == 0)[0]
	c_red[:,z] = 0
	return z, c_red; #z is the frame number where the spectrogram was made 0.

def onset_detect(y=None,sr=44100,S= None, max_size=3, lag=1,pre_max=5, post_max=5,pre_avg = 5, post_avg=5, delta= 0.5, wait = 5, hop_length= 512, n_fft= None  ):
	o_env= librosa.onset.onset_strength(y=y, sr=sr,S= S, max_size = max_size, lag =lag)#o_env1 gives the onset strength for all the frames.
	times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr, hop_length = hop_length, n_fft= n_fft) #array of time values of the frames
	peaks = librosa.util.peak_pick(o_env,pre_max, post_max, pre_avg, post_avg, delta, wait)#peaks has the indexes of the frames where peak is detected
							  #(onset_env, pre_max, post_max, pre_avg, post_avg, delta, wait)
	#onset_frames = librosa.onset.onset_detect(onset_envelope=o_env1, sr=sr)--> This function automatically picks peaks etc. Not used in this code.
	#onset_frames are the frame numbers in the spectrogram where onsets were detected
	return times, peaks, o_env

def zero_boundaries(z):
	"""This function will take the input as z(frame numbers of spectrogram where zero), 
	the indexes where the Cqt has been made zero and then, 
	finds out the boundaries of the intervals"""
	arr = np.array([])
	curr =0
	index = 1
	count =0
	#arr = np.append(arr,z[curr])
	while(curr+index< len(z)):
		#print curr
		if(z[curr+index]==z[curr]+1):
			curr = curr+index
			count = count +1
		else:
			#arr = np.append(arr, z[curr])#This will mark the end of the current zero interval 
			arr = np.append(arr, z[curr+index])#This will mark only the beginning of the next zero interval
			curr = curr + index
			count =0
	return arr.astype(int);


def find_common_zerospeaks(peaks,z):
	"""This function removes peak values where a zero was also detected. It must have been a spurious peak"""
	intersection = np.in1d(peaks, z) 
	i = np.where(intersection==True)
	peaks = np.delete(peaks, i, axis =0)
	return peaks

def frame_file_converter(path, fileName, sr, hop_length):
	converted_name = path + fileName.split('.')[0]+ 'converted.txt'
	hop_duration = float(hop_length)/float(sr)
	fr = open(path +fileName)

	fw = open(path + fileName.split('.')[0]+ 'converted.txt', 'w')

	line0 = fr.readline()

	lines = fr.readlines()

	line0split = line0.split()
	line0chordIndex = line0split[1]

	chordIndex = int(line0chordIndex)
	chordName1 = line0split[2]
	chordName2 = line0split[3]
	startFrameIndex = int(line0split[0])
	endFrameIndex = []
	count =0
	for x in range(0,len(lines),1):
		split = lines[x].split()
		currentChordIndex = int(split[1])
		currentFrameIndex = int(split[0])

		if(currentChordIndex== chordIndex):
			#print("Count = %d"%(count))
			count +=1
		else:
			count =0 
			endFrameIndex = currentFrameIndex
			fw.write("%f %f %s\n"%(startFrameIndex*hop_duration, endFrameIndex*hop_duration, chordName1))
			chordIndex = currentChordIndex
			startFrameIndex = currentFrameIndex
			chordName1 = split[2]
			chordName2 = split[3]
			#print("%d %d %d %s %s"%(chordIndex,startFrameIndex, endFrameIndex, chordName1, chordName2))
	fr.close()
	fw.close()
	print("File %s successfully converted"%(fileName))
	return path + fileName.split('.')[0]+ 'converted.txt';


		
