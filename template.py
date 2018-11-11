import numpy as np
from decimal import *


chordTriad = [[0 ,'N' ,[0,0,0,0,0,0,0,0,0,0,0,0], 'N'],
			  [1 ,'C'  ,[1,0,0,0,1,0,0,1,0,0,0,0], 'C'],
			  [2 ,'C#' ,[0,1,0,0,0,1,0,0,1,0,0,0],'Db'],
			  [3 ,'D'  ,[0,0,1,0,0,0,1,0,0,1,0,0], 'D'],
			  [4 ,'D#' ,[0,0,0,1,0,0,0,1,0,0,1,0],'Eb'],
			  [5 ,'E'  ,[0,0,0,0,1,0,0,0,1,0,0,1], 'E'],
			  [6 ,'F'  ,[1,0,0,0,0,1,0,0,0,1,0,0], 'F'],
			  [7 ,'F#' ,[0,1,0,0,0,0,1,0,0,0,1,0],'Gb'],
			  [8 ,'G'  ,[0,0,1,0,0,0,0,1,0,0,0,1], 'G'],
			  [9 ,'G#' ,[1,0,0,1,0,0,0,0,1,0,0,0],'Ab'],
			  [10,'A'  ,[0,1,0,0,1,0,0,0,0,1,0,0], 'A'],
			  [11,'A#' ,[0,0,1,0,0,1,0,0,0,0,1,0],'Bb'],
			  [12,'B'  ,[0,0,0,1,0,0,1,0,0,0,0,1], 'B'],

			  [13 ,'C:min' ,[1,0,0,1,0,0,0,1,0,0,0,0], 'C:min'],
			  [14 ,'C#:min',[0,1,0,0,1,0,0,0,1,0,0,0], 'Db:min'],
			  [15 ,'D:min' ,[0,0,1,0,0,1,0,0,0,1,0,0], 'D:min'],
			  [16 ,'D#:min',[0,0,0,1,0,0,1,0,0,0,1,0], 'Eb:min'],
			  [17 ,'E:min' ,[0,0,0,0,1,0,0,1,0,0,0,1], 'E:min'],
			  [18 ,'F:min' ,[1,0,0,0,0,1,0,0,1,0,0,0], 'F:min'],
			  [19 ,'F#:min',[0,1,0,0,0,0,1,0,0,1,0,0], 'Gb:min'],
			  [20 ,'G:min' ,[0,0,1,0,0,0,0,1,0,0,1,0], 'G:min'],
			  [21 ,'G#:min',[0,0,0,1,0,0,0,0,1,0,0,1], 'Ab:min'],
			  [22,'A:min' ,[1,0,0,0,1,0,0,0,0,1,0,0], 'A:min'],
			  [23,'A#:min',[0,1,0,0,0,1,0,0,0,0,1,0], 'Bb:min'],
			  [24,'B:min' ,[0,0,1,0,0,0,1,0,0,0,0,1], 'B:min']   

			  ]


chordSeventh = [     

			  [25 ,'C:maj7'  ,[1,0,0,0,1,0,0,1,0,0,0,1], 'C:maj7'],
			  [26 ,'C#:maj7' ,[1,1,0,0,0,1,0,0,1,0,0,0],'Db:maj7'],
			  [27 ,'D:maj7'  ,[0,1,1,0,0,0,1,0,0,1,0,0], 'D:maj7'],
			  [28 ,'D#:maj7' ,[0,0,1,1,0,0,0,1,0,0,1,0],'Eb:maj7'],
			  [29 ,'E:maj7'  ,[0,0,0,1,1,0,0,0,1,0,0,1], 'E:maj7'],
			  [30 ,'F:maj7'  ,[1,0,0,0,1,1,0,0,0,1,0,0], 'F:maj7'],
			  [31 ,'F#:maj7' ,[0,1,0,0,0,1,1,0,0,0,1,0],'Gb:maj7'],
			  [32 ,'G:maj7'  ,[0,0,1,0,0,0,1,1,0,0,0,1], 'G:maj7'],
			  [33 ,'G#:maj7' ,[1,0,0,1,0,0,0,1,1,0,0,0],'Ab:maj7'],
			  [34 ,'A:maj7'  ,[0,1,0,0,1,0,0,0,1,1,0,0], 'A:maj7'],
			  [35 ,'A#:maj7' ,[0,0,1,0,0,1,0,0,0,1,1,0],'Bb:maj7'],
			  [36 ,'B:maj7'  ,[0,0,0,1,0,0,1,0,0,0,1,1], 'B:maj7'],

			  [37 ,'C:min7' ,[1,0,0,1,0,0,0,1,0,0,1,0], 'C:min7'],
			  [38 ,'C#:min7',[0,1,0,0,1,0,0,0,1,0,0,1], 'Db:min7'],
			  [39 ,'D:min7' ,[1,0,1,0,0,1,0,0,0,1,0,0], 'D:min7'],
			  [40 ,'D#:min7',[0,1,0,1,0,0,1,0,0,0,1,0], 'Eb:min7'],
			  [41 ,'E:min7' ,[0,0,1,0,1,0,0,1,0,0,0,1], 'E:min7'],
			  [42 ,'F:min7' ,[1,0,0,1,0,1,0,0,1,0,0,0], 'F:min7'],
			  [43 ,'F#:min7',[0,1,0,0,1,0,1,0,0,1,0,0], 'Gb:min7'],
			  [44 ,'G:min7' ,[0,0,1,0,0,1,0,1,0,0,1,0], 'G:min7'],
			  [45 ,'G#:min7',[0,0,0,1,0,0,1,0,1,0,0,1], 'Ab:min7'],
			  [46 ,'A:min7' ,[1,0,0,0,1,0,0,1,0,1,0,0], 'A:min7'],
			  [47 ,'A#:min7',[0,1,0,0,0,1,0,0,1,0,1,0], 'Bb:min7'],
			  [48 ,'B:min7' ,[0,0,1,0,0,0,1,0,0,1,0,1], 'B:min7']

			  ]

def correlate(z):
	z = z/z.max()
	corrSumTriad =0
	maxTriad =0
	indexTriad =0

	corrSumSeventh =0
	maxSeventh=0
	indexSeventh =0

	isTriad =0
	for y in range(0,len(chordTriad)-1,1):
		corrSumTriad =  float(np.correlate( z,chordTriad[y][2]))/3
		if (corrSumTriad>maxTriad):
			maxTriad = corrSumTriad
			indexTriad = y	
	for y in range(0,len(chordSeventh)-1,1):
		corrSumSeventh =  float( np.correlate( z,chordSeventh[y][2]) )/4
		if (corrSumSeventh>maxSeventh):
			maxSeventh = corrSumSeventh
			indexSeventh= y
	maxim = max(maxTriad, maxSeventh)

	if(maxim == maxSeventh and maxSeventh!=0):
		index =  indexSeventh
	else:
		index = indexTriad
		isTriad =1
	return index, isTriad, maxTriad, maxSeventh, z


# def chordFind(t, strING, binsPerOctave= '',location, start_idx):
# 	path = location + strING + binsPerOctave+ '.txt'
# 	f = open(path, 'a')
# 	# path_vector =  location + strING + binsPerOctave+ 'Vector'+ '.txt'
# 	# f_vector = open(path_vector, 'a')
# 	for x in range(0,len(t),1):
# 		index, isTriad, maxTriad, maxSeventh, z = correlate(t[x])
# 		#f_vector.write("%d %f %f %f %f %f %f %f %f %f %f %f %f\n"%(x+start_idx,z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8],z[9],z[10],z[11]))
		
# 		getcontext().prec =9
# 		if isTriad==1:
# 			f.write("%d %d %s %s %f %f \n"%(x+start_idx,chordTriad[index][0],chordTriad[index][1],chordTriad[index][3], maxTriad, maxSeventh))
# 		else:
# 			f.write("%d %d %s %s %f %f \n"%(x+start_idx,chordSeventh[index][0],chordSeventh[index][1],chordSeventh[index][3], maxTriad, maxSeventh ))
# 	f.close()
# 	return ;

def chordFind(t, start_idx, chord_labels):
	# path = location + strING + binsPerOctave+ '.txt'
	# f = open(path, 'a')
	# path_vector =  location + strING + binsPerOctave+ 'Vector'+ '.txt'
	# f_vector = open(path_vector, 'a')
	for x in range(0,len(t),1):
		index, isTriad, maxTriad, maxSeventh, z = correlate(t[x])
		#f_vector.write("%d %f %f %f %f %f %f %f %f %f %f %f %f\n"%(x+start_idx,z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8],z[9],z[10],z[11]))
		
		getcontext().prec =9
		if isTriad==1:
			chord_labels = np.vstack((chord_labels, [x+start_idx,chordTriad[index][0],chordTriad[index][1],chordTriad[index][3], maxTriad, maxSeventh]))
			#f.write("%d %d %s %s %f %f \n"%(x+start_idx,chordTriad[index][0],chordTriad[index][1],chordTriad[index][3], maxTriad, maxSeventh))
		else:
			chord_labels = np.vstack((chord_labels, [x+start_idx,chordSeventh[index][0],chordSeventh[index][1],chordSeventh[index][3], maxTriad, maxSeventh ]))
			#f.write("%d %d %s %s %f %f \n"%(x+start_idx,chordSeventh[index][0],chordSeventh[index][1],chordSeventh[index][3], maxTriad, maxSeventh ))
	#f.close()
	return chord_labels;