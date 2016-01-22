#!/usr/bin/python
currentTerm = 0
a = 0
b = 1
while(currentTerm < 10):
 print("Term ", currentTerm + 1, " = ", a)
 new = a + b
 a = b
 b = new
 
 currentTerm = currentTerm + 1
