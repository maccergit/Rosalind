# coding: utf8
"""
Merge Two Sorted Arrays

An array A[1..n] is said to have a majority element if more than half of its entries are the same.

Given: A positive integer n≤10^5 and a sorted array A[1..n] of integers from −10^5 to 10^5, a positive integer m≤10^5 and a sorted array B[1..m] of integers from −10^5 to 10^5.

Return: A sorted array C[1..n+m] containing all the elements of A and B.

Sample Dataset
 4
 2 4 10 18
 3
 -5 11 12

Sample Output
 -5 2 4 10 11 12 18
 
 Use heapq library to merge sorted iterables
"""

import heapq

def processData(inFileName):
    with open(inFileName) as datafile:
        datafile.readline()
        A = [int(x) for x in datafile.readline().strip().split(" ")]
        datafile.readline()
        B = [int(x) for x in datafile.readline().strip().split(" ")]
    return " ".join(str(x) for x in heapq.merge(A, B))
    
assert processData('sample.txt') == '-5 2 4 10 11 12 18'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_mer.txt')
    resultsfile.write(str(result))

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_mer_1_dataset.txt')
    resultsfile.write(str(result))

print('done')