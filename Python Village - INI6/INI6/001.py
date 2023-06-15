# coding: utf8
"""
Intro to Python dictionary

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

Sample Dataset
 We tried list and we tried dicts also we tried Zen

Sample Output
 and 1
 We 1
 tried 3
 dicts 1
 list 1
 we 2
 also 1
 Zen 1
"""

def processData(inFileName, outFileName):
    words = {}
    with open(outFileName, 'w') as resultsFile:
        with open(inFileName) as datafile:
            for word in next(datafile).split():
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        for word, count in words.items():
            resultsFile.write(word + ' ' + str(count) + '\n')

"""
Personal observations : 
- Simple procedural approach - read words, adding them to dictionary with initial count of 1 if not already there, or adding to the count if they are - then iterate over the
dictionary to produce the results.
"""
    
processData('sample.txt', 'sampleresults.txt')

processData('rosalind_ini6_1_dataset.txt', 'results.txt')

print('done')