# import matplotlib.pyplot as plt
# import numpy as np

# import librosa
# import vamp

import feature 
import visual 
import chunk_send
import evaluation


location = '/mnt/c/Users/rohith/Desktop/FLstudio/reggae_ska/audio/wav/'
name = 'reggae_1_95BPM.wav'

#sr = 44100
#fmin = librosa.midi_to_hz(36)
# bins_per_octave = 36
hop_length = 512

y, sr = feature.load_audio(name= name, location = location)
cqt = feature.find_cqt(y=y)


#1.First find onset peaks
times,peaks, o_env= feature.onset_detect(y=y)

#2.Find silence regions and their boundaries
z,c_red = feature.silence_spectrogram(cqt)
z_boundaries = feature.zero_boundaries(z)

#3. Remove spurious peaks
peaks = feature.find_common_zerospeaks(peaks = peaks, z =z)

#4.send peaks,z_boundaries, audio to chunkSender which will create a frame-level file
new_name = chunk_send.chunk_sender(peaks=peaks, z_boundaries=z_boundaries, aud=y, location=location, name=name.split('.')[0],hop_length= 512,binsPerOctave= 36,sr=44100)

#5. Convert the frame based chord labels to time based labels
est_file = feature.frame_file_converter(path = location, fileName = new_name , sr= sr, hop_length= hop_length)

#6. Compare annotations 
ref_file = '/mnt/c/Users/rohith/Desktop/FLstudio/reggae_ska/annotation/chords/convertedAnnotation/Timed_reggae_1_95BPM.txt'
root, majmin, mirex, thirds, est_labels, ref_labels, intervals, comparisons_root = evaluation.eval_csr(est_file= est_file, ref_file =ref_file )

print "root = %f, majmin =%f, mirex=%f thirds=%f"%(root, majmin, mirex,thirds)

visual.plot_chord_root_comparision(sr=sr,y=y, est_labels= est_labels, ref_labels= ref_labels, intervals = intervals, comparisons_root= comparisons_root)