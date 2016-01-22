#!/usr/bin/python

import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("targetTerm", help="The number of terms to print", type=int)
parser.add_argument("-a", "--printAll", help="Print all of the terms", type=bool)
args = parser.parse_args()

currentTerm = 0
a = 0
b = 1

strings = []
start = time.time()
while(currentTerm < args.targetTerm):
 strings.append("Term %s = %s" % (currentTerm + 1, a))
 new = a + b
 a = b
 b = new
 
 currentTerm = currentTerm + 1
 
if(args.printAll):
 print("\n".join(strings), "\nCalculated in : ", time.time() - start)
 print("Printed in : ", time.time() - start)
else:
 print("Term ", args.targetTerm, " = ", b - a, "\nCalculated in : ", time.time() - start)
