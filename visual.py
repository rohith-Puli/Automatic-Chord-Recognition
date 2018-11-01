import matplotlib.pyplot as plt 
import numpy as np 
import librosa, librosa.display


def plot_audio(x):
	fig = plt.figure()
	plt.plot(x)
	plt.show()
	return;

def plot_onsets(sr,y, times,peaks, o_env_max, name='plot'):
	
	"""
	sr = sampling rate,
	y = the audio data
	times = the 'times' output of the function feature.onset_detect() --> (An array of time stamps of each frame)
	peaks = the 'peaks' output of the function feature.onset_detect() --> (An array of frame numbers where onset is detected)
	=> times[peaks] will essentially give timestamps of where peaks are detected
	 """	
	t = np.arange(0, len(y),1)  * float(1)/float(sr)
	plt.figure()
	plt.title(name)
	plt.plot(t,y)
	plt.vlines(times[peaks], 0, o_env_max, color='r', alpha=0.9,
           linestyle='--', label='Onsets')
	plt.show()
	return;

def plot_silence_boundaries(sr,y,times, z_boundaries, o_env_max):
	t = np.arange(0, len(y),1)  * float(1)/float(sr)
	plt.figure()
	plt.plot(t,y)
	plt.vlines(times[z_boundaries], 0, o_env_max, color='y', alpha=0.9,
           linestyle='--', label='Onsets')
	plt.show()
	return;

def plot_both_onsetzero(sr,y,times,peaks,z,z_boundaries, o_env_max):
	#The next 3 lines will remove onsets where a zero is also detected. This is most probably a spurious peak
	intersection = np.in1d(peaks, z) 
	i = np.where(intersection==True)
	peaks = np.delete(peaks, i, axis =0)

	t = np.arange(0, len(y),1)  * float(1)/float(sr)
	plt.figure()
	plt.plot(t,y)
	plt.vlines(times[peaks], 0, o_env_max, color='r', alpha=0.9,
           linestyle='--', label='Onsets')
	plt.vlines(times[z_boundaries], 0, o_env_max, color='y', alpha=0.9,
       linestyle='--', label='zeros')
	plt.show()
	return;

def plot_chord_comparision():
	return;

def plot_chord_root_comparision(sr,y, est_labels, ref_labels, intervals, comparisons_root):
	#parameters are obtained from evaluation.py
	#This function plots estimated vs compared chords
	delta = float(1)/float(sr)
	timey = np.arange(0, len(y),1)  * delta

	ynum = [0,1,2,3,4,5,6,7,8,9,10,11,12]
	ylabels1 = ['C','C#','D','D#', 'E', 'F', 'F#', 'G','G#','A','A#', 'B','N']
	ylabels2 = ['C','Db','D','Eb', 'E', 'F', 'Gb', 'G','Ab','A','Bb', 'B','N']
	indices_est = np.zeros(len(est_labels))
	indices_ref = np.zeros(len(ref_labels)) 

	for a in range(0, len(est_labels),1):
		chord_est = est_labels[a].split(':')[0]
		if(len(chord_est)==2):
			if(chord_est[1]== '#'):
				indices_est[a] = int(ylabels1.index(chord_est))
			elif(chord_est[1]== 'b'):
				indices_est[a] = int(ylabels2.index(chord_est))
		else:
			indices_est[a] = int(ylabels1.index(chord_est))
	for a in range(0, len(ref_labels),1):
		chord_ref =ref_labels[a].split(':')[0]
		if(len(chord_ref)==2):
			if(chord_ref[1]== '#'):
				indices_ref[a] = int(ylabels1.index(chord_ref))
			elif(chord_ref[1]== 'b'):
				indices_ref[a] = int(ylabels2.index(chord_ref))
		else:
			indices_ref[a] = int(ylabels1.index(chord_ref))


	length = intervals[len(intervals)-1,1]#last time value in seconds
	time = np.arange(0, length, delta)
	y_ref_index = np.copy(time)
	y_est_index = np.copy(time)
	#intervals_round = np.around(self.intervals,4)
	intervals_round = intervals
	for x in range(0, len(intervals_round),1):
		start_time = float(intervals_round[x,0])
		end_time = float(intervals_round[x,1])
		start_index = int(start_time/delta)
		end_index = int(end_time/delta)
		comp = int(comparisons_root[x])
		y_ref_index[start_index:end_index] = indices_ref[x]
		y_est_index[start_index:end_index] = indices_est[x]


	fig1 = plt.figure()
	ax0 = plt.subplot(2,1,1)
	plt.plot(timey,y)

	ax1 = plt.subplot(2,1,2, sharex= ax0)
	plt.ylim(0,13)
	plt.yticks(ynum,ylabels1)
	plt.plot(time,y_ref_index, color = 'green')
	plt.plot(time,y_est_index, color = 'red', )
	plt.grid()

	plt.show()