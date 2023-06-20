# coding: utf8
"""
Conditions and Loops

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset
 100 200

Sample Output
 7500
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        a, b = [int(x.strip()) for x in datafile.readline().split(" ")]
    return sum(range(a | 1, b + 1, 2))

"""
Personal observations : 
- Similar to first solution, but skips over even values.  Note use of bitwise 'or' to ensure starting on odd value.  Since only odd values are generated, no need to filter
out even values, so no need for list comprehension that uses modulo operator.
"""
    
assert processData('sample.txt') == 7500

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ini4_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))