'''
Created on May 7, 2015

@author: Chocolate
'''
'''
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n;
    cin >> n;
    
    unsigned short* a = new unsigned short[n];
    for(int i = 0;i < n;i++)
        cin >> a[i];
    
    int partial[65536];
    fill(partial, partial + 65536, 0);
    
    int xsum = 0;
    partial[xsum]++;
    for(int i = 0;i < n;i++) {
        xsum ^= a[i];
        partial[xsum]++;
    }
    
    int count[65536];
    fill(count, count + 65536, 0);
    
    for(int i = 0;i < 65536;i++)
        for(int j = 0;j < i;j++)
            count[i ^ j] += partial[i] * partial[j];
    
    int max = 0;
    for(int i = 0;i < 65536;i++) 
        if(count[i] > count[max])
            max = i;
    
    cout << max << ' ' << count[max] << endl;
    
    delete[] a;
    
    return 0;
}

'''
ll=[];
n=input();
for _ in xrange(n):
    ll.append(input());
partial=[0]*n;
xsum=0;
partial[xsum]+=1;
for i in xrange(0,n):
    xsum^=ll[i];
    partial[xsum]+=1;
count1=[0]*n;
for i in xrange(0,n):
    for j in xrange(0,i):
        count1[i^j]+=partial[i] * partial[j];
max1=0;
for i in xrange(0,n):
    if count1[i] > count1[max1]:
        max1 = i;
print(str(max1)+" "+str(count1[max1]));
    

