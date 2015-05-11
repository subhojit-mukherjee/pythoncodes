'''
Created on May 7, 2015
https://www.hackerrank.com/contests/projecteuler/challenges/euler004
@author: Chocolate
'''
def binSearch(arr,elm):
    lo=0;
    hi=len(arr)-1;
    #print hi;
    while(lo<=hi):
        mid=lo+((hi-lo)/2);
        #print mid
        if(arr[mid]==elm):
            return mid;
        elif(arr[mid]>elm):
            hi=mid-1;
        else:
            lo=mid+1;
        #print lo
    return hi;
ll=[];
for i in range(100,1000):
    for j in range(100,1000):
        mulnum=i*j;
        mulnums=str(mulnum);
        if(mulnums==mulnums[::-1]):
            ll.append(mulnum);
ll=sorted(ll);            
#print ll;
for _ in xrange(input()):
    n=input();
    print(ll[binSearch(ll, n)]);
    

    