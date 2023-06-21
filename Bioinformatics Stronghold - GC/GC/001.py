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

# Read an entire FASTA formatted file into memory, returning a dictionary keyed by genome ID, with sequence strings as values.
def readFASTA(inFileName):
    retval = {}
    key = ''
    data = ''
    with open(inFileName) as f:
        for line in (x.strip() for x in f.readlines()):
            if line[0] == '>':
                if key != '':
                    retval[key] = data
                    data = ''
                key = line[1:]
            else:
                data += line
    retval[key] = data
    return retval

# Given a gnome sequence, compute the GC ratio
def computeGC(data):
    return len([1 for x in data if x in ['G', 'C']]) / len(data)

def processData(inFileName):
    fasta_data = readFASTA(inFileName)
    maxGC = 0
    for key in fasta_data:
        gc = computeGC(fasta_data[key])
        if gc > maxGC:
            maxGC = gc
            result = key + '\n' + '{:.6f}'.format(maxGC * 100)
    return(result)
    
assert processData('sample.txt') == 'Rosalind_0808\n60.919540'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_gc_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))