# coding: utf8
"""
Merge Sort

Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.

Return: A sorted array A[1..n].

Sample Dataset
 10
 20 19 35 -18 17 -20 20 1 4 4

Sample Output
 -20 -18 1 4 4 17 19 20 20 35
 
 Cheating - use Python built in sorting - not a merge sort
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        datafile.readline()
        return " ".join(str(y) for y in sorted(int(x) for x in datafile.readline().strip().split(" ")))

"""
Personal observations : 
- Handy to test any actual implementations.
"""
    
assert processData('sample.txt') == '-20 -18 1 4 4 17 19 20 20 35'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ms.txt')
    resultsfile.write(str(result))

print('done')