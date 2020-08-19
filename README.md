#### MDA\_OnlineRegisters

Supplementary materials for the Online Registers MDA analysis.

#### Process Write-up

###### SOCC
Prior to tagging the SOCC corpus we first selected all comment threads containing more than 700 words, this was done using dataSelection.py which stores each thread in a separate file.

After retrieving the threads the CORE\_cleanup.py script was ran on the data to remove various data gathering artifacts.

After cleanup Gimple\_Wrapper.py was run on the dataset to Gimple tag the threads after which the Clarke\_Wrapper.py was run to Clarke tag the files.

No problems were encountered with this dataset and all features were counted using the postag_counter.py script to create frequency matrices.

###### CORE
For the CORE corpus the CORE_cleanup.py script was ran to remove all html tags and other artifacts from the data gathering step.

CORE\_rename.py was run on the files to give each file the correct prefix and remove whitespace from filenames.

After this step the Gimple tagger was run using Gimple\_Wrapper.py. Due to encoding problems in certain proper nouns containing vowels with accent marks we turned on "error: ignore" which removes all instances of bad encoding. This did not seem to have an impact on the tagger as it would still recognize these words as proper nouns. After this the Clarke\_Wraper.py was run without any problem

The postag_counter.py was run to retrieve the feature counts and store them in a csv file.

###### Data combination

We removed all features that were contained in less than 5% of all files by identifying them using the counts.py script and removing the columns from the frequency matrix using the columnDrop.py script.

All frequency matrices for CORE and SOCC were then combined into one file using the csv_combine.py script.

#### Overview and description of the files (in alphabetical order):

###### Clarke\_Tagger\_2018.txt

This Clarke tagger is slightly modified to interface correctly with the Gimple tagger used in this project.

###### Clarke\_Wrapper.py

Python script calls the Clarke tagger on all files within the specified corpus folder.

###### columnDrop.py 

Script for removing the specified columns from a .csv file.

###### CORE\_cleanup.py

Python script for removing various artifacts from the data collection process.

###### CORE\_rename.py

Script for renaming files to contain the correct register label.

###### counts.py

Script for calculating the percentage of files each feature occurs in.

###### csv\_combine.py

Script for combining multiple csv files to create one frequency matrix.

###### dataSelection.py

Python script for selecting threads of >700 words from the SOCC comment file

###### Gimple\_Wrapper.py

This python cripts calls the Gimple tagger on all files within the specified corpus folder.

###### postag\_counter.py

Python script for counting all POS tags specified in the input file.

###### removeSpace.py

Short script for removing whitespace from file names.
