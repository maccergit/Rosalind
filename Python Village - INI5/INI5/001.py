# coding: utf8
"""
Reading and Writing

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

Sample Dataset
 Bravely bold Sir Robin rode forth from Camelot
 Yes, brave Sir Robin turned about
 He was not afraid to die, O brave Sir Robin
 And gallantly he chickened out
 He was not at all afraid to be killed in nasty ways
 Bravely talking to his feet
 Brave, brave, brave, brave Sir Robin
 He beat a very brave retreat

Sample Output
 Yes, brave Sir Robin turned about
 And gallantly he chickened out
 Bravely talking to his feet
 He beat a very brave retreat
"""

def processData(inFileName, outFileName):
    with open(outFileName, 'w') as resultsFile:
        with open(inFileName) as datafile:
            count = 1
            for text in datafile:
                if count % 2 == 0:
                    resultsFile.write(text)
                count += 1

"""
Personal observations : 
- No unit test here - the result is not a simple string that can be tested with an assert.
- Simple procedural approach - keep a line counter, and only write the even numbered lines back out.
"""
    
processData('sample.txt', 'sampleresults.txt')

processData('rosalind_ini5_1_dataset.txt', 'results.txt')

print('done')