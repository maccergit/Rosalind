# coding: utf8
"""
Given: A positive integer k≤20, a positive integer n≤10^4, and k arrays of size n containing integers from −10^5 to 10^5.

Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.

Sample Dataset
 4 5
 2 -3 4 10 5
 8 2 4 -2 -8
 -5 2 3 2 -4
 5 4 -5 6 8

Sample Output
 -1
 2 4
 -1
 1 3
 
use itertools to generate permutations
TODO : in progress
"""

import itertools as tools

def processData(inFileName):
    with open(inFileName) as datafile:
        result = []
        datafile.readline()
        for line in datafile:
            data = [int(x) for x in line.strip().split(" ")]
            indexes = [(i1, i2) for (i1, i2) in tools.permutations(range(len(data)), 2) if i1 < i2]
            sums = [data[i1] + data[i2] for (i1, i2) in indexes]
            if 0 in sums:
                i = sums.index(0)
                result.append(" ".join(str(x + 1) for x in indexes[i]))
            else:
                result.append('-1')
        print(result)
        return result

assert processData('sample.txt') == ['-1', '2 4', '-1', '1 3']

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_2sum.txt')
    resultsfile.write('\n'.join(result))