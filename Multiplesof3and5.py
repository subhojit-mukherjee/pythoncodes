'''
Created on May 6, 2015
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
@author: Chocolate

'''
def sum1(n,d):
    m = int(n/d);
    return (d*m*(m+1)/2);
for _ in xrange(input()):
    n=input();
    print(sum1(n-1,3)+sum1(n-1,5)-sum1(n-1,15));
'''
def check15(num):
    if num%15==0:
        return 1;
    else:
        return 0;


for _ in xrange(input()):
    n=input();
    a=3;
    b=5;
    i=a;
    j=b;
    sum1=0;
    count=2;
    var=1;
    if n<3:
        print(0);
        continue;
    while var==1:
        if (i>=n) and (j>=n):
            break;
        if(i<n):
            sum1+=i;
            i=a*count;
        if(j<n):
            sum1+=j;
            j=b*count;
        count+=1;
    a=15;
    i=a;
    count=2;
    while var==1:
        if i>=n:
            break;
        sum1=sum1-i;
        i=a*count;
        count+=1;
    print(sum1);
'''
'''def checkDiv(num):
    if (num%3==0) or (num%5==0):
        return 1;
    else:
        return 0;


for _ in xrange(input()):
    n=input();
    sum1=0;
    for i in xrange(3,n,1):
        if(checkDiv(i)==1):
            sum1+=i;
    print(sum1);
   '''     
        
        