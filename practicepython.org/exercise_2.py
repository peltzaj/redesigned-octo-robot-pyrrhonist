#!/usr/bin/env python
# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
import sys, os, time

num = int(raw_input("Please pick a number, any number: "))
divisor = int(raw_input("Pick a second number: "))

if ( ( num % 2 ) == 0 ):
  print "The number: ",num," is even."
  if ( (num % 4 ) == 0 ):
    print "The number: ",num," is divisable by four."
else:
  print "The number: ",num," is odd."

if ( ( num % divisor ) == 0 ):
  print "The number: ",num," is divisable by: ",divisor

sys.exit(0)
