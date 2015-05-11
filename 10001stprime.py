'''
Created on May 8, 2015

@author: Chocolate
'''
def SieveofEras(arr):
    arr[0]=True;
    arr[1]=True;
    for i in xrange(1,len(arr)):
        if arr[i]==False:
            for j in xrange(i*2,len(arr),i):
                arr[j]=True;
    return arr;

ll=[False]*10002
ll=SieveofEras(ll);
for _ in xrange(input()):
    n=input();
    idx=2;
    while idx<len(ll):
        #print idx;
        if(n==0):
            break;
        if(ll[idx]==False):
            n-=1;
        idx+=1;
    print(idx-1);
