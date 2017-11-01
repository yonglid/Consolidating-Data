import csv
import pandas as pd
from itertools import chain 
from datetime import datetime
from copy import deepcopy
import os
from merge import merge

# x/column1.row2+column1.row1 
# x += 1
# check if manual input or automatic
directory = raw_input("Please enter directory path with files you want to modify: ")
# string_input = raw_input("Please enter files (separate with spaces): ")
# input_list = string_input.split()
# 

input_list = []
original_length = len(os.listdir(directory))
if os.path.exists(directory): 
	for file in os.listdir(directory): 
		if ('_new' not in file) and file.endswith(".csv"):
			# print file
			input_list.append(file)
			# print
	
# number = 0
else: 
	directory = raw_input("Please enter a valid directory:")
# copyof_input_list = deepcopy(input_list)
new_input = []

def main():
	
	# if 'ACC.csv' in input_list: 
	# 	copyof_input_list.remove('ACC.csv')
	# if 'IBI.csv' in input_list: 
	# 	copyof_input_list.remove('IBI.csv')
	# if 'tags.csv' in input_list: 
	# 	copyof_input_list.remove('tags.csv')

	for file in input_list: 
		# print "File in input_list" , file
		if file == 'ACC.csv':
			ACC_fun(file) 
			name_of_file = file[:-4] + "_new.csv"
			new_input.append(name_of_file)
		elif file == 'IBI.csv': 
			name_of_file = file[:-4] + "_new.csv"
			IBI_fun(file)
			new_input.append(name_of_file)
		elif file == 'tags.csv':
			name_of_file = file[:-4] + "_new.csv"
			tagEvents(file)
			new_input.append(name_of_file)

		else: 
			# print copyof_input_list
			# print 'here'
			dataFrames(file)
			# print "copy of input list: " , copyof_input_list
			name_of_file = file[:-4] + "_new.csv"
			# don't put the following line within the dataframe function idiot
			# was extra looping
			new_input.append(name_of_file)
		# print "New input list: " , new_input
		# print "First input list: " , input_list
	# print "merging"
	merge(new_input, directory)
	# print 'merge done'

def ACC_fun(filename): 
	file = os.path.join(directory, filename)  
	df = pd.read_csv(file, header=None)
	# df.loc[row, column]
	initialx = df.loc[0,0]
	initialy = df.loc[0,1]
	initialz = df.loc[0,2]

	# df[column][row]
	numx = df[0][2:]
	numy = df[1][2:]
	numz = df[2][2:]
	hertzx = df[0][1]
	hertzy = df[1][1]
	hertzz = df[2][1]

	# print another
	file_n = filename[:-4]
	final_file_n = file_n + ' real time'
	new_data = {
		'unix time' :[], 
		final_file_n : [], 
		'ACC_x': [], 
		'ACC_y':[], 
		'ACC_z':[]
	}
	sampleNumber = 0
	for item in numx: 
		if (hertzx) or (initialx):
			pass
		# else: 
		new_data['ACC_x'].append(item)
		newcolumn = float(sampleNumber)/hertzx + initialx 
		sampleNumber = sampleNumber + 1
		new_data['unix time'].append(newcolumn)
		realtime = datetime.fromtimestamp(newcolumn).strftime('%Y-%m-%d %H:%M:%S')
		new_data[final_file_n].append(realtime)
	for item in numy: 
		if (hertzy) or (initialy):
			pass
		# else: 
		new_data['ACC_y'].append(item)
	for item in numz: 
		if (hertzz) or (initialz):
			pass
		# else: 
		new_data['ACC_z'].append(item)

	unix_df = pd.DataFrame(new_data)

	name_of_file = file[:-4] + "_new.csv"
	unix_df.to_csv(os.path.join(directory, name_of_file), header=True, index=False, encoding='utf-8', mode='a')
def IBI_fun(filename): 
		# with open("TEMP.csv", "w") as csvoutput: 
			# writer = csv.writer(csvoutput, lineterminator='\n')
	# header is necessary for easier indexing like 0,0 
	file = os.path.join(directory, filename)  
	df = pd.read_csv(file, header=None)
	# df[column][row]
	ibi = df[1][1:]
	initial = df[0][0]
	times_from_initial = df[0][1:]
	file_n = filename[:-4]
	final_file_n = file_n + ' real time'
	new_data = {
		'unix time': [], 
		final_file_n: [], 
		file_n: []
	}
	# new_data[file_n].append(initial)
	# sampleNumber = 0
	for item in ibi: 
		new_data[file_n].append(item)
	
	
	for time in times_from_initial: 
		newunix = initial + time
	
		new_data['unix time'].append(newunix)
		realtime = datetime.fromtimestamp(newunix).strftime('%Y-%m-%d %H:%M:%S')
		new_data[final_file_n].append(realtime)
	unix_df = pd.DataFrame(new_data)
	name_of_file = file[:-4] + "_new.csv"
	unix_df.to_csv(os.path.join(directory, name_of_file), header=True, index=False, encoding='utf-8', mode='a')
def tagEvents(filename): 
	# read in the file as dataframe
	file = os.path.join(directory, filename)  
	df = pd.read_csv(file, header=None)
	file_n = filename[:-4]
	final_file_n = file_n + ' real time'
	tags = df[0][:]
	new_data = {	
		'unix time': [], 
		file_n: [], 
		final_file_n: []
	}

	# could also have enumerate(tags) for index and values 
	tagNum = 1
	for tag in tags: 
		new_data['unix time'].append(tag)
		new_data[file_n].append("Tag " + str(tagNum))
		# fromtimestamp; utctimestamp is 14; would subtract 5 from it; but it looks like this subtracts 4...
		realtime = datetime.fromtimestamp(tag).strftime('%Y-%m-%d %H:%M:%S')
		new_data[final_file_n].append(realtime)
		tagNum += 1
	unix_df = pd.DataFrame(new_data)
	name_of_file = file[:-4] + "_new.csv"

	unix_df.to_csv(os.path.join(directory, name_of_file), header=True, index=False, encoding='utf-8', mode='a')

def dataFrames(filename):
	# for file in files: 
	# 	print file  
	file = os.path.join(directory, filename)  
	df = pd.read_csv(file, header=None)
	file_n = filename[:-4]
	final_file_n = file_n + ' real time'

	unixtime = df[0][0]
	# print unixtime
	freq = df[0][1]
	# print freq

	fileItems = df[0][2:]


	new_data = { 
		'unix time' : [],
		file_n : [], 
		final_file_n : []
	}
	sampleNumber = 0
	for item in fileItems: 
		new_data[file_n].append(item)
		newcolumn = float(sampleNumber)/freq + unixtime 
		sampleNumber = sampleNumber + 1
		new_data['unix time'].append(newcolumn)
		realtime = datetime.fromtimestamp(newcolumn).strftime('%Y-%m-%d %H:%M:%S')
		new_data[final_file_n].append(realtime)

	df = pd.DataFrame(new_data)
	name_of_file = file[:-4] + "_new.csv"
	df.to_csv(os.path.join(directory, name_of_file), header=True, index=False, encoding='utf-8', mode='a')

	# new_input.append(name_of_file)
	

main()


	