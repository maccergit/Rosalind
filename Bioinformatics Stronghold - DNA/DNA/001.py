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
        counts = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
        for x in datafile.readline().strip():
            counts[x] += 1
        return(' '.join([str(counts[x]) for x in 'ACGT']))

"""
Personal observations : 
- Easy loop over string, using characters as key into hash, keeping count along the way.
- Iteration is procedural, but once we have the counts, we then can use list processing methods to convert to the correct ordering and format.
"""
    
assert processData('sample.txt') == '20 12 17 21'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_dna_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))