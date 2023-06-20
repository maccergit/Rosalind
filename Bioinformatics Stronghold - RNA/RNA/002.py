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

from Bio.Seq import Seq

def processData(inFileName):
    with open(inFileName) as datafile:
        return(Seq(datafile.readline().strip()).transcribe())

"""
Personal observations : 
- Biopython makes this a bit more readable as to what we want
"""
    
assert processData('sample.txt') == 'GAUGGAACUUGACUACGUAAAUU'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_rna_1_dataset.txt')
    resultsfile.write(str(result))