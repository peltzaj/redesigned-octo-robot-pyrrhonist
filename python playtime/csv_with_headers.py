#!/usr/bin/env python

import os, sys, argparse, csv

def main():
  it = get_args()
  with open(it.thefile,'r+') as csvfile:
    readthis = csv.DictReader(csvfile)
    writethis = csv.DictWriter(csvfile, fieldnames=readthis.fieldnames)
    for rows in readthis:
        print rows
    writethis.writerow({readthis.fieldnames[0]: 'Ben', \
                         readthis.fieldnames[1]: 'Brand', \
                         readthis.fieldnames[2]: '60 morrow ave', \
                         readthis.fieldnames[3]: 'Male', \
                         readthis.fieldnames[4]: '87',})
  csvfile.close()
  sys.exit(0)

def get_args():
  parser = argparse.ArgumentParser(description="This script will play with a csv file with header")
  parser.add_argument("-f","--file",dest="thefile",default="header.csv",
                        help="the path of the file to read")

  args = parser.parse_args()
  return args

if __name__ == "__main__":
  main()
