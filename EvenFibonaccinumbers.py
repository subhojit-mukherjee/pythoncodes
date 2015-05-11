'''
Created on May 6, 2015

@author: Chocolate
'''
import abc
'''

When taking the following rules into account:

    even + even = even

    even + odd = odd

    odd + even = odd

    odd + odd = even

The parity of the first Fibonacci numbers is:

    o o e o o e o o e ...

Thus basically, you simply need to do steps of three. Which is:

(1,1,2)
(3,5,8)
(13,21,34)

Given (a,b,c) this is (b+c,b+2*c,2*b+3*c).

This means we only need to store the two last numbers, and calculate given (a,b), (a+2*b,2*a+3*b).

Thus (1,2) -> (5,8) -> (21,34) -> ... and always return the last one.

This will work faster than a "filter"-approach because that uses the if-statement which reduces pipelining.

def checkTheMultiple(arr, num, n):
 # print("In checker");
 i = 2;
 a = num * i;
 while a <= n:
  # print(a);
  arr[a - 1] = 1;
  # print(arr);
  i = i + 1;
  a = num * i;
  
  
def checkPrime(n):
    resultlist=[];
    if n >= 2:
        llist = [0] * n;
        for j in xrange(1, n, 1):
            if llist[j] == 0:
                checkTheMultiple(llist, j + 1, n);
    # print("Back");
    # print(llist);
                resultlist.extend([j+1]);
        return resultlist;
'''    
def fibo(n):
    a=[0]*(n+1);
    a[0]=1;
    a[1]=2;
    for i in xrange(2,n+1,2):
        a[i]=a[i-2]+(a[i-1]*2);
        a[i+1]=(2*a[i-2])+(a[i-1]*3);
        if a[i+1]>=n:
            break;
    return a;
for _ in xrange(input()):
    N=input();
    abc=[x for x in fibo(N) if x % 2 == 0];
    #print fibo(N);
    bca=[x for x in abc if x<N];
    #print abc;
    print(sum(bca));


