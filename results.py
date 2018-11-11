
import matplotlib.pyplot as plt 

results_file_path = '/mnt/c/Users/rohith/Documents/BITS_Pilani/IITB/Guitar_Chord_Detection/IDMT-SMT-GUITAR_V2/results_cqt.txt'

class val_dur:
	def __init__(self, value, duration):
		self.value = value
		self.duration = duration

fr = open(results_file_path)
lines = fr.readlines()

rec_method_dict = {}
rec_method_dict['acoustic_mic'] = {'root':[],'majmin':[],'mirex':[],'thirds':[]}
rec_method_dict['acoustic_pickup'] = {'root':[],'majmin':[],'mirex':[],'thirds':[]}
rec_method_dict['Career_SG'] = {'root':[],'majmin':[],'mirex':[],'thirds':[]}
rec_method_dict['Ibanez_2820'] = {'root':[],'majmin':[],'mirex':[],'thirds':[]}


genre_dict = {}
genre_dict['classical'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['country_folk'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['jazz'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['latin'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['metal'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['pop'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['reggae_ska'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }
genre_dict['rock_blues'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }

def evaluate_weighted_csr(dict_values): #dict_values is a list of val_dur objects
	sum_csr =dict_values[0].value*dict_values[0].duration
	total_duration =dict_values[0].duration
	for x in range(1, len(dict_values),1):
		sum_csr = sum_csr + dict_values[x].value*dict_values[x].duration
		total_duration =total_duration +dict_values[x].duration
	return sum_csr/total_duration;

for x in range(0, len(lines),1):

	line = lines[x].split(' ')
	name_file_split = line[0].split('_')
	duration = float(line[5])
	root = val_dur(float(line[1]), duration)
	majmin = val_dur(float(line[2]),duration)
	mirex = val_dur(float(line[3]),duration)
	thirds = val_dur(float(line[4]),duration)

	rec_method = name_file_split[0] + '_' + name_file_split[1]
	tempo =name_file_split[2]
	genre = name_file_split[3]

	
	if(rec_method =='acoustic_mic'):
		rec_method_dict['acoustic_mic']['root'].append(root)
		rec_method_dict['acoustic_mic']['majmin'].append(majmin)
		rec_method_dict['acoustic_mic']['mirex'].append(mirex)
		rec_method_dict['acoustic_mic']['thirds'].append(thirds)
	elif(rec_method =='acoustic_pickup'):
		rec_method_dict['acoustic_pickup']['root'].append(root)
		rec_method_dict['acoustic_pickup']['majmin'].append(majmin)
		rec_method_dict['acoustic_pickup']['mirex'].append(mirex)
		rec_method_dict['acoustic_pickup']['thirds'].append(thirds)
	elif(rec_method =='Career_SG'):
		rec_method_dict['Career_SG']['root'].append(root)
		rec_method_dict['Career_SG']['majmin'].append(majmin)
		rec_method_dict['Career_SG']['mirex'].append(mirex)
		rec_method_dict['Career_SG']['thirds'].append(thirds)
	elif(rec_method =='Ibanez_2820'):
		rec_method_dict['Ibanez_2820']['root'].append(root)
		rec_method_dict['Ibanez_2820']['majmin'].append(majmin)
		rec_method_dict['Ibanez_2820']['mirex'].append(mirex)
		rec_method_dict['Ibanez_2820']['thirds'].append(thirds)

#genre_dict['classical'] = {'fast':{'root':[],'majmin':[],'mirex':[],'thirds':[]}, 'slow':{'root':[],'majmin':[],'mirex':[],'thirds':[]} }

	if(genre == 'classical'):
		if(tempo =='fast'):
			genre_dict['classical']['fast']['root'].append(root)
			genre_dict['classical']['fast']['majmin'].append(majmin)
			genre_dict['classical']['fast']['mirex'].append(mirex)
			genre_dict['classical']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['classical']['slow']['root'].append(root)
			genre_dict['classical']['slow']['majmin'].append(majmin)
			genre_dict['classical']['slow']['mirex'].append(mirex)
			genre_dict['classical']['slow']['thirds'].append(thirds)

	elif(genre == 'country'):
		if(tempo =='fast'):
			genre_dict['country_folk']['fast']['root'].append(root)
			genre_dict['country_folk']['fast']['majmin'].append(majmin)
			genre_dict['country_folk']['fast']['mirex'].append(mirex)
			genre_dict['country_folk']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['country_folk']['slow']['root'].append(root)
			genre_dict['country_folk']['slow']['majmin'].append(majmin)
			genre_dict['country_folk']['slow']['mirex'].append(mirex)
			genre_dict['country_folk']['slow']['thirds'].append(thirds)

	elif(genre == 'jazz'):
		if(tempo =='fast'):
			genre_dict['jazz']['fast']['root'].append(root)
			genre_dict['jazz']['fast']['majmin'].append(majmin)
			genre_dict['jazz']['fast']['mirex'].append(mirex)
			genre_dict['jazz']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['jazz']['slow']['root'].append(root)
			genre_dict['jazz']['slow']['majmin'].append(majmin)
			genre_dict['jazz']['slow']['mirex'].append(mirex)
			genre_dict['jazz']['slow']['thirds'].append(thirds)

	elif(genre == 'latin'):
		if(tempo =='fast'):
			genre_dict['latin']['fast']['root'].append(root)
			genre_dict['latin']['fast']['majmin'].append(majmin)
			genre_dict['latin']['fast']['mirex'].append(mirex)
			genre_dict['latin']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['latin']['slow']['root'].append(root)
			genre_dict['latin']['slow']['majmin'].append(majmin)
			genre_dict['latin']['slow']['mirex'].append(mirex)
			genre_dict['latin']['slow']['thirds'].append(thirds)

	elif(genre == 'metal'):
		if(tempo =='fast'):
			genre_dict['metal']['fast']['root'].append(root)
			genre_dict['metal']['fast']['majmin'].append(majmin)
			genre_dict['metal']['fast']['mirex'].append(mirex)
			genre_dict['metal']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['metal']['slow']['root'].append(root)
			genre_dict['metal']['slow']['majmin'].append(majmin)
			genre_dict['metal']['slow']['mirex'].append(mirex)
			genre_dict['metal']['slow']['thirds'].append(thirds)

	elif(genre == 'pop'):
		if(tempo =='fast'):
			genre_dict['pop']['fast']['root'].append(root)
			genre_dict['pop']['fast']['majmin'].append(majmin)
			genre_dict['pop']['fast']['mirex'].append(mirex)
			genre_dict['pop']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['pop']['slow']['root'].append(root)
			genre_dict['pop']['slow']['majmin'].append(majmin)
			genre_dict['pop']['slow']['mirex'].append(mirex)
			genre_dict['pop']['slow']['thirds'].append(thirds)

	elif(genre == 'reggae' or genre=='ska'):
		if(tempo =='fast'):
			genre_dict['reggae_ska']['fast']['root'].append(root)
			genre_dict['reggae_ska']['fast']['majmin'].append(majmin)
			genre_dict['reggae_ska']['fast']['mirex'].append(mirex)
			genre_dict['reggae_ska']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['reggae_ska']['slow']['root'].append(root)
			genre_dict['reggae_ska']['slow']['majmin'].append(majmin)
			genre_dict['reggae_ska']['slow']['mirex'].append(mirex)
			genre_dict['reggae_ska']['slow']['thirds'].append(thirds)

	elif(genre == 'rock'):
		if(tempo =='fast'):
			genre_dict['rock_blues']['fast']['root'].append(root)
			genre_dict['rock_blues']['fast']['majmin'].append(majmin)
			genre_dict['rock_blues']['fast']['mirex'].append(mirex)
			genre_dict['rock_blues']['fast']['thirds'].append(thirds)
		elif(tempo == 'slow'):
			genre_dict['rock_blues']['slow']['root'].append(root)
			genre_dict['rock_blues']['slow']['majmin'].append(majmin)
			genre_dict['rock_blues']['slow']['mirex'].append(mirex)
			genre_dict['rock_blues']['slow']['thirds'].append(thirds)

fr.close()


class four_results:
	def __init__(self, root=0, majmin=0, mirex=0, thirds=0):
		self.root = root
		self.majmin = majmin
		self.mirex = mirex
		self.thirds = thirds
		
#print evaluate_weighted_csr(genre_dict['pop']['slow']['root']+genre_dict['rock_blues']['fast']['root'])

#Evaluate for whole genre
#Evaluate for each mic_setup
#Evaluate for fast and slow in each genre

###############Plots Mic_types###############################3
csr_acoustic_mic = four_results()
csr_acoustic_mic.root =  evaluate_weighted_csr(rec_method_dict['acoustic_mic']['root'])
csr_acoustic_mic.mirex =  evaluate_weighted_csr(rec_method_dict['acoustic_mic']['mirex'])
csr_acoustic_mic.majmin =  evaluate_weighted_csr(rec_method_dict['acoustic_mic']['majmin'])
csr_acoustic_mic.thirds =  evaluate_weighted_csr(rec_method_dict['acoustic_mic']['thirds'])

csr_acoustic_pickup = four_results()
csr_acoustic_pickup.root =  evaluate_weighted_csr(rec_method_dict['acoustic_pickup']['root'])
csr_acoustic_pickup.mirex =  evaluate_weighted_csr(rec_method_dict['acoustic_pickup']['mirex'])
csr_acoustic_pickup.majmin =  evaluate_weighted_csr(rec_method_dict['acoustic_pickup']['majmin'])
csr_acoustic_pickup.thirds =  evaluate_weighted_csr(rec_method_dict['acoustic_pickup']['thirds'])

csr_Career_SG = four_results()
csr_Career_SG.root =  evaluate_weighted_csr(rec_method_dict['Career_SG']['root'])
csr_Career_SG.mirex =  evaluate_weighted_csr(rec_method_dict['Career_SG']['mirex'])
csr_Career_SG.majmin =  evaluate_weighted_csr(rec_method_dict['Career_SG']['majmin'])
csr_Career_SG.thirds =  evaluate_weighted_csr(rec_method_dict['Career_SG']['thirds'])

csr_Ibanez_2820 = four_results()
csr_Ibanez_2820.root =  evaluate_weighted_csr(rec_method_dict['Ibanez_2820']['root'])
csr_Ibanez_2820.mirex =  evaluate_weighted_csr(rec_method_dict['Ibanez_2820']['mirex'])
csr_Ibanez_2820.majmin =  evaluate_weighted_csr(rec_method_dict['Ibanez_2820']['majmin'])
csr_Ibanez_2820.thirds =  evaluate_weighted_csr(rec_method_dict['Ibanez_2820']['thirds'])

csr_mic_setup_roots = [csr_acoustic_mic.root,csr_acoustic_pickup.root,csr_Career_SG.root,csr_Ibanez_2820.root]

csr_mic_setup_mirex = [csr_acoustic_mic.mirex,csr_acoustic_pickup.mirex,csr_Career_SG.mirex,csr_Ibanez_2820.mirex]

csr_mic_setup_majmin = [csr_acoustic_mic.majmin,csr_acoustic_pickup.majmin,csr_Career_SG.majmin,csr_Ibanez_2820.majmin]

csr_mic_setup_thirds = [csr_acoustic_mic.thirds,csr_acoustic_pickup.thirds,csr_Career_SG.thirds,csr_Ibanez_2820.thirds]

# width = 0.5
# x_axis = [1,2,3,4]
# x_ticks = ['acoustic_mic','acoustic_pickup','Career_SG','Ibanez_2820']
# header = ['roots','mirex','majmin','thirds']
# p1= plt.bar(x_axis,csr_mic_setup_roots,width=width,color = 'r' )
# p2 =plt.bar(x_axis,csr_mic_setup_mirex,width=width,color = 'b' )
# p3 =plt.bar(x_axis,csr_mic_setup_majmin,width=width,color = 'g' )
# p4 =plt.bar(x_axis,csr_mic_setup_thirds,width=width,color = 'c' )

# plt.xticks(x_axis,x_ticks)
# plt.ylim((0,1))
# plt.legend((p1[0], p2[0], p3[0], p4[0]), (header[0], header[1], header[2], header[3]), fontsize=12, ncol=4, framealpha=0, fancybox=True)
# plt.show()
#########################Plots mic_types##################################



def csr_genre_tempo(genre, tempo):
	csr = four_results()
	csr.root = evaluate_weighted_csr(genre_dict[genre][tempo]["root"])
	csr.majmin = evaluate_weighted_csr(genre_dict[genre][tempo]["majmin"])
	csr.mirex = evaluate_weighted_csr(genre_dict[genre][tempo]["mirex"])
	csr.thirds = evaluate_weighted_csr(genre_dict[genre][tempo]["thirds"])
	return csr

csr_classical_fast = csr_genre_tempo("classical", "fast")
csr_classical_slow = csr_genre_tempo("classical", "slow")

csr_country_folk_fast = csr_genre_tempo("country_folk", "fast")
csr_country_folk_slow = csr_genre_tempo("country_folk", "slow")

csr_jazz_fast = csr_genre_tempo("jazz", "fast")
csr_jazz_slow = csr_genre_tempo("jazz", "slow")

csr_latin_fast = csr_genre_tempo("latin", "fast")
csr_latin_slow = csr_genre_tempo("latin", "slow")

csr_metal_fast = csr_genre_tempo("metal", "fast")
csr_metal_slow = csr_genre_tempo("metal", "slow")

csr_pop_fast = csr_genre_tempo("pop", "fast")
csr_pop_slow = csr_genre_tempo("pop", "slow")

csr_reggae_ska_fast = csr_genre_tempo("reggae_ska", "fast")
csr_reggae_ska_slow = csr_genre_tempo("reggae_ska", "slow")

csr_rock_blues_fast = csr_genre_tempo("rock_blues", "fast")
csr_rock_blues_slow = csr_genre_tempo("rock_blues", "slow")


x_axis_fast = [1,3,5,7,9,11,13,15]
x_axis_slow = [1.5,3.5,5.5,7.5,9.5,11.5,13.5,15.5]
#x_axis_fast = [1,2,3,4,5,6,7,8]
x_labels =["classical","country_folk","jazz","latin","metal","pop","reggae_ska","rock_blues"]

list_genres_fast=[csr_classical_fast,csr_country_folk_fast,csr_jazz_fast,csr_latin_fast,csr_metal_fast,csr_pop_fast,csr_reggae_ska_fast,csr_rock_blues_fast] 
list_genres_slow=[csr_classical_slow,csr_country_folk_slow,csr_jazz_slow,csr_latin_slow,csr_metal_slow,csr_pop_slow,csr_reggae_ska_slow,csr_rock_blues_slow]

def appender(list_genres):
	roots =[]
	print type(roots)
	majmin = []
	mirex =[]
	thirds=[]
	for x in range(0, len(list_genres),1):
		roots.append(list_genres[x].root)
		majmin.append(list_genres[x].majmin)
		mirex.append(list_genres[x].mirex)
		thirds.append(list_genres[x].thirds)

	return roots, mirex, majmin, thirds

roots_fast, mirex_fast, majmin_fast, thirds_fast = appender(list_genres_fast)
roots_slow, mirex_slow, majmin_slow, thirds_slow = appender(list_genres_slow)

width = 0.48
header1 = ['roots','mirex','majmin','thirds']
header2 =['roots','mirex','majmin','thirDSs']
p1= plt.bar(x_axis_fast,roots_fast,width=width,color = 'r',align='edge' )
p2 =plt.bar(x_axis_fast,mirex_fast,width=width,color = 'b',align='edge' )
p3 =plt.bar(x_axis_fast,majmin_fast,width=width,color = 'g',align='edge' )
p4 =plt.bar(x_axis_fast,thirds_fast,width=width,color = 'c',align='edge' )

width = 0.5
#header = ['roots','mirex','majmin','thirds']
p_1= plt.bar(x_axis_slow,roots_slow,width=width,color = '#c1070d',align='edge' )
p_2 =plt.bar(x_axis_slow,mirex_slow,width=width,color = '#0a2168',align='edge' )
p_3 =plt.bar(x_axis_slow,majmin_slow,width=width,color = '#125907',align='edge' )
p_4 =plt.bar(x_axis_slow,thirds_slow,width=width,color = '#11787f',align='edge' )

plt.xticks(x_axis_fast,x_labels)
plt.ylim((0,1))
plt.grid()
plt.legend((p1[0], p2[0], p3[0], p4[0]), (header1[0], header1[1], header1[2], header1[3]), fontsize=12, ncol=4, framealpha=0, fancybox=True)

plt.show()


