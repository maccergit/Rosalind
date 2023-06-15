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
            resultsFile.write(''.join(datafile.readlines()[1::2]))

"""
Personal observations : 
- Read the entire file in all at once as a sequence of lines, slice the entire sequence with a skip over odd lines (note that 0th entry is line 1, which is odd), and then
join them all together into a single string to write to results files (note that line endings are read in and kept at end of each line - no need to add them).
"""
    
processData('sample.txt', 'sampleresults.txt')

processData('rosalind_ini5_1_dataset.txt', 'results.txt')

print('done')