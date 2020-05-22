import os
import re

def main(corpusFolder):
	for folder in os.listdir(corpusFolder):
		for file in os.listdir(corpusFolder+folder):
			os.rename(corpusFolder + folder + '/' + file, corpusFolder + folder + '/' +  re.sub(r' ', '', file))

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='rename files to not contain spaces')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
