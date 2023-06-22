# coding: utf8
"""
Calculating Expected Offspring

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population
possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
 1 0 0 1 0 1

Sample Output
 3.5
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        (a, b, c, d, e, f) = datafile.readline().strip().split()
    # combinations 'a', 'b', and 'c' have 100% chance of A phenotype
    # combination 'd' has 75% chance of A phenotype (from Punnet square)
    # combination 'e' has 50% chance of A phenotype (from Punnet square)
    # combination 'f' has 0% chance of A phenotype
    
    # Each combination has 2 children - so multiply each chanve by 2, and multiply result by associated population :
    # result - 2 * 1 * a + 2 * 1 * b + 2 * 1 * c + 2 * .75 * d + 2 * .5 * e + 2 * 0 * f
    # simplifies to...
    
    result = 2 * (int(a) + int(b) + int(c)) + 1.5 * int(d) + int(e)
    
    return(str(result))
    
assert processData('sample.txt') == '3.5'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_iev_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))