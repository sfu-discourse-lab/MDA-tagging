import os

def main(corpusPath):
	directory = corpusPath
	for file in os.listdir(directory):
		path = directory + file
		os.system('perl ./Clarke_Tagger_2018.txt %s' % path)
		with open("mdatagtweets01.txt", "r") as f:
			with open("./clarke_tagged/%s_tagged.txt" % file.rsplit('_', 1)[0], "w") as output:
				for line in f:
					output.write(line)
		os.remove("mdatagtweets01.txt")

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Clarke tag files in directory')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath)