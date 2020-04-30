import os
import subprocess

def main(corpusPath):
	directory = corpusPath
	for file in os.listdir(directory):
		path = directory + file
		rawTag = subprocess.run(['./ark-tweet-nlp-0.3.2/runTagger.sh', path], stdout=subprocess.PIPE).stdout.decode('utf-8')
		splitList = rawTag.split('\t')
		i = 0
		taggedFinal = ''
		for word in splitList[0].split():
			taggedFinal = taggedFinal + word + "_" + splitList[1].split(" ")[i] + " "
			i += 1
		with open("./gimple_tagged/%s_tagged.txt" % file.split('.')[0], "w") as output:
			output.write(taggedFinal)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Gimple tag files in directory')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath)
