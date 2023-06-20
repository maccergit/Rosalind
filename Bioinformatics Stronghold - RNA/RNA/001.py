# coding: utf8
"""
Transcribing DNA into RNA

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
 GATGGAACTTGACTACGTAAATT

Sample Output
 GAUGGAACUUGACUACGUAAAUU
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        return(datafile.readline().strip().replace('T', 'U'))

"""
Personal observations : 
- Sometimes, python makes the solution trivial
"""
    
assert processData('sample.txt') == 'GAUGGAACUUGACUACGUAAAUU'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_rna_1_dataset.txt')
    resultsfile.write(str(result))