# coding: utf8
"""
Finding a Protein Motif

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID
followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
 A2Z669
 B5ZC00
 P07204_TRBM_HUMAN
 P20840_SAG1_YEAST

Sample Output
 B5ZC00
 85 118 142 306 395
 P07204_TRBM_HUMAN
 47 115 116 382 409
 P20840_SAG1_YEAST
 79 109 135 248 306 348 364 402 485 501 614
"""

import urllib.request
from io import StringIO
from Bio import SeqIO

motif = 'N{P}[ST]{P}'

def matchMotif(seq):
    if len(seq) < 4:
        return False
    if seq[0] == 'N':
        if seq[1] != 'P':
            if seq[2] in ['S', 'T']:
                if seq[3] != 'P':
                    return True
    return False

def getUniprotRecords(uniprotID):
    with urllib.request.urlopen('http://www.uniprot.org/uniprot/' + uniprotID + '.fasta') as response:
        return(SeqIO.parse(StringIO(str(response.read(), 'utf-8')), 'fasta'))

def processData(inFileName):
    # Get the FASTA records from UniProt
    fastaRecords = []
    uniprotIDs = []
    with open(inFileName) as datafile:
        for uniprotID in (x.strip() for x in datafile):
            # Some of the IDs are not just access IDs - but we need only that portion for the call.  We also need the original for display.
            if '_' in uniprotID:
                accessID = uniprotID[:uniprotID.index('_')]
            else:
                accessID = uniprotID
            uniprotIDs.append(uniprotID)
            for record in getUniprotRecords(accessID):
                fastaRecords.append(record)
    
    result = ''
    # Step through the sequences
    for i in range(len(fastaRecords)):
        # Find the matching locations for the motif in the current sequence, and save them in a list
        matches = []
        seq = fastaRecords[i].seq
        for j in range(len(seq)):
            if matchMotif(seq[j:]):
                matches.append(str(j + 1))
        # We found all the matches, now add them to the results (but only if matches were found).
        if len(matches) > 0:
            result += uniprotIDs[i] + '\n' + ' '.join(matches) + '\n'
    if len(result) > 0:
        result = result[:-1]
    return(result)

"""
Personal observations : 
- The notes about the access IDs were not very clear - a little trial and error by hand on the site showed that only the initial portion appears to work.
- Not the best approach - but good enough.  The logic to test for the motif is not general, and should be handled by a motif->regex translator to handle any sort of motif.
- This problem felt like it had a lot of requirements and could have been broken into smaller problems.
"""
    
assert processData('sample.txt') == '''B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614'''

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_mprt.txt')
    print(result)
    resultsfile.write(str(result))