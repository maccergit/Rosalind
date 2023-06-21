# coding: utf8
"""
Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
 GATATATGCATATACTT
 ATAT

Sample Output
 2 4 10
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        s = datafile.readline().strip()
        t = datafile.readline().strip()
    
    return(" ".join([str(x + 1) for x in range(len(s)) if s[x:(len(t) + x)] == t]))
    
assert processData('sample.txt') == '2 4 10'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_subs_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))