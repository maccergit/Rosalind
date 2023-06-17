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

Use the networkx library to handle graph stuff.
"""

import networkx as nx


def processData(inFileName):
    with open(inFileName) as datafile:
        # First line is number of vertices and edges - may not be obvious that we need this, but it's
        # how we know about any stand-alone nodes.  Without edges, they aren't in the edge list.
        v_count = [int(x.strip()) for x in datafile.readline().split()][0]
        mygraph = nx.read_edgelist(datafile)
    if v_count > len(mygraph):
        for x in range(len(mygraph), v_count):
            mygraph.add_node(str(x + 1))
    return " ".join(str(x[1]) for x in sorted(list(mygraph.degree())))

"""
Personal observations : 
- networkx is probably overkill for this project, but is probably useful for more complex graph problems.  Most of the code is building the graph structure in memory - the
actual computing of the degree list is a single call into the library.
- Rosalind edge list file format differs slightly from networkx edge list file format - networkx does not support the first line with vertex count and edge count.  By
reading the first line ourselves, we leave the file position in the correct place for networkx to read the rest of the file, and can then adjust the resulting graph to
take into account any lone vertices.
"""
    
assert processData('sample.txt') == '2 4 2 2 2 2'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_deg_1_dataset.txt')
    resultsfile.write(str(result))
    
print('done')