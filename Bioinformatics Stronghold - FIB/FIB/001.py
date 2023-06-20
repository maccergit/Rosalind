# coding: utf8
"""
Rabbits and Recurrence Relations

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation,
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset
 5 3

Sample Output
 19
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        (n, k) = (int(x) for x in datafile.readline().strip().split())
    p1, p2 = 1, 1
    for i in range(2, n):
        p1, p2 = p2, p1 * k + p2
    return p2
    
assert processData('sample.txt') == 19

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_fib_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))