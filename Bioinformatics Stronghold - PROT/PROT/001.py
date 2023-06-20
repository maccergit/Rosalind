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

def processData(inFileName):
    codonMapping = {'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L',
                    'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S',
                    'UAU' : 'Y', 'UAC' : 'Y', 'UAA' : '*', 'UAG' : '*',
                    'UGU' : 'C', 'UGC' : 'C', 'UGA' : '*', 'UGG' : 'W',
                    'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
                    'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
                    'CAU' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q',
                    'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',
                    'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M',
                    'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
                    'AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K',
                    'AGU' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R',
                    'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
                    'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
                    'GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E',
                    'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'}
    
    with open(inFileName) as datafile:
        data = datafile.readline().strip()
        
    codons = [data[i:i + 3] for i in range(0, len(data), 3)]
    return "".join([codonMapping[x] for x in codons if codonMapping[x] != '*'])
    
assert processData('sample.txt') == 'MAMAPRTEINSTRING'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_prot_1_dataset.txt')
    resultsfile.write(str(result))