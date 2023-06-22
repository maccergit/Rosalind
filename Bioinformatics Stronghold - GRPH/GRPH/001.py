# coding: utf8
"""
Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset
 >Rosalind_0498
 AAATAAA
 >Rosalind_2391
 AAATTTT
 >Rosalind_2323
 TTTTCCC
 >Rosalind_0442
 AAATCCC
 >Rosalind_5013
 GGGTGGG

Sample Output
 Rosalind_0498 Rosalind_2391
 Rosalind_0498 Rosalind_0442
 Rosalind_2391 Rosalind_2323
"""

import fasta

def processData(inFileName):
    # Parse the FASTA file
    records = fasta.readFastaFile(inFileName)
    
    # Build the prefix map
    prefixmap = {}
    for fastaid in records:
        prefix = records[fastaid][:3]
        if prefix not in prefixmap:
            prefixmap[prefix] = []
        prefixmap[prefix].append(fastaid)
    
    # Find the overlaps, building the results along the way
    retval = ''
    for fastaid in records:
        postfix = records[fastaid][-3:]
        if postfix in prefixmap:
            overlaps = [x for x in prefixmap[postfix] if x != fastaid]
            for overlapid in overlaps:
                retval += fastaid + ' ' + overlapid + '\n'
    retval = retval[:-1]
    return(retval)
    
assert processData('sample.txt') == """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_grph_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))