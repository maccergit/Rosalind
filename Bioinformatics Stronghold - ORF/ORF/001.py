# coding: utf8
"""
Open Reading Frames

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
 >Rosalind_99
 AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
 MLLGSFRLIPKETLIQVAGSSPCNLS
 M
 MGMTPRLGLESLLE
 MTPRLGLESLLE
"""

import fasta
from Bio.Seq import Seq

def getReverseComplement(s):
    return(Seq(s).reverse_complement())

def getStartIndices(s):
    return([i for i in range(len(s)) if s[i:i + 3] == 'ATG'])

def getOrfsFromStarts(s, starts):
    result = set()
    for start in starts:
        stop = 0
        for i in range(start, len(s), 3):
            if stop == 0 and s[i:i + 3] in ['TAG', 'TGA', 'TAA']:
                stop = i
        if stop != 0:
            result.add(s[start:stop + 3])
    return(result)

def mapToProteins(orfs):
    return(set(str(x) for x in set((orf.translate(to_stop = True) for orf in orfs))))
            

def processData(inFileName):
    # Parse the FASTA file - probably overkill for this problem, as we don't car care about the FASTA IS, and it's only a single record.
    # Make these BioPython sequences to make life easy.
    records = fasta.readFastaFile(inFileName)
    s1 = Seq(list(records.values())[0])
    s2 = getReverseComplement(s1)
    
    # Find all start codons at any point along the string.
    starts1 = getStartIndices(s1)
    starts2 = getStartIndices(s2)
    
    # Get sequences that start with the start codon and end with the first stop codon later in the string.
    # NOTE - for each start codon, we have a frame, and subsequent codons align to triplets thereafter.
    # NOTE - if no stop codon appears after the start codon, then the start codon is no good and can be discarded.
    # NOTE - we use a set here to avoid duplicate sequences.  This is not entirely sufficient, as different sequences can produce the same protein.
    # However, pruning early can help avoid unnecessary work.
    
    orfs = getOrfsFromStarts(s1, starts1)
    orfs.update(getOrfsFromStarts(s2, starts2))
    
    # Map ORF sequences to proteins, storing results into another set (to avoid duplicates) - and then format as result.
    return('\n'.join(mapToProteins(orfs)))

"""
Personal observations : 
- Once again, BioPython saves a lot of work.
"""

# Do set comparisons, since lines can be in any order
assert set(processData('sample.txt').split('\n')) == set(('MLLGSFRLIPKETLIQVAGSSPCNLS',
                                                          'M', 
                                                          'MGMTPRLGLESLLE',
                                                          'MTPRLGLESLLE'))

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_orf_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))