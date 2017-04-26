#!/usr/bin/env python

import os, sys, argparse, json
from pprint import pprint


def main():
  it = get_args()
  with open(it.thefile,'r') as datafile:
    data = json.load(datafile)
    print data['firstName']
  sys.exit(0)

def get_args():
  parser = argparse.ArgumentParser(description="read in a json file and plays with it")
  parser.add_argument("-f","--file",dest="thefile",default="customers.json",
                        help="please specify a file")
  args = parser.parse_args()
  return args

if __name__ == "__main__":
  main()
