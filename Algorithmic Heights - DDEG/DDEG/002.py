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

Use utility class to read Rosalind data to networkx graph, and then use that to compute results.
"""

import graph as ut

def processData(inFileName):
    mygraph = ut.readRosalindEdgeFile(inFileName)
    return " ".join(str(sum(x[1] for x in mygraph.degree(mygraph[node]))) for node in sorted(mygraph))

assert processData('sample.txt') == '3 5 5 5 0'

with open('results1.txt', 'w') as resultsfile:
    result = processData('rosalind_ddeg_1_dataset.txt')
    resultsfile.write(str(result))
    
with open('results2.txt', 'w') as resultsfile:
    result = processData('rosalind_ddeg_2_dataset.txt')
    resultsfile.write(str(result))

print('done')