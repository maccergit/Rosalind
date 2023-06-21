# coding: utf8
"""
Counting Point Mutations

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
 GAGCCTACTAACGGGAT
 CATCGTAATGACGGCCT

Sample Output
 7
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        s = datafile.readline().strip()
        t = datafile.readline().strip()
    return(str(len([1 for x in range(len(s)) if s[x] != t[x]])))
    
assert processData('sample.txt') == '7'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_hamm_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))