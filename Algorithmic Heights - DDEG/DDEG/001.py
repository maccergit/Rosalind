# coding: utf8
"""
Double-Degree Array

Given: A simple graph with n≤10^3 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.

Sample Dataset
 5 4
 1 2
 2 3
 4 3
 2 4

Sample Output
 3 5 5 5 0

Roll our own adjacency set approach.
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        # first line has vertices and adges counts
        v_count = int(datafile.readline().strip().split(" ")[0])
        # build empty adjacency set for each node
        adj_set = {node: {'dd': 0, 'degree': 0, 'adj': set()} for node in (str(x) for x in range(1, v_count + 1))}
        # populate the adjacency set from the datafile
        for line in datafile:
            v1, v2 = line.strip().split(" ")
            adj_set[v1]['adj'].add(v2)
            adj_set[v2]['adj'].add(v1)
        # compute 1st level degree for each node
        for key in adj_set:
            adj_set[key]['degree'] = len(adj_set[key]['adj'])
        # compute 2nd level degree for each node
        for key in adj_set:
            adj_set[key]['dd'] = sum(adj_set[x]['degree'] for x in adj_set[key]['adj'])
        return " ".join(str(adj_set[x]['dd']) for x in sorted(adj_set))
    
assert processData('sample.txt') == '3 5 5 5 0'

with open('results1.txt', 'w') as resultsfile:
    result = processData('rosalind_ddeg_1_dataset.txt')
    resultsfile.write(str(result))
    
with open('results2.txt', 'w') as resultsfile:
    result = processData('rosalind_ddeg_2_dataset.txt')
    resultsfile.write(str(result))
    
print('done')