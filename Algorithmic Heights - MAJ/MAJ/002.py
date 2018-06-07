# coding: utf8
"""
Majority Element

An array A[1..n] is said to have a majority element if more than half of its entries are the same.

Given: A positive integer k≤20, a positive integer n≤10^4, and k arrays of size n containing positive integers not exceeding 10^5.

Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise.

Sample Dataset
 4 8
 5 5 5 5 5 5 5 5
 8 7 7 7 1 7 3 7
 7 1 6 5 10 100 1000 1
 5 1 6 7 1 1 10 1

Sample Output
 5 7 -1 -1
 
 Use ability of Counter to keep track of most common element
"""

import collections

def processData(inFileName):
    with open(inFileName) as datafile:
        n = [int(x) for x in datafile.readline().strip().split()][1]
        results = []
        for line in datafile:
            value, count = collections.Counter(line.strip().split()).most_common(1)[0]
            results.append(str(value) if count > n / 2 else '-1')
        return " ".join(results)
    
assert processData('sample.txt') == '5 7 -1 -1'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_maj.txt')
    print result
    resultsfile.write(str(result))