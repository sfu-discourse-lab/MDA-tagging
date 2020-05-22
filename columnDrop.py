import os
import pandas as pd

def main(corpusFolder):
	data = pd.read_csv(corpusFolder + "normalized_postag_counts.csv")
	newData = data.drop(['HASHTAG', 'PROCONTRACT', 'CONTRACTPROQUAN', 'POSESPROQUAN', 'SWEAR', 'SINFLECT', 'THATADJCOMP', 'INITIALMENTION'], axis=1)
	newData.to_csv(corpusFolder + "normalized_postag_counts_clean.csv", index=False)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='rename files to not contain spaces')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
