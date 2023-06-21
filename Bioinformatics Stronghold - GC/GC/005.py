# coding: utf8
"""
Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

Sample Dataset
 >Rosalind_6404
 CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
 TCCCACTAATAATTCTGAGG
 >Rosalind_5959
 CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
 ATATCCATTTGTCAGCAGACACGC
 >Rosalind_0808
 CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
 TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output
 Rosalind_0808
 60.919540
"""

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def computeKey(record):
    return(gc_fraction(record.seq) * 100)

def processData(inFileName):
    record = max(SeqIO.parse(inFileName, 'fasta'), key = computeKey)
    return(record.id + '\n' + '{:.6f}'.format(computeKey(record)))

"""
Personal observations : 
- Implement a way to compare BioPython sequence records, and then use built-in "max()" to find the highest value.
"""
    
assert processData('sample.txt') == 'Rosalind_0808\n60.919540'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_gc_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))