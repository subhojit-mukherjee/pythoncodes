'''
Created on May 7, 2015

@author: Chocolate
'''
def RangeLCM(first, last):
    factors = range(first, last+1)
    for i in range(0, len(factors)):
        if factors[i] != 1:
            n = first + i
            for j in range(2*n, last+1, n):
                factors[j-first] = factors[j-first] / factors[i]
    return reduce(lambda a,b: a*b, factors, 1)