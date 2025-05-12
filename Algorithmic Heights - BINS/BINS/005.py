# coding: utf8
"""
Binary Search

Given: Two positive integers n≤10^5 and m≤10^5, a sorted array A[1..n] of integers from −10^5 to 10^5 and a list of m integers −10^5≤k1,k2,…,km≤10^5.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

Sample Dataset
 5
 6
 10 20 30 40 50
 40 10 35 15 40 20

Sample Output
 4 1 -1 -1 4 2

Dictionary search
"""

def readlineValues(infile):
    return [x.strip() for x in infile.readline().split()]

def lookup(dataDict, value):
    try:
        retval = dataDict[value]
    except KeyError:
        retval = -1
    return retval

def processParsedData(dataDict, dataUnsorted):
    return ' '.join(str(lookup(dataDict, x)) for x in dataUnsorted)

def processData(inFileName):
    with open(inFileName) as datafile:
        # With Python, we don't care about the size of the data arrays, so we just skip them
        datafile.readline()
        datafile.readline()
        dataSorted = [int(x) for x in readlineValues(datafile)]
        dataUnsorted = [int(x) for x in readlineValues(datafile)]
    index = 1
    dataDict = {}
    for key in dataSorted:
        if key not in dataDict:
            dataDict[key] = index
        index += 1
    return processParsedData(dataDict, dataUnsorted)

assert lookup({}, 40) == -1
assert lookup({}, 10) == -1
assert lookup({}, 35) == -1
assert lookup({}, 15) == -1
assert lookup({}, 20) == -1

assert lookup({10 : 1}, 40) == -1
assert lookup({20 : 1}, 40) == -1
assert lookup({30 : 1}, 40) == -1
assert lookup({40 : 1}, 40) == 1
assert lookup({50 : 1}, 40) == -1
assert lookup({10 : 1}, 10) == 1
assert lookup({10 : 1}, 20) == -1

assert processData('sample.txt') == '4 1 -1 -1 4 2'

assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 85) == -1
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 80) == 8
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 10) == 1
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 20) == 2
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 30) == 3
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 40) == 4
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 50) == 5
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 60) == 6
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 70) == 7
assert lookup({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, 90) == 9

assert processParsedData({10 : 1, 20 : 2, 30 : 3, 40 : 4, 50 : 5, 60 : 6, 70 : 7, 80 : 8, 90 : 9}, [85, 80, 10, 20, 30, 40, 50, 60, 70, 90]) == '-1 8 1 2 3 4 5 6 7 9'

with open('results_hash.txt', 'w') as resultsfile:
    result = processData('rosalind_bins_1_dataset.txt')
    resultsfile.write(str(result))

