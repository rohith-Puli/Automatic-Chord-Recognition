import os
from shutil import copyfile
import feature 
import visual 
import chunk_send
import evaluation

dataset4_path = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/dataset4/'



def make_single_folder_wav(dataset4_path, dest_path):
	#This function will take all the WAVE files in the dataset and put them in the dest_path
	if(os.path.exists(dest_path)==False):
		os.mkdir(dest_path)

	mic_name = os.listdir(dataset4_path)
	print mic_name
	for a in range(0, len(mic_name),1):
		path_1 = os.path.join(dataset4_path, mic_name[a])
		tempo = os.listdir(path_1)
		for b in range(0, len(tempo),1):
			path_2 = os.path.join(path_1,tempo[b])
			genre = os.listdir(path_2)
			for c in range(0, len(genre),1):
				path_3 = os.path.join(path_2, genre[c])
				path_a = os.path.join(path_3,'audio/')
				wav_file = os.listdir(path_a)
				for d in range(0, len(wav_file),1):
					final_name_aud = mic_name[a]+'_' + tempo[b] +'_' + wav_file[d]
					path_wav = os.path.join(path_a, wav_file[d])
					path_dest =  os.path.join(dest_path, final_name_aud)
					copyfile(path_wav,path_dest)
	return;

def make_single_folder_csv(dataset4_path, dest_path):
	#This function will take all the reference annotations i.e. the .csv files for chords and put them in the dest_path
	if(os.path.exists(dest_path)==False):
		os.mkdir(dest_path)

	mic_name = os.listdir(dataset4_path)
	print mic_name
	for a in range(0, len(mic_name),1):
		path_1 = os.path.join(dataset4_path, mic_name[a])
		tempo = os.listdir(path_1)
		for b in range(0, len(tempo),1):
			path_2 = os.path.join(path_1,tempo[b])
			genre = os.listdir(path_2)
			for c in range(0, len(genre),1):
				path_3 = os.path.join(path_2, genre[c])
				path_a = os.path.join(path_3,'annotation/chords/')
				csv_file = os.listdir(path_a)
				for d in range(0, len(csv_file),1):
					final_name_aud = mic_name[a]+'_' + tempo[b] +'_' + csv_file[d]
					path_wav = os.path.join(path_a, csv_file[d])
					path_dest =  os.path.join(dest_path, final_name_aud)
					copyfile(path_wav,path_dest)
	return;


def allWav_wav_to_frame_to_time(allWav_path,dest_path_time):
	if(os.path.exists(dest_path_time)==False):
		os.mkdir(dest_path_time)
	# This function template matches the audio file after detecting the onsets and writes two files as output-> Chord labels in time intervals in dest_path_time
	for wav_file in os.listdir(allWav_path):

		name = wav_file

		y, sr = feature.load_audio(name= name, location = allWav_path)
		cqt = feature.find_cqt(y=y)

		#1.First find onset peaks
		times,peaks,o_env= feature.onset_detect(y=y)

		#2.Find silence regions and their boundaries
		z,c_red = feature.silence_spectrogram(cqt)
		z_boundaries = feature.zero_boundaries(z)

		#3. Remove spurious peaks
		peaks = feature.find_common_zerospeaks(peaks = peaks, z =z)

		#4.send peaks,z_boundaries, audio to chunkSender which will create a frame-level file
		chord_labels = chunk_send.chunk_sender(peaks=peaks, z_boundaries=z_boundaries, aud=y,method = 'nnls', name=name.split('.')[0],hop_length= 512,binsPerOctave= 36,sr=44100)

		#5. Convert the frame based chord labels to time based labels
		est_file = feature.frame_file_converter(frame_array=chord_labels , sr=sr, hop_length= 512, dest_path = dest_path_time, name =name.split('.')[0])

		print '%s successfully processed'%(wav_file)
	return;

# allWav_path = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/allWav/'
# dest_path_time = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/allWav_time_nnls/'
# allWav_wav_to_frame_to_time(allWav_path,dest_path_time)


##========The following functions are for the dataset========########

def is_subseq(x, y):
	"""
	Helper function:
	Returns bool if string x is a subsequence of string y
	"""
	x = list(x)
	for letter in y:
		if x and x[0] == letter:
			x.pop(0)

	return not x

def convertChordLabelToHARTE(chordLabel):
	"""
	Helper function:
	Description: 
		This takes in a chordLabel as in the chord annotations in IDMT-SMT Guitar dataset and converts them into 
		standard chord label syntax according to HARTE
		[Harte, C. (2010). Towards automatic extraction of harmony information from music signals (Doctoral dissertation)]
	"""

	if chordLabel == 'NC':
		return 'N'

	shortHandList = ['maj', 'min', 'dim', 'aug', 'maj7', 'min7', '7', 'dim7', 'hdim7', 'minmaj7', 'maj6', 'min6', '9', 'maj9', 'min9', 'sus2', 'sus4']

	names = chordLabel.split('/')
	rootName = names[0][0]
	modifier = ""
	shortHand = ""
	#inversion  = "" if len(names) == 1 else names[1]
	#intervals = ""

	if len(names[0]) == 1:
		return rootName

	if names[0][1] in ['b','#']:
	    modifier = names[0][1]
	    extraName = names[0][2:]
	else:
	    extraName = names[0][1:]

	bestShortHandLength = 0
	for c in shortHandList:
	    if is_subseq(c, extraName):
	        if bestShortHandLength < len(c):
	            shortHand = c
	            bestShortHandLength = len(c)
	            
	# TODO: add extra intervals also to the HARTE label name, currently IDMT-SMT Guitar Dataset doesn't have them comma separated
	#intervals = extraName.split(shortHand)[1]

	# Collect all the parts of the HARTE label and return

	finalName =  rootName + modifier 
	if shortHand != "":
		finalName = finalName + ":" + shortHand

	# Removed Inversion for now TODO: Raises Invalid Scale Degree error in Mir Eval
	#if inversion != "":
	#	finalName = finalName + "/"+ inversion

	return finalName


def ref_annotation_single_file_converter(path_source, path_dest,fileName):
	#This function takes a reference annotation where chords are labelled on Beats and converts it into the 'time_begin time_end chord_label' format.
	timeList = []
	fr = open(os.path.join(path_source,fileName), 'r')

	if(os.path.exists(path_dest)==False):
		os.mkdir(path_dest)

	fw = open(path_dest + fileName.split('.')[0]+ '.txt', 'w')
	lines = fr.readlines()
	for x in range(0, len(lines)-3,1):
		flag =0 #Flag to ensure that a later if statement does not override an earlier statement
		if(len(lines[x])> 15): #3 if conditions based on the digits of the numbers. Two digits in time, two digits in measures etc
			if(lines[x][15]== ':'):
				if(flag!=1):
					chordMarker = 16 #Marking the chord name
					original_name = lines[x][chordMarker:]
					harte_name = convertChordLabelToHARTE(original_name)
					timeList = timeList + [ ( float(lines[x][0:11]),harte_name ) ]
					flag =1
		if(len(lines[x])> 16):
			if(lines[x][16]== ':'):
				if(flag!=1):
					chordMarker = 17
					original_name = lines[x][chordMarker:]
					harte_name = convertChordLabelToHARTE(original_name)
					timeList = timeList + [ ( float(lines[x][0:11]),harte_name ) ]
					flag =1
		if(len(lines[x])> 17):
			if(lines[x][17]== ':'):
				if(flag!=1):
					chordMarker = 18
					original_name = lines[x][chordMarker:]
					harte_name = convertChordLabelToHARTE(original_name)
					timeList = timeList + [ ( float(lines[x][0:11]),harte_name) ]
					flag =1
	for x in range(0, len(timeList)-1,1):
		fw.write("%f %f %s\n"%(timeList[x][0], timeList[x+1][0], timeList[x][1] ))
	
	fr.close()
	fw.close()
	return;

def ref_annotation_multiple_file_converter(path_source, path_dest):
	#This function takes multiple GT annotation files, converts them into 'time_begin time_end chord_label' format.
	#Uses the function ref_annotation_single_file_converter() defined above
	for csv_file in os.listdir(path_source):
		print csv_file
		ref_annotation_single_file_converter(path_source, path_dest,csv_file)
	return;

def evaluate_dataset(estimated_folder, reference_folder,results_file_path ):
	#This function takes the folder of estimated annotations in 'time_begin time_end chord_label' format as one input
	#This function takes the folder of  reference annotations in 'time_begin time_end chord_label' format as the other input
	#Uses mir_eval to evaluate and finally puts all the results for each file, line by line in a csv file 
	f = open(results_file_path, 'w')
	estimated_folder_files = os.listdir(estimated_folder)
	reference_folder_files = os.listdir(reference_folder)
	for x in range(0, len(estimated_folder_files),1):
		est_file_name = estimated_folder_files[x].split('_estimated')[0]
		ref_file_name = reference_folder_files[x].split('.')[0]

		fr = open(os.path.join(estimated_folder,estimated_folder_files[x])) 
		lines_estimated_file = fr.readlines()
		duration = lines_estimated_file[len(lines_estimated_file)-1].split(' ')[1]
		if (est_file_name == ref_file_name):
			root, majmin, mirex, thirds, est_labels, ref_labels, intervals, comparisons_root = evaluation.eval_csr(est_file= os.path.join(estimated_folder,estimated_folder_files[x]), ref_file =os.path.join(reference_folder,reference_folder_files[x]) )
			f.write('%s %f %f %f %f %f \n'%(est_file_name, root, majmin, mirex,thirds, float(duration) ))
	f.close()
	return;

estimated_folder = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/allWav_time_cqt/'
reference_folder = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/allCsv_converted/'
results_file_path = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/results_cqt.txt'
evaluate_dataset(estimated_folder, reference_folder,results_file_path )