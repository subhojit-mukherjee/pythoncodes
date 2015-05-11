'''
Created on May 6, 2015
https://www.hackerrank.com/contests/projecteuler/challenges/euler072
@author: Chocolate
'''

def P(L):
    phi = range(L+1)
    for n in xrange(2, L+1):
        if phi[n] == n:
            for k in xrange(n, L+1, n):
                phi[k] -= phi[k] // n
    return sum(phi) - 1

for _ in xrange(input()):
    n=input();
    print(P(n));