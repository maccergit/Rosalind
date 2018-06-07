# coding: utf8
"""
Degree Array 

Given: A simple graph with n≤10^3 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the degree of vertex i.

Sample Dataset
 6 7
 1 2
 2 3
 6 3
 5 6
 2 5
 2 4
 4 1

Sample Output
 2 4 2 2 2 2
"""

import collections

def processData(inFileName):
    with open(inFileName) as datafile:
        # First line is number of vertices and edges - may not be obvious that we need this, but it's
        # how we know about any stand-alone nodes.  Without edges, they aren't in the edge list.
        v_count = [int(x.strip()) for x in datafile.readline().split()][0]
        data = collections.Counter(' '.join(line.strip() for line in datafile).split(' '))
        counts = [data[key] for key in sorted(data)]
        if len(counts) < v_count:
            for x in xrange(len(counts), v_count):
                counts.append(0)
        return ' '.join(str(x) for x in counts)
    
assert processData('sample.txt') == '2 4 2 2 2 2'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_deg_1_dataset.txt')
    resultsfile.write(str(result))
    
print 'done'