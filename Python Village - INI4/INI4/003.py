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
        a |= 1
        b -= 1 - (b % 2)
        return int((a + b) * (b - a + 2) / 4)

"""
Personal observations : 
- Use math formula of (a + b)(b - a + 2) / 4 : Note use of bitwise 'or' to ensure starting on odd value - but it's not so easy to force the last index to be odd, so use
modulo math.  No iteration.  Note need to convert to int, as result would normally be float and include ".0" and not match expected format.
"""
    
assert processData('sample.txt') == 7500

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ini4_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))