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
    result = []
    start = s.find(t)
    while start > -1:
        result.append(str(start + 1))
        start = s.find(t, start + 1)
    return(" ".join(result))
    
assert processData('sample.txt') == '2 4 10'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_subs_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))