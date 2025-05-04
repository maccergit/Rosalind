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

import math

def fibb(n):
    root5 = math.sqrt(5)
    return int(((1 + root5) ** n - (1 - root5) ** n) / (root5 * (2 ** n)))

"""
Personal observations : 
- Uses Binet's formula, instead of iteration, so is O(c)
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        return fibb(int(datafile.readline().strip()))
    
assert processData('sample.txt') == 8

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_fibo_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))

# TODO - when adding wiki page, include link to Fibonacci in Euler wiki page.