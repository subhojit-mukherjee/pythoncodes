'''
Created on May 6, 2015
int target = 200;
int[] coinSizes = { 1, 2, 5, 10, 20, 50, 100, 200 };
int[] ways = new int[target+1];
ways[0] = 1;
 
for (int i = 0; i < coinSizes.Length; i++) {
    for (int j = coinSizes[i]; j <= target; j++) {
        ways[j] += ways[j - coinSizes[i]];
    }
}
https://www.hackerrank.com/contests/projecteuler/challenges/euler031
http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
@author: Chocolate
'''
for _ in xrange(input()):
    n=input();
    coinSizes=[ 1, 2, 5, 10, 20, 50, 100, 200 ];
    ways=[0]*(n+1);
    ways[0]=1;
    for i in coinSizes:
        j=i;
        while j<=n:
            ways[j]+=ways[j - i];
            j+=1;
            
    print(ways[n]%(10**9+7));        
    