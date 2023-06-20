# coding: utf8
"""
Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
 AAAACCCGGT

Sample Output
 ACCGGGTTTT
"""

def processData(inFileName):
    trans = str.maketrans({'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'})
    with open(inFileName) as datafile:
        return(datafile.readline().strip().translate(trans)[::-1])

"""
Personal observations : 
- The need for a special maketrans() seems odd - would be nice if translate() could do that for us.
"""
    
assert processData('sample.txt') == 'ACCGGGTTTT'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_revc_1_dataset.txt')
    resultsfile.write(str(result))