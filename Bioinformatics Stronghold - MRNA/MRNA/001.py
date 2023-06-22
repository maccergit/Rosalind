# coding: utf8
"""
Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
(Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
 MA

Sample Output
 12
"""

from math import prod

codonMap = {'F' : ['UUU', 'UUC'],
            'L' : ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
            'S' : ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
            'Y' : ['UAU', 'UAC'],
            '*' : ['UAA', 'UAG', 'UGA'],
            'C' : ['UGU', 'UGC'],
            'W' : ['UGG'],
            'P' : ['CCU', 'CCC', 'CCA', 'CCG'],
            'H' : ['CAU', 'CAC'],
            'Q' : ['CAA', 'CAG'],
            'R' : ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
            'V' : ['GUU', 'GUC', 'GUA', 'GUG'],
            'A' : ['GCU', 'GCC', 'GCA', 'GCG'],
            'D' : ['GAU', 'GAC'],
            'E' : ['GAA', 'GAG'],
            'G' : ['GGU', 'GGC', 'GGA', 'GGG'],
            'I' : ['AUU', 'AUC', 'AUA'],
            'M' : ['AUG'],
            'T' : ['ACU', 'ACC', 'ACA', 'ACG'],
            'N' : ['AAU', 'AAC'],
            'K' : ['AAA', 'AAG']}

def processData(inFileName):
    with open(inFileName) as datafile:
        protein = datafile.readline().strip() + '*'
    return(str(prod([len(codonMap[x]) for x in protein]) % 1000000))
    
assert processData('sample.txt') == '12'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_mrna_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))