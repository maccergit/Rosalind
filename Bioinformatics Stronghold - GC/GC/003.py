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

# Given a gnome sequence, compute the GC ratio
def computeGC(data):
    return len([1 for x in data if x in ['G', 'C']]) / len(data)

def processData(inFileName):
    maxGC = 0
    for record in SeqIO.parse(inFileName, 'fasta'):
        gc = computeGC(record.seq)
        if gc > maxGC:
            maxGC = gc
            result = record.id + '\n' + '{:.6f}'.format(maxGC * 100)
    return(result)

"""
Personal observations : 
- BioPython provides almost the same functionality as the library, but probably handles edge cases better, and may perform better.  It also handles other file formats.
- If you can find a good library that does what you need, then don't roll your own.
"""
    
assert processData('sample.txt') == 'Rosalind_0808\n60.919540'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_gc_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))