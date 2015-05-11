'''
Created on May 10, 2015

@authorr: Chocolate
'''
from math import sqrt;
class MyClass(object):
    def __init__(self, real=0.0,imag=0.0):
        self.real=real;
        self.imag=imag;
    def __add__(self, x):
        r=self.real+x.real;
        i=self.imag+x.imag;
        return MyClass(r,i);
    def __sub__(self, x):
        r=self.real-x.real;
        i=self.imag-x.imag;
        return MyClass(r,i);
    def __mul__(self, x):
        r=(self.real*x.real)-(self.imag*x.imag);
        i=(self.real*x.imag)+(self.imag*x.real);
        return MyClass(r,i);
    def __div__(self, x):
        '''
        float div=(x.real*x.real) + (x.imag*x.imag);
               complex tmp;
               tmp.real=(real*c.real)+(imag*c.imag);
               tmp.real/=div;
               tmp.imag=(imag*c.real)-(real*c.imag);
               tmp.imag/=div;
               return tmp;
        '''
        d=(x.real*x.real) + (x.imag*x.imag);
        r=(self.real*x.real)+(self.imag*x.imag);
        r=r/d;
        i=(self.imag*x.real)-(self.real*x.imag);
        i=i/d;
        return MyClass(r,i);
    def modu(self):
        z=(self.real*self.real)+(self.imag*self.imag);
        return sqrt(z);
    def __str__(self):
        if(self.imag<0):
            #print "%.2f %.2f" % (self.real, self.imag),"i"
            return str("%.2f - %.2fi" % (self.real, abs(self.imag)))
        
        #print "%.2f + %.2f" % (self.real, self.imag),"i"
        return str("%.2f + %.2fi" % (self.real, self.imag))

n1,n2=map(float,raw_input().split());
n3,n4=map(float,raw_input().split());
a=MyClass(n1+0.0,n2+0.0);
b=MyClass(n3+0.0,n4+0.0);
print(a+b);
print(a-b);
print(a*b);
print(a/b);
print(round(a.modu(),2));
print(round(b.modu(),2));
#print a+b;
