'''
Created on May 7, 2015
https://www.hackerrank.com/contests/projecteuler/challenges/euler003
@author: Chocolate
'''
def prime(n):
    i = 2
    #print n;
    while (n % i != 0 and i*i< n):
        i += 1
        #print "In While",i
    if (i*i < n):
        #print "In if",i;
        return prime (n / i)
    else:
        print n

for _ in xrange(input()):
    n = input()
    prime(n)
