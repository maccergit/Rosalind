# coding: utf8
"""
Variables and Some Arithmetic

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

Sample Dataset
 3 5

Sample Output
 34
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        return sum(int(x.strip()) ** 2 for x in datafile.readline().split(" "))
    
assert processData('sample.txt') == 34

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ini2_1_dataset.txt')
    print result
    resultsfile.write(str(result))