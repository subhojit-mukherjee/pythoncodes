'''
Created on May 10, 2015
https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort
@author: Chocolate
'''
from operator import itemgetter
N,M=map(int,raw_input().split());
ll=[[0 for _ in xrange(M)]for _ in xrange(N)]
for i in xrange(N):
    elm=map(int,raw_input().split());
    for j in xrange(M):
        ll[i][j]=elm[j];
#print ll;
k=input();
ll.sort(key=itemgetter(k));
print ll;
flag=ll[0][k];
print " ".join(map(str,ll[0]));
for i in xrange(1,N):
    if flag!=ll[i][k]:
        print " ".join(map(str,ll[i]));
        flag=ll[i][k];