from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

# Fixing random state for reproducibility
file = raw_input("Enter first file: ")
df = pd.read_csv(file).fillna('0')

file2 = raw_input("Enter second file: ")
df2 = pd.read_csv(file2).fillna('0')
# print df
# np.random.seed(19680801)

imageName = raw_input("Name your plot: ")

string_input = raw_input("What columns do you want to plot?:")
input_list = string_input.split()
name = imageName[:-4] + 'Scatter.csv'

def merge(file, file2): 
	data_frames = [df, df2]
	df_merged = reduce(lambda left, right: pd.merge(left, right, on='unix time', how='outer'), data_frames)
	df_merged_sorted = df_merged.sort_values(['unix time'])

	
	mergedDF = df_merged_sorted.to_csv(name, sep=',', na_rep='', index=False)

# # print df['BVP']
def scatter(file):
	df = pd.read_csv(file).fillna('0')
	# if len(input_list) == 1:
	# 	column = input_list[0]
	# 	x = df[column]
	# 	y = df[column]
	# elif len(input_list) > 2: 
	# 	print "error" # error, only two columns right now
	# else: 
	x_input = input_list[0]
	y_input = input_list[1]
	x = df[x_input]
	y = df[y_input]

	plt.scatter(x, y, c="g")
	plt.title(imageName[:-4])
	plt.xlabel(x_input)
	plt.ylabel(y_input)
	plt.legend(loc=2)
	plt.savefig(imageName)
	plt.show()

merge(file, file2)
scatter(name)