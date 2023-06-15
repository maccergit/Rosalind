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

Use the utility class to handle Rosalind formatted data.
"""

import utility.graph as ut

def processData(inFileName):
    mygraph = ut.readRosalindEdgeFile(inFileName)
    return " ".join(str(x[1]) for x in sorted(list(mygraph.degree())))
    
assert processData('sample.txt') == '2 4 2 2 2 2'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_deg_1_dataset.txt')
    resultsfile.write(str(result))
    
print('done')