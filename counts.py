import os
import pandas as pd

def main(corpusFolder):
	data = pd.read_csv(corpusFolder + "postag_counts_clean.csv")
	counts = data.astype(bool).sum(axis=0)
	for index, count in counts.items():
		print(index + ": " + str(count) + " - " + str(count/41574))

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='rename files to not contain spaces')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
