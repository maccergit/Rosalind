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
"""

import collections

def processData(inFileName):
    with open(inFileName) as datafile:
        k, n = (int(x) for x in datafile.readline().strip().split())
        results = ['-1' for x in range(0, k)]
        current = 0
        for line in datafile:
            data = collections.Counter(line.strip().split())
            for x in data:
                if data[x] > n / 2:
                    results[current] = x
            current += 1
        return " ".join(results)

"""
Personal observations : 
- brute force approach of counting all the values in the array, and then looking for the one (if any) that has a large enough count to be the majority.
"""
    
assert processData('sample.txt') == '5 7 -1 -1'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_maj.txt')
    print(result)
    resultsfile.write(str(result))