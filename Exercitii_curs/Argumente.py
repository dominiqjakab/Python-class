#!/usr/bin/python3.10

import sys

n = len(sys.argv)

if n <3:
    print("Usage: ./Argumente.py nr1 nr.2")
    exit()

print("Number of arguments found: " + str(n) + "\n1st: " + sys.argv[0] + "\n2nd: " + sys.argv[1])

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

b = a1 + a2
print("Sum is " + str(b))