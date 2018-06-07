# coding: utf8
"""
Fibonacci numbers

Given: A positive integer n≤25.

Return: The value of Fn.

Sample Dataset
 6

Sample Output
 8
"""

def fibb(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    current = 1
    while current < n:
        n1, n2 = n2, n1 + n2
        current += 1
    return n2

def processData(inFileName):
    with open(inFileName) as datafile:
        return fibb(int(datafile.readline().strip()))
    
assert processData('sample.txt') == 8

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_fibo_1_dataset.txt')
    print result
    resultsfile.write(str(result))