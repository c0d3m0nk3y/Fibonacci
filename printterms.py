#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--targetTerm", help="The number of terms to print", type=int)
args = parser.parse_args()

currentTerm = 0
a = 0
b = 1

while(currentTerm < args.targetTerm):
 print("Term ", currentTerm + 1, " = ", a)
 new = a + b
 a = b
 b = new
 
 currentTerm = currentTerm + 1
