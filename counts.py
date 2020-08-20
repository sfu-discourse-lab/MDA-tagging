# ----------------------------------------------------------------
# find the percentage of texts containing a specific feature
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os
import pandas as pd

def main(corpusFolder):
	data = pd.read_csv(corpusFolder + "postag_counts.csv")
	counts = data.astype(bool).sum(axis=0)
	for index, count in counts.items():
		print(index + ": " + str(count) + " - " + str(count/41574))

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='count and find percentage of occurrences of feature in files.')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
