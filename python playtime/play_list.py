#!/usr/bin/env python


import os, sys

def main():
  L = [ 1, 6, 19, 37, 2, 3, 5, 42, 20, 41, 40, 15, 34, 28, 176, -11]
  L.sort()
  print "original list is: ",L
  T = []
  holder = ""
  inside = False
  for index, item in enumerate(L):
    #print index, item
    if index == len(L)-1 :
        holder = holder + str(item)
        inside = False
        T.append( holder)
        holder = ""
        #print "last object! holder is (",holder,") inside is false and T is: ",T
        continue
    if L[index]+1 == L[index+1]:
      if inside:
        #print "inside grouping with L[index] and holder is (",holder,")"
        continue
      else:
        holder = str(item) + "-"
        inside = True
        #print "holder contains (",holder,") and inside is true"
    else:
      holder = holder + str(item)
      inside = False
      T.append( holder )
      holder = ""
      #print "holder is (",holder,") inside is false and T is: ",T
  print "the new list from the list is: ",T

  sys.exit(0)


if __name__ == "__main__":
  main()
