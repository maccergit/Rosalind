# coding: utf8
"""
Binary Search

Given: Two positive integers n≤10^5 and m≤10^5, a sorted array A[1..n] of integers from −10^5 to 10^5 and a list of m integers −10^5≤k1,k2,…,km≤10^5.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

Sample Dataset
 5
 6
 10 20 30 40 50
 40 10 35 15 40 20

Sample Output
 4 1 -1 -1 4 2

Use Python's binary search

TODO - this appears to be broken, as it does not match the results of the linear search
"""

import bisect

def readlineValues(infile):
    return [x.strip() for x in infile.readline().split()]

def lookup(dataSorted, value):
    i = bisect.bisect_left(dataSorted, value)
    if i != len(dataSorted) and dataSorted[i] == value:
        return i + 1
    return -1

def processData(inFileName):
    with open(inFileName) as datafile:
        # With Python, we don't care about the size of the data arrays, so we just skip them
        datafile.readline()
        datafile.readline()
        dataSorted = readlineValues(datafile)
        dataUnsorted = readlineValues(datafile)
        return ' '.join(str(lookup(dataSorted, x)) for x in dataUnsorted)
    
print(processData('sample.txt'))
assert processData('sample.txt') == '4 1 -1 -1 4 2'

with open('results_bin2.txt', 'w') as resultsfile:
    result = processData('rosalind_bins_1_dataset.txt')
    resultsfile.write(str(result))

print('done')