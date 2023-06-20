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

def processData(inFileName):
    with open(inFileName) as datafile:
        data = datafile.readline().strip()
    return(' '.join([str(data.count(x)) for x in 'ACGT']))

"""
Personal observations : 
- Use the built in string "count()" method.
- Easier to read, but may iterate over the string multiple times, rather than a single pass.
"""
    
assert processData('sample.txt') == '20 12 17 21'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_dna_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))