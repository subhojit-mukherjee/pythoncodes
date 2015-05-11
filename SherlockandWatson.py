'''
Created on May 7, 2015
https://www.hackerrank.com/challenges/sherlock-and-watson
@author: Chocolate
'''
inp=map(int,raw_input().split());
numofelm=inp[0];
rot=inp[1];
qur=inp[2];
arr=map(int,raw_input().split());
arr1=[0]*numofelm;
for i in xrange(0,numofelm):
    arr1[(i+rot)%numofelm]=arr[i];
for _ in xrange(qur):
    print(arr1[input()]);