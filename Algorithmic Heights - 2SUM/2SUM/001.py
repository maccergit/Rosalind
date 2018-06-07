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
 
Brute force - IN PROGESS
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        datafile.readline()
        data = [int(x) for x in datafile.readline().strip().split(" ")]
        total = 0
        for i in xrange(0, len(data) - 1):
            total += len([x for x in data[i + 1:] if data[i] > x])
        return str(total)

with open('sample_results.txt', 'w') as resultsfile:
    result = processData('sample.txt')
    print result
    resultsfile.write(str(result))
'''
with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_inv.txt')
    print result
    resultsfile.write(str(result))
    '''