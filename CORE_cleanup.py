# ----------------------------------------------------------------
# remove various text retrieval artifacts such as html tags
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os
import re

def main(corpusFolder):
	for folder in os.listdir(corpusFolder):
		os.mkdir('./CORE_registers_untagged_textOnly/' + folder)
		for file in os.listdir(corpusFolder + folder):
			i = 0
			# all files contained headers with metadata from the webpage which has to be removed
			# metadata was contained in the first 4-5 lines and was separated from main text by a newline
			with open(corpusFolder + folder + "/" + file, 'r', encoding="latin-1") as inputFile:
				for line in inputFile:
					if line == "\n":
						i+1
						break
					i+1
				lines = inputFile.readlines()[i:]
			# artifacts such as html tags and separators such as repeating strings of dashes need to be removed
			with open('./CORE_registers_untagged_textOnly/'+ folder + '/' + file, 'w') as output:
				for line in lines:
					first = re.sub(r'<.{1,3}> ', '', line)
					second = re.sub(r'_{4,100} ', '', first)
					third = re.sub(r'-{4,100}', '', second)
					fourth = re.sub(r'~{4,100}', '', third)
					output.write(fourth)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='remove artifacts from data collection process')
	parser.add_argument('corpusPath', type='str', help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath) 
