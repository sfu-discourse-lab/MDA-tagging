# ----------------------------------------------------------------
# find and retrieve comment threads of size greater than 700 words
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------


import pandas as pd
import nltk
from nltk import word_tokenize
import csv
from pathlib import Path


def findThreads(inputFile, outputFolder):
	"""finds threads of length greater than 700 words
	
	Iterate through the input data to find threads of lenght greater than 700 words
	and store the commonts in a csv together with an ID indicating which thread
	it is from.
	"""
	data = pd.read_csv(inputFile)
	first = data["comment_counter"].iloc[0]
	last_id = first.split('_')[1] + first.split('_')[2]
	threadSize = 0
	numComments = 0
	dataDict = {}
	threadsTotal = 0

	with open('%sgnm_threads.csv' %outputFolder, mode='w') as output:
		writer = csv.writer(output, delimiter=',')
		writer.writerow(["id"] + ["text"])
		for index, row in data.iterrows():
	        	# if current comment is in same thread add to dict
			if row[1].split('_')[1] + row[1].split('_')[2] == last_id:
				dataDict[row[1]] = row[6]
				threadSize += len(word_tokenize(row[6]))
				numComments += 1
				last_id = row[1].split('_')[1] + row[1].split('_')[2]
				continue
			# if threadsize >= 700 words and contains at least 2 comments
			# then thread is written to csv
			if threadSize >= 700 and numComments > 2:
				threadsTotal += 1
				writer = csv.writer(output, delimiter=',')
				for x in dataDict:
					writer.writerow([x] + [dataDict[x]])
                    
			dataDict.clear()
			threadSize = 0
			numComments = 0
			# initialize variables for next thread using values of initial comment
			dataDict[row[1]] = row[6]
			threadSize += len(word_tokenize(row[6]))
			numComments += 1
			last_id = row[1].split('_')[1] + row[1].split('_')[2]

def storeThreads(outputFolder):
	"""store each thread in separate .txt file

	retrieve the threads from the gnm_threads csv and store each thread
	in an individual .txt file for future cleaning and analysis
	"""
	data = pd.read_csv('%sgnm_threads.csv' %outputFolder)

	first = data["id"].iloc[0]
	last = first.split('_')[1] + first.split('_')[2]
	text = ""
	filename = first

	# loop over comments and string concatenate them together on one line before writing to file
	for index, row in data.iterrows():
		if row[0].split('_')[1] + row[0].split('_')[2] == last:
			text += row[1] + " "
		else:

			with open('%sthreads/%s.txt' %(outputFolder, filename), 'w') as out:
				out.write(text)
			text = row[1] + " "
			filename = row[0]
		last = row[0].split('_')[1] + row[0].split('_')[2]

def main(inputFile, outputFolder):

	Path(outputFolder).mkdir(parents=True, exist_ok=True)
	Path(outputFolder + "threads/").mkdir(parents=True, exist_ok=True)

	findThreads(inputFile, outputFolder)
	storeThreads(outputFolder)


if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description='select comment threads of more than 700 words')
	parser.add_argument('inputFile', type=str, help='the path to the input csv')
	parser.add_argument('outputFolder', type=str, help='the path to the output folder; eg. ./folder1/folder2/')
	args = parser.parse_args()
	
	main(args.inputFile, args.outputFolder)
