#!/usr/bin/env python
# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
import sys,os,time

num=int(raw_input("Pick a number: "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print "The list provided is: ",a
print "We will print the entries less than: ",num

for index, item in enumerate(a):
  if ( item < num ):
    b.append(item)
print "The NEW list provided is: ",b

sys.exit(0)
