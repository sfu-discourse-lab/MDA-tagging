# ----------------------------------------------------------------
# combine columns of lesser features into macro features and drop merged columns
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os
import pandas as pd

def main(corpusFolder):
	data = pd.read_csv(corpusFolder + "postag_counts.csv")

	# combine various punctuation tags into one 'PUNC' tag
	punc = data['BRACKET'] + data['CAPS'] + data['COLON'] + data['COMMA'] + data['EXCLAM'] + data['FULSTOP'] + data['QUES'] + data['SMCOLON']
	data['PUNC'] = punc

	# combine various web tags inton one 'WEB' tag
	web = data['ELIPS'] + data['EMOTICON'] + data['HASHTAG'] + data['LAUGH'] + data['MENTION'] + data['URL']
	data['WEB'] = web

	# combine various IVB tags inton one 'IVB' tag
	ivb = data['DOIVB'] + data['HAVEIVB'] + data['IVB']
	data['IVB'] = ivb

	# combine various interjection tags into one 'INTJ' tag
	intj = data['OTHRINTJ'] + data['POSINTJ'] + data['NEGINTJ']
	data['INTJ'] = intj

	# combine various initial verb tags into one 'VBI' tag
	vbi = data['VBIG'] + data['VBIMD'] + data['VBIQ'] + data['VBIS'] + data['VBIX']
	data['VBI'] = vbi

	newData = data.drop(['BRACKET', 'CAPS', 'COLON', 'COMMA', 'EXCLAM', 'FULSTOP', 'QUES', 'SMCOLON', 'ELIPS', 'EMOTICON', 'HASHTAG', 'LAUGH', 'MENTION', 'URL', 'DOIVB', 'HAVEIVB', 'IVB', 'OTHRINTJ', 'POSINTJ', 'NEGINTJ', 'VBIG', 'VBIMD', 'VBIQ', 'VBIS', 'VBIX', 'CONTRACTWH', 'POSSPRO', 'PROCONTRACT', 'CONTRACTPROQUAN', 'POSESPROQUAN', 'SWEAR', 'SINFLECT', 'THATADJCOMP', 'INITIALMENTION'], axis=1)
	newData.to_csv(corpusFolder + "postag_counts_clean.csv", index=False)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='combine lesser features into macro features and remove extra columns')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
