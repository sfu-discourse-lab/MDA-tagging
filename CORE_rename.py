# ----------------------------------------------------------------
# remove spaces from file names and add correct filename prefix
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os
import re

def main(corpusFolder):
	# remove whitespace from file names
        for folder in os.listdir(corpusFolder):
                for file in os.listdir(corpusFolder+folder):
                        os.rename(corpusFolder + folder + '/' + file, corpusFolder + folder + '/' +  re.sub(r' ', '', file))

	for file in os.listdir(corpusFolder):
		# change the following line with the correct prefix
		newName = '31_IDE_res_' + file.rsplit('+', 1)[1]
		os.rename(corpusFolder + file, corpusFolder + newName)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='remove artifacts from data collection process')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath)
