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

"""
Personal observations : 
- Getting PyDev to handle imports from other projects in the same workspace is a bit of a pain, but can be done.  To get the utility to load using the fully qualified
name, had to add the the project folder as an external source library, and not as a project reference (project reference works - but then it acts like the module is in the
current directory, and only the short name and not the fully qualified name works - this pollutes the global namespace).  Even with AI assistance, this took some trial and
error.
- The previous version that converted Rosalind formatted data was complex enough to warrant separation into a utility module, making this version much cleaner.
"""
    
assert processData('sample.txt') == '2 4 2 2 2 2'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_deg_1_dataset.txt')
    resultsfile.write(str(result))
    
print('done')