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
 
better flattening using itertools
"""

import collections
import itertools

def processData(inFileName, outFileName):
    with open(outFileName, 'w') as resultsFile:
        with open(inFileName) as datafile:
            for word, count in collections.Counter(itertools.chain.from_iterable(x.strip().split() for x in datafile.readlines())).items():
                resultsFile.write(word + ' ' + str(count) + '\n')
    
processData('sample.txt', 'sampleresults.txt')

processData('rosalind_ini6_1_dataset.txt', 'results.txt')

print('done')