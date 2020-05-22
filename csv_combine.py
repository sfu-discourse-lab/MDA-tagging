import os

def main(corpusFolder):
	fout = open(corpusFolder + "postag_counts.csv", 'a')

	for line in open(corpusFolder + "postag_counts1.csv"):
		fout.write(line)

	for num in range(2,3):
		f = open(corpusFolder + "postag_counts" + str(num) + ".csv")
		i = 0
		for line in f:
			if i == 0:
				i += 1
				continue
			fout.write(line)
			i += 1
		f.close()
	fout.close()

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='rename files to not contain spaces')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus')
	args = parser.parse_args()
	main(args.corpusPath)
