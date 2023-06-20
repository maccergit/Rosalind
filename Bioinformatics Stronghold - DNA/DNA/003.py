# coding: utf8
"""
Counting DNA Nucleotides

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
 AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
 20 12 17 21
"""

from collections import Counter

def processData(inFileName):
    with open(inFileName) as datafile:
        counts = Counter(datafile.readline().strip())
    return(' '.join([str(counts[x]) for x in 'ACGT']))

"""
Personal observations : 
- Use collections.Counter class
- Easer to read than explicit coding with hash buckets, but still only a single pass.
"""
    
assert processData('sample.txt') == '20 12 17 21'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_dna_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))