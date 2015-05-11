'''
Created on May 10, 2015
https://www.hackerrank.com/contests/pythonist/challenges/python-string-formatting
@author: Chocolate
'''
n1=int(raw_input());
j = len(str(bin(n1)[2:]));
for i in xrange(1, n1 + 1):
    print '%*s %*s %*s %*s' % (j, i, j, format(i, 'o'), j, str(format(i, 'x')).upper(), j, bin(i)[2:])
