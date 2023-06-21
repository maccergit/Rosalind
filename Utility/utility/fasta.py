# coding: utf8
"""
Utilities that support reading FASTA formatted files.
"""

def processLines(lines):
    """
    Convert iterable containing FASTA formatted lines to a dictionary.
    
    Used to decouple I/O from actual processing to facilitate unit testing.
    """
    retval = {}
    key = ''
    data = ''
    
    # Iterate ove the lines, looking for '>' to indicate the start of a new block of data.
    # We accumulate the data as we iterate over the block, until we hit the next block.
    # We then store the accumulated data to the dictionary, and start accumulating data
    # from the next block.  Of course, we have not accumulated data from a previous block
    # when we hit the first header, and we need to store the data for the last block
    # after we are done with all of the blocks.
    for line in (x.strip() for x in lines):
        if line[0] == '>':
            if key != '':
                retval[key] = data
            data = ''
            key = line[1:]
        else:
            data += line
    if key != '':
        retval[key] = data
    return retval

def readFastaFile(inFileName):
    """
    Read a FASTA formatted file and return a dictionary with header lines as keys, and sequences as values.
    """
    with open(inFileName) as datafile:
        return processLines(datafile.readlines())