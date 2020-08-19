# ----------------------------------------------------------------
# wrapper to run the Clarke Tagger on entire directory
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os

def main(corpusPath):
	directory = './gimple_tagged/' + corpusPath + '/'
	for file in os.listdir(directory):
		path = directory + file
		os.system('perl ./Clarke_Tagger_2018.txt %s %s' % (path, str(corpusPath)))
		with open("mdatagtweets%s.txt" % str(corpusPath), "r") as f:
			with open("./clarke_tagged/%s/%s_tagged.txt" % (str(corpusPath), file.rsplit('_', 1)[0]), "w") as output:
				for line in f:
					output.write(line)
		os.remove("mdatagtweets%s.txt" % str(corpusPath))

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Clarke tag files in directory')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath)
