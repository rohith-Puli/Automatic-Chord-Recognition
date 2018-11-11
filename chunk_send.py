import numpy as np
import feature 

import template
import os
#os.remove("ChangedFile.csv")
#print("File Removed!")

def return_zero_between_onset(onsetfr_index_1, onsetfr_index_2, z_boundaries):
	"""
	Auxilliary function to find if are zero is detected between two onsets
	"""
	flag =False
	element = None
	for y in range(0, len(z_boundaries),1):
		if(z_boundaries[y]>onsetfr_index_1 and z_boundaries[y]< onsetfr_index_2):
			flag =True
			element = z_boundaries[y]
			break
	return flag, element

def chroma_method(chunk, method,sr,hop_length):
	if (method == 'cqt'):
		chroma = feature.chroma_finder().from_cqt(chunk)
	elif (method == 'nnls'):
		chroma =feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=4096)
	return chroma


#def  chunk_sender(peaks, z_boundaries, aud,sr, hop_length=512,binsPerOctave, location, name, fmin):
def chunk_sender(peaks, z_boundaries, aud, method, name,hop_length= 512,binsPerOctave= 36,sr=44100):

	new_name = name + str(binsPerOctave)+ '.txt'

	if (method=='nnls'):
		binsPerOctave = ''

	chord_labels = np.empty([1,6])
	""" this function will take in the onset peaks and the frame numbers of the z_boundaries and template matches between an onset and a corresponding z boundary
		if exists. Else template matching is done between two onset frames
		Calculate peaks,z_boundaries from functions in features.py
	"""

	""" If a .txt file already exists, delete it, so that it will not append it to the existing file
	"""

	# path = location +new_name
	# if(os.path.exists(path)):
	# 	os.remove(path)
	# 	print 'Earlier version of the frame .txt file detected and removed'
	# else:
	# 	print 'File is newly created'

	for x in range(0, len(peaks)-1,1):
		flag, element = return_zero_between_onset(peaks[x], peaks[x+1], z_boundaries)
		start_idx = peaks[x]
		if(flag):
			zero_idx = element
			end_idx = peaks[x+1]
			chunk = aud[start_idx*hop_length:zero_idx*hop_length]

			############Choose the method to find CHROMA#####################
			#chroma = feature.chroma_finder().from_cqt(chunk)
			chroma = chroma_method(chunk,method,sr, hop_length)
			#chroma = feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=2048)
			chroma = chroma.T

			chord_labels= template.chordFind(t = chroma,start_idx = start_idx,chord_labels=chord_labels) 

			chunk = aud[zero_idx*hop_length : end_idx*hop_length]
			chunk=np.zeros(np.shape(chunk))

			############CHROMA#####################
			#chroma = feature.chroma_finder().from_cqt(chunk)
			chroma = chroma_method(chunk,method,sr, hop_length)
			#chroma = feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=2048)
			chroma = chroma.T

			chord_labels= template.chordFind(t = chroma,start_idx = zero_idx,chord_labels=chord_labels) 

		else:
			end_idx = peaks[x+1]
			chunk = aud[start_idx*hop_length:end_idx*hop_length]

			############CHROMA#####################
			#chroma = feature.chroma_finder().from_cqt(chunk)
			chroma = chroma_method(chunk,method,sr, hop_length)
			#chroma = feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=2048)
			chroma = chroma.T
			chord_labels= template.chordFind(t = chroma,start_idx = start_idx,chord_labels=chord_labels) 

	#The code below is exclusively for the last peak
	length = len(feature.chroma_finder().from_cqt(y=aud).T)
	flag_last, element_last = return_zero_between_onset(peaks[len(peaks)-1], length-1, z_boundaries)
	start_idx = peaks[len(peaks)-1]
	if(flag_last):
		end_idx = element_last
		chunk = aud[start_idx*hop_length:end_idx*hop_length]

		############CHROMA#####################
		#chroma = feature.chroma_finder().from_cqt(chunk)
		#chroma = feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=2048)
		chroma = chroma_method(chunk,method,sr, hop_length)
		chroma= chroma.T
		chord_labels= template.chordFind(t = chroma,start_idx = start_idx,chord_labels=chord_labels) 
		chunk = aud[end_idx*hop_length:len(aud)]
		chunk=np.zeros(np.shape(chunk))

		############CHROMA#####################
		#chroma = feature.chroma_finder().from_cqt(chunk)
		#chroma = feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=2048)
		chroma = chroma_method(chunk,method,sr, hop_length)
		chroma= chroma.T
		chord_labels= template.chordFind(t = chroma,start_idx = end_idx,chord_labels=chord_labels) 
	else:
		end_idx = length
		chunk = aud[start_idx*hop_length:end_idx*hop_length]

		############CHROMA#####################
		#chroma = feature.chroma_finder().from_cqt(chunk)
		#chroma = feature.nnls().chroma(data= chunk, sample_rate = sr,hop_length=hop_length, frame_length=2048)
		chroma = chroma_method(chunk,method,sr, hop_length)
		chroma = chroma.T
		chord_labels= template.chordFind(t = chroma,start_idx = start_idx,chord_labels=chord_labels) 

	chord_labels = chord_labels[1:]	
	#return new_name 
	return chord_labels