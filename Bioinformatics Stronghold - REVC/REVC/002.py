# coding: utf8
"""
Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
 AAAACCCGGT

Sample Output
 ACCGGGTTTT
"""

from Bio.Seq import Seq

def processData(inFileName):
    with open(inFileName) as datafile:
        return(Seq(datafile.readline().strip()).reverse_complement())

"""
Personal observations : 
- Much nicer with BioPython - we don't get lost in the implementation details
"""
    
assert processData('sample.txt') == 'ACCGGGTTTT'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_revc_1_dataset.txt')
    resultsfile.write(str(result))