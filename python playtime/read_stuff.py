#!/usr/bin/env python

import csv, os, sys, argparse

def main():
  arguments = get_args()

  try:
    with open(arguments.thefile,'r+') as f:
      datain = csv.reader(f,delimiter=',')
      dataout = csv.writer(f,delimiter=',')
      for row in datain:
        print row[1]
      #dataout.writerow(['Ben','60 morrow ave','Male','87'])
  except:
    print "failed to open ",arguments.thefile,"."
    sys.exit(1)

  f.close()
  sys.exit(0)

def get_args():
  parser = argparse.ArgumentParser(description="simple file manipulation")
  parser.add_argument("-f","--file",dest="thefile",
                        default="/Users/peltzaj/Desktop/Workbook1.csv",
                        help="Absolute File Path")
  args = parser.parse_args()
  return args

if __name__ == "__main__":
  main()
