# coding: utf8
"""
Merge Sort

Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.

Return: A sorted array A[1..n].

Sample Dataset
 10
 20 19 35 -18 17 -20 20 1 4 4

Sample Output
 -20 -18 1 4 4 17 19 20 20 35
 
 Implement a true recursive merge sort, using the merge list code from MER.
"""

def merge(A, B):
    C = []
    while len(A) + len(B) > 0:
        if len(B) == 0:
            C.append(A.pop(0))
        else:
            if len(A) == 0:
                C.append(B.pop(0))
            else:
                if A[0] < B[0]:
                    C.append(A.pop(0))
                else:
                    C.append(B.pop(0))
    return C

def sort(data):
    if len(data) == 1:
        return data
    return merge(sort(data[:len(data) / 2]), sort(data[len(data) / 2:]))
    
def processData(inFileName):
    with open(inFileName) as datafile:
        datafile.readline()
        return " ".join(str(y) for y in sort([int(x) for x in datafile.readline().strip().split(" ")]))
    
assert processData('sample.txt') == '-20 -18 1 4 4 17 19 20 20 35'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ms.txt')
    resultsfile.write(str(result))

print 'done'