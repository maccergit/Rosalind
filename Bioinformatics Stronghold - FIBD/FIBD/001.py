# coding: utf8
"""
Mortal Fibonacci Rabbits

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
 6 3

Sample Output
 4
"""

def processData(inFileName):
    # extract arguments
    with open(inFileName) as datafile:
        (n, m) = (int(x) for x in datafile.readline().strip().split())
    # intialize number of rabbits for each month
    rabbitMonths = [0] * (m - 2) + [1, 1, 1]
    # iterate over the remaining months
    for i in range(n - 2):
        rabbitMonths = rabbitMonths[1:] + [rabbitMonths[-1] + rabbitMonths[-2] - rabbitMonths[0]]
    return rabbitMonths[-1]

assert processData('sample.txt') == 4

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_fibd_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))