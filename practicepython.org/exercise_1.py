#!/usr/bin/env python
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import os,sys, time

name=raw_input("What is your name: ")
age=int(raw_input("What is your age: "))
numrepeats=int(raw_input("How many times would you like to see this output: "))

# getting the current year
thisyear=int(time.strftime("%Y"))

#math portion
yearsuntilcenturian = 100 - age
turncenturian = thisyear + yearsuntilcenturian

while (numrepeats > 0):
  print name," You will turn 100 years old in the year ",turncenturian
  numrepeats = numrepeats - 1

sys.exit(0)
