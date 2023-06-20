# coding: utf8
"""
Introduction to the Bioinformatics Armory

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
Note: You must provide your answer in the format shown in the sample output below.

Sample Dataset
 AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
 20 12 17 21
"""

from Bio.Seq import Seq

def processData(inFileName):
    with open(inFileName) as datafile:
        data = Seq(datafile.readline().strip())
    return(' '.join([str(data.count(x)) for x in 'ACGT']))

"""
Personal observations : 
- Using BioPython.  A trivial case, where the sequence is treated just like a string.
"""
    
assert processData('sample.txt') == '20 12 17 21'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ini.txt')
    print(result)
    resultsfile.write(str(result))