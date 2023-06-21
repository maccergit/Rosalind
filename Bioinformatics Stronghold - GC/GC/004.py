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

def processData(inFileName):
    maxGC = 0
    for record in SeqIO.parse(inFileName, 'fasta'):
        gc = gc_fraction(record.seq)
        if gc > maxGC:
            maxGC = gc
            result = record.id + '\n' + '{:.6f}'.format(maxGC * 100)
    return(result)

"""
Personal observations : 
- Once you start using a portion of BioPython, you get other functionality as well.
"""
    
assert processData('sample.txt') == 'Rosalind_0808\n60.919540'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_gc_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))