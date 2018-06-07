# coding: utf8
"""
Counting Inversions

An inversion of an array A[1..n] is a pair of indices (i,j) such that 1≤i<j≤n and A[i]>A[j]. The number of inversions shows how far the array is from being sorted:
if it is already sorted then there are no inversions, whereas if it is sorted in reverse order then the number of inversions is maximal.

Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.

Return: The number of inversions in A.

Sample Dataset
 5
 -6 1 15 8 10

Sample Output
 2
 
 Brute force - very slow!
 
 TODO - modified merge sort
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        datafile.readline()
        data = [int(x) for x in datafile.readline().strip().split(" ")]
        total = 0
        for i in xrange(0, len(data) - 1):
            total += len([x for x in data[i + 1:] if data[i] > x])
        return str(total)
    
assert processData('sample.txt') == '2'
assert processData('sample2.txt') == '8'
assert processData('sample4.txt') == '3'
assert processData('sample5.txt') == '5'
assert processData('sample3.txt') == '159'
assert processData('sample6.txt') == '216'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_inv.txt')
    print result
    resultsfile.write(str(result))