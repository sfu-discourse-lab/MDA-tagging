import os
import re

def main(corpusFolder):
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
