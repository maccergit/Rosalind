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
    index = 0
    done = False
    while not done:
        try:
            start = s.index(t, index) + 1
        except ValueError:
            done = True
        if not done:
            result.append(str(start))
            index = start + 1
    return(" ".join(result))
    
assert processData('sample.txt') == '2 4 10'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_subs_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))