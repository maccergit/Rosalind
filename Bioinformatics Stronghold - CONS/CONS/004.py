# coding: utf8
"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
 >Rosalind_1
 ATCCAGCT
 >Rosalind_2
 GGGCAACT
 >Rosalind_3
 ATGGATCT
 >Rosalind_4
 AAGCAACC
 >Rosalind_5
 TTGGAACT
 >Rosalind_6
 ATGCCATT
 >Rosalind_7
 ATGGCACT

Sample Output
 ATGCAACT
 A: 5 1 0 0 5 5 0 0
 C: 0 0 1 4 2 0 6 1
 G: 1 1 6 3 0 1 0 0
 T: 1 5 0 0 0 1 1 6
"""

import fasta
from collections import Counter

class ProfileMatrix:
    """
    A profile matrix built from a list of DNA strings (not FASTA records).  It will automatically count the bases in the sequences and figure out
    a consensus base for each location in the strings.  The consensus results are available as a list, or a string.  the underlying counts are 
    available as a list of counts for a given base, or as a dictionary of all the counts keyed by the bases.
    
    Currently specific for DNA strings, so the bases are assumed to be 'ACGT' - but could be generalized to accept string or list of bases for use.
    Note that bases cannot be explicitly determined from the passed in sequences, as there could be a base that is never used, and thus would be missed.
    It may be possible to infer some alphabets from the provided data, but explicit is better than implicit,
    """
    baseCounts = []
    
    def __init__(self, sequences):
        """
        Given a list of DNA strings, built the profile matrix - missing bases are skipped over (there are no 0 counts internally).
        """
        for index in range(len(sequences[0])):
            self.baseCounts.append(Counter([seq[index] for seq in sequences]))
    
    def getConsensus(self):
        """
        Return the consensus list of bases.  No problem with missing bases, as there will always be at least one base in each position.
        """
        return([counter.most_common(1)[0][0] for counter in self.baseCounts])
    
    def getConsensusString(self):
        """
        Return the consensus list as a DNA string.
        """
        return("".join([str(x) for x in self.getConsensus()]))
    
    def getBaseCounts(self, base):
        """
        Return a list of the computed counts for a given base - if the base was missing for a position, the count is inferred to be 0.
        """
        return([counter.get(base, 0) for counter in self.baseCounts])
    
    def getCounts(self):
        """
        Return a dictionary of all the computed counts for all bases, keyed by the base.  Assumed to be DNA, so bases are A, C, G, and T.
        """
        return({base : self.getBaseCounts(base) for base in 'ACGT'})

def processData(inFileName):
    # Parse the FASTA file
    records = fasta.readFastaFile(inFileName)
    
    # Create the profile matrix from just the sequences
    pm = ProfileMatrix([records[fastaid] for fastaid in records])
    
    # format and return the result string
    return(pm.getConsensusString() + '\n' +'\n'.join([base + ': ' + " ".join([str(x) for x in pm.getBaseCounts(base)]) for base in 'ACGT']))

"""
Personal observations : 
- Refactor the Counter version into a separate class that knows how to return the consensus string and profile matrix from a provided iterator of sequences.
- If we end up using this elsewhere, then should pull into the the utility library.
- If needed for other types of sequences (proteins, other DNA strand), then generalize to accept a different alphabet.
"""
    
assert processData('sample.txt') == """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_cons_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))