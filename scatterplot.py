from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

# Fixing random state for reproducibility
file = raw_input("Enter first file: ")
df = pd.read_csv(file)


file2 = raw_input("Enter second file: ")
df2 = pd.read_csv(file2)
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
# for l in lst: 
	# 	if type(l) is int:
	# 		print "int" , l
	# 	elif type(l) is str: 
	# 		print "str" , l
	# print lst 
def normalize(lst):

	# base = min(lst)
	# ranges = max(lst) - base
	#  map(lambda x: (x-base)/ranges, lst)

	# return [(x-base)/ranges for x in lst]

	base = min(lst)
	ranges = max(lst) - base

	return map(lambda x: (x-base)/ranges, lst)

def scatter(file):
	df= pd.read_csv(file).fillna(np.nan)
	# print df
	# df = df_other.replace('', np.nan)
	# if len(input_list) == 1:
	# 	column = input_list[0]
	# 	x = df[column]
	# 	y = df[column]
	# elif len(input_list) > 2: 
	# 	print "error" # error, only two columns right now
	# else: 
	x_input = input_list[0]
	y_input = input_list[1]

	# for value in df["tag"]: 
	# 	if value == "Tag 1":

	# left person 
	index_tag1 = df.index[df['tags_x'] == "Tag 5"]
	index_tag2 = df.index[df['tags_x'] == "Tag 6"]
	new_df = df.iloc[index_tag1[0]:index_tag2[0]]
	# masked = pd.isnull(np.ma.array(new_df, mask=np.isnan(new_df)))
	# print "new_df: " , new_df

	# x = (new_df[x_input] - new_df[x_input].mean())/new_df[x_input].std()
	# x = normalize(new_df[x_input])
	# y = normalize(new_df[y_input])
	x = new_df[x_input]
	y = new_df[y_input]

	# y = (new_df[y_input] - new_df[y_input].mean())/new_df[y_input].std()
	# x = normalize(np.ma.masked_where(new_df[x_input] == np.isnan
	# 	array(new_df[x_input], mask=np.isnan(new_df[x_input])))
	# print "x: " , x 
	# y = normalize(np.ma.array(new_df[y_input], mask=np.isnan(new_df[y_input])))
	# print "y: " , y 

	plt.scatter(x, y, c="g")
	plt.title(imageName[:-4])
	plt.xlabel(x_input)
	plt.ylabel(y_input)
	plt.legend(loc=2)
	plt.savefig(imageName)
	plt.show()

merge(file, file2)
scatter(name)