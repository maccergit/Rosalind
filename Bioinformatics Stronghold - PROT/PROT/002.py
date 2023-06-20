# coding: utf8
"""
Translating RNA into Protein

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
 AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
 MAMAPRTEINSTRING
"""

from Bio.Seq import Seq

def processData(inFileName):
    
    with open(inFileName) as datafile:
        return(Seq(datafile.readline().strip()).translate(to_stop = True))

"""
Personal observations : 
- Much better with BioPython
"""
    
assert processData('sample.txt') == 'MAMAPRTEINSTRING'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_prot_1_dataset.txt')
    resultsfile.write(str(result))