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
        # Turn the edge list into a flat set of references vertices, then count each time each vertex appears
        data = collections.Counter(' '.join(line.strip() for line in datafile).split(' '))
        # get just the counts (degrees) in sorted order
        counts = [data[key] for key in sorted(data)]
        # add any vertices that are missing from the edge list.  Since they are not in the list, we don't know their id thus don't know their location in the sorted list,
        # so we just tack them on the end as degree 0 (no edges).
        if len(counts) < v_count:
            for x in range(len(counts), v_count):
                counts.append(0)
        # glue them together into a nice string
        return ' '.join(str(x) for x in counts)

"""
Personal observations : 
- With a simple graph that is minimal (no duplicate edges), each vertex appears once on each edge that has that vertex as an endpoint.  Thus, we only need to count the
number of times the vertex appears in the edge list to get its degree.  Since the output is positional, we need to sort by vertex ID to get the correct output.
- The special case of vertices with no edges (and thus not connected to the graph) is not mentioned in the discussion.  May not actually be a simple graph, and not be 
necessary, but included for completeness.
"""
    
assert processData('sample.txt') == '2 4 2 2 2 2'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_deg_1_dataset.txt')
    resultsfile.write(str(result))
    
print('done')