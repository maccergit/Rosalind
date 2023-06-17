# coding: utf8
"""
Given: A positive integer k≤20, a positive integer n≤10^4, and k arrays of size n containing integers from −10^5 to 10^5.

Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.

Sample Dataset
 4 5
 2 -3 4 10 5
 8 2 4 -2 -8
 -5 2 3 2 -4
 5 4 -5 6 8

Sample Output
 -1
 2 4
 -1
 1 3
 
Brute force - works, used to verify other approaches
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        result = []
        datafile.readline()
        for line in datafile:
            data = [int(x) for x in line.strip().split(" ")]
            result1 = -1
            result2 = -1
            for index1 in range(len(data) // 2):
                for index2 in range(index1, len(data)):
                    if data[index1] == -data[index2]:
                        result1 = index1 + 1
                        result2 = index2 + 1
            if result1 == -1:
                result.append('-1')
            else:
                result.append(str(result1) + ' ' + str(result2))
        return result

assert processData('sample.txt') == ['-1', '2 4', '-1', '1 3']

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_2sum.txt')
    resultsfile.write('\n'.join(result))