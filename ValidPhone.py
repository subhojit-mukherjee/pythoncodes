'''
Created on May 10, 2015
https://www.hackerrank.com/contests/pythonist/challenges/regex-1-validating-the-phone-number
@author: Chocolate
'''
import re
EMAIL_REGEX = re.compile(r'^[789]{1}[0-9]{9}$');
for _ in xrange(input()):
    if EMAIL_REGEX.match(raw_input()):
        print "YES";
    else:
        print "NO";
        