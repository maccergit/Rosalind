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

Binary search - use python library
"""

import bisect

def readlineValues(infile):
    return [x.strip() for x in infile.readline().split()]

def lookup(dataSorted, value):
    # Exit conditions
    if len(dataSorted) == 0:
        return -1
    if len(dataSorted) == 1:
        if value == dataSorted[0]:
            return 0
        else:
            return -1
    
    # Split the array into 2 arrays
    midIndex = len(dataSorted) // 2
    leftSorted = dataSorted[:midIndex]
    rightSorted = dataSorted[midIndex:]
    retval = None
    
    # Determine which subarray to search
    if value < rightSorted[0]:
        # no index adjustment needed
        retval =  lookup(leftSorted, value)
    elif value == rightSorted[0] and leftSorted[len(leftSorted) - 1] == rightSorted[0]:
        retval = lookup(leftSorted, value)
    else:
        retval = lookup(rightSorted, value)
        if not(retval < 0):
            retval += midIndex
            
    return retval

def processParsedData(dataSorted, dataUnsorted):
    return ' '.join(str(val if (val := lookup(dataSorted, x)) < 0 else val + 1) for x in dataUnsorted)

def processData(inFileName):
    with open(inFileName) as datafile:
        # With Python, we don't care about the size of the data arrays, so we just skip them
        datafile.readline()
        datafile.readline()
        dataSorted = [int(x) for x in readlineValues(datafile)]
        dataUnsorted = [int(x) for x in readlineValues(datafile)]
    return processParsedData(dataSorted, dataUnsorted)

assert lookup([], 40) == -1
assert lookup([], 10) == -1
assert lookup([], 35) == -1
assert lookup([], 15) == -1
assert lookup([], 20) == -1

assert lookup([10], 40) == -1
assert lookup([20], 40) == -1
assert lookup([30], 40) == -1
assert lookup([40], 40) == 0
assert lookup([50], 40) == -1
assert lookup([10], 10) == 0
assert lookup([10], 20) == -1
    
assert processData('sample.txt') == '4 1 -1 -1 4 2'

assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 85) == -1
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 80) == 7
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 10) == 0
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 20) == 1
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 30) == 2
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 40) == 3
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 50) == 4
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 60) == 5
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 70) == 6
assert lookup([10, 20, 30, 40, 50, 60, 70, 80, 90], 90) == 8

assert processParsedData([10, 20, 30, 40, 50, 60, 70, 80, 90], [85, 80, 10, 20, 30, 40, 50, 60, 70, 90]) == '-1 8 1 2 3 4 5 6 7 9'

with open('results_binary2.txt', 'w') as resultsfile:
    result = processData('rosalind_bins_1_dataset.txt')
    resultsfile.write(str(result))
    
# TODO - wiki space needs to note the following : data needs to be converted to ints, because sring compare of ints is incorrect (show examples).
# TODO - the 1-based indexing of Rosalind does not match the 0-based indexing of Python - easy approach is to do everything in 0-based indexing, and then
# convert to 1-based indexing once we have the results.  Problem is this is easy to forget.
# TODO - problem statement and sample data do not show any special requirements for handling duplicate data.  Binary search algorithm typically returns first found
# index that satisfies the search - NOT the smallest index that satisfies the search (this makes it a tiny bit faster).  The accepted solution only works if we
# assume it wants the smallest index that satisfies the binary search (which is what a linear search provides).
# TODO - use "bisect_left" to do the binary search using a library
# TODO - use hash lookup - does not care if indexed data is sorted, and can be used when passed unsorted data - binary search would require a sort step.
