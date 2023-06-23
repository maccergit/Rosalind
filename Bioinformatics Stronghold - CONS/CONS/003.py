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
from collections import Counter

def processData(inFileName):
    # Parse the FASTA file
    records = fasta.readFastaFile(inFileName)

    # assumption - all records have sequence of same length
    width = len([x for x in records.values()][0])
    
    # build the profile matrix as a list of Counters
    profileMatrix = []
    for index in range(width):
        bases = [records[fastaid][index] for fastaid in records]
        profileMatrix.append(Counter(bases))
    
    # compute consensus results by getting the most_common element of each Counter
    result = ''
    for index in range(width):
        result += profileMatrix[index].most_common(1)[0][0]
    print(result)
    
    # add formatted profileMatix to result - note that we provide the default 0 for bases that were missing, and thus not counted.
    for base in 'ACGT':
        result += '\n' + base + ': ' + ' '.join([str(counter.get(base, 0)) for counter in profileMatrix])
    
    return(result)

"""
Personal observations : 
- Use Counter to provide counts and most common base.
"""
    
assert processData('sample.txt') == """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_cons_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))