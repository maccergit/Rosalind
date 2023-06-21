# coding: utf8
"""
Mendel's First Law

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
 2 2 2

Sample Output
 0.78333
"""

def processData(inFileName):
    with open(inFileName) as datafile:
        (k, m, n) = [int(x) for x in datafile.readline().strip().split()]
    
    total = 0
    
    # if first parent is from 'k', then does not matter what other parent is - so figure odds of first parent being 'k'
    total += k / (k + m + n)
    
    # if first parent is not from 'k', but second parent is, then it does not matter what first parent was (just was not 'k')
    total += ((m + n) / (k + m + n)) * (k / (k + m + n - 1))
    
    # We've now removed the combinations with 'k' members, so now only need to look at combinations of "m" and "n"
    
    # Both parents are 'm' - Punnet square shows .75 chance (.25 AA, .50 Aa, and .25 aa)
    total += (m / (k + m + n)) * ((m - 1) / (k + m + n - 1)) * .75
    
    # We can ignore both parents are 'n' - they have a 0 chance.
    
    # Mix of 'm' and 'n' - Punnet square shows .5 chance (.5 Aa and .5 aa).  Do each pair separately to make sure we don't
    # include 'm' and 'm' (done above) or 'n' and 'n' (because it's 0 chance).
    
    total += (m / (k + m + n)) * (n / (k + m + n - 1)) * .5
    total += (n / (k + m + n)) * (m / (k + m + n - 1)) * .5
    
    # format to 5 decimals to match sample
    return('{:.5f}'.format(total))
    
assert processData('sample.txt') == '0.78333'

with open('results.txt', 'w') as resultsfile:
    result = processData('rosalind_iprb_1_dataset.txt')
    print(result)
    resultsfile.write(str(result))