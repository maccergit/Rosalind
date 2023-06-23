# coding: utf8
"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
 >Rosalind_1
 ATCCAGCT
 >Rosalind_2
 GGGCAACT
 >Rosalind_3
 ATGGATCT
 >Rosalind_4
 AAGCAACC
 >Rosalind_5
 TTGGAACT
 >Rosalind_6
 ATGCCATT
 >Rosalind_7
 ATGGCACT

Sample Output
 ATGCAACT
 A: 5 1 0 0 5 5 0 0
 C: 0 0 1 4 2 0 6 1
 G: 1 1 6 3 0 1 0 0
 T: 1 5 0 0 0 1 1 6
"""

import fasta

def processData(inFileName):
    # Parse the FASTA file
    records = fasta.readFastaFile(inFileName)
    
    # assumption - all records have sequence of same length
    width = len([x for x in records.values()][0])
    
    # build the profile matrix
    profileMatrix = {'A' : [0] * width, 'C' : [0] * width, 'G' : [0] * width, 'T' : [0] * width}
    for fastaid in records:
        index = 0
        for base in records[fastaid]:
            profileMatrix[base][index] += 1
            index += 1
    
    # compute consensus results
    result = ''
    for index in range(width):
        baseCounts = [profileMatrix[base][index] for base in 'ACGT']
        result += ['A', 'C', 'G', 'T'][baseCounts.index(max(baseCounts))]
    
    # add formatted profileMatix to result
    for base in 'ACGT':
        result += '\n' + base + ': ' + ' '.join([str(x) for x in profileMatrix[base]])
    
    return(result)

"""
Personal observations : 
- Start with profile matrix of all '0' and step through each sequence in turn - update tally as we move along the sequences.
"""
    
assert processData('sample.txt') == """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_cons_1_dataset.txt')
    resultsfile.write(str(result))