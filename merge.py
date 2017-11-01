import pandas as pd
import numpy as np
import functools
import os
import re

# input folder name and then merge the files - input folder for csv files 
# checking values of IBI = good 
# trying to understand why Empatica's #s look like that 
# start analyzing that data (for next week) - look at EDA column (electronic) 
# insert the tag events - insert another column "1" for when tag is used 
# merged file from person 1 and person 2 
# select times from the two tags 
# auto regressions; auto correlations 
# good for time series; 
# way to do that between 2 people
# scatter plot for one time point and another for another time plot 
# coefficient for every through = quality of collaboration 
# more synchronized 

# look into autoregression; autocorrelation 

# string_input = raw_input("Please enter files you want to merge (separate with spaces): ")
# nameofFile = raw_input("Name the file: ")

# input_list = string_input.split()
# input_list = ['ACC_new.csv', 'BVP_new.csv', 'EDA_new.csv', 'HR_new.csv', 'IBI_new.csv', 'tags_new.csv', 'TEMP_new.csv']
# directory = '/Users/yonglidich/desktop/testdirectory'
# def merge(input_list, directory): 

def merge(input_list, directory): 
	data_frames = []
	for file in input_list: 
		filename = os.path.join(directory, file)
		df1 = pd.read_table(filename, sep=',')
		# print df1
		data_frames.append(df1)

	# value = csv1['name'].values
		# value = csv1['name'].values

		# got rid of fill at the end because it was being counted as a value
		# df_merged = reduce(lambda left, right: pd.merge(left, right, on=['unix time'], how='outer'), data_frames).fillna('')

	df_merged = reduce(lambda left, right: pd.merge(left, right, on='unix time', how='outer'), data_frames)
	df_merged_sorted = df_merged.sort_values(['unix time'])

	findSlashes = (re.findall(r'/(\w+)', directory) or None)
	name = findSlashes[len(findSlashes)-1] + 'Merged.csv'
	df_merged_sorted.to_csv(os.path.join(directory, name), sep=',', na_rep='', index=False)

# merge(input_list, directory)

