'''
Created on May 10, 2015

@author: Chocolate

'''
import re
EMAIL_REGEX = re.compile(r"^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[^@]{3}$");
ll=[];
for _ in xrange(input()):
    strinp=raw_input();
    if EMAIL_REGEX.match(strinp):
        ll.append(strinp);
print sorted(ll);
        
