# coding: utf8
"""
Insertion Sort

Given: A positive integer n≤10^3 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].

Sample Dataset
 6
 6 10 4 5 1 2

Sample Output
 12
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        # With Python, we don't care how many items there are, so we skip the first line
        datafile.readline()
        data = [int(x) for x in datafile.readline().strip().split()]
        count = 0
        for i in xrange(2, len(data) + 1):
            k = i
            while k > 1 and data[k - 1] < data[k - 2]:
                data[k - 2], data[k - 1] = data[k - 1], data[k - 2]
                count += 1
                k -= 1
        return count
    
assert processData('sample.txt') == 12

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ins.txt')
    print result
    resultsfile.write(str(result))