#!/usr/bin/env python

import sys,os,argparse

def main():
  it = get_args()
  try:
    file = open(it.thefile,'r')
  except:
    print "cant open file: ",it.thefile,"."
    
  print "we will replace ",it.searcher," with ",it.replacer, \
          " in the file ",it.thefile," and output that to the screen"
  for lines in file:
      print lines.replace(it.searcher,it.replacer).rstrip()

  file.close()
  sys.exit(0)

def get_args():
  parser = argparse.ArgumentParser(description="This will read in a file and replace a word with another")
  parser.add_argument("-f","--file",dest="thefile",
                        default="/Users/peltzaj/Desktop/mouse.txt",
                        help="Absolute File Path to file to be manipulated")
  parser.add_argument("-s","--search",dest="searcher",default="the",
                        help="the word to be replaced")
  parser.add_argument("-r","--replace",dest="replacer",default="teh",
                        help="the word to replace the searched word with")

  args = parser.parse_args()
  return args

if __name__ == "__main__":
  main()
