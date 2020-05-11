import os
import subprocess

def main(corpusPath):
	# the corpus is stored under "directories" and each register is in a different subdirectory
	directory = "./directories/" + str(corpusPath) + "/"
	for file in os.listdir(directory):
		path = directory + file
		rawTag = subprocess.run(['./ark-tweet-nlp-0.3.2/runTagger.sh', path], stdout=subprocess.PIPE).stdout.decode('utf-8')
		## rawTag is the complete output of the tagger which is quiet messy
		## splitList contains each paragraph as a separate list item
		splitList = rawTag.split('\n')
		taggedFinal = ''
		print(splitList)
		for paragraph in splitList:
			i = 0
			## data[0] contains the text, data[1] contains the tags
			data = paragraph.split("\t")
			for word in data[0].split(" "):
				if len(word) == 0:
					continue
				taggedFinal = taggedFinal + word + "_" + data[1].split(" ")[i] + " "
				i += 1
		with open("./gimple_tagged/%s/%s_tagged.txt" % (str(corpusPath), file.split('.')[0]), "w") as output:
			 output.write(taggedFinal)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Gimple tag files in directory')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath)
