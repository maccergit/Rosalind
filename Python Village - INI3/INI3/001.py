# coding: utf8
"""
Strings and lists

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

Sample Dataset
 HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
 22 27 97 102

Sample Output
 Humpty Dumpty
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        text = datafile.readline()
        indices = [int(x.strip()) for x in datafile.readline().split(" ")]
        return text[indices[0]:indices[1] + 1] + ' ' + text[indices[2]:indices[3] + 1]
    
assert processData('sample.txt') == 'Humpty Dumpty'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_ini3_1_dataset.txt')
    print result
    resultsfile.write(str(result))