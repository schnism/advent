#!/usr/bin/python

import sys

biggest = 0
sumelf = 0

for line in sys.stdin:
	if len(line)==1:
		print("Summe " ,sumelf)
		if sumelf>biggest:
			biggest=sumelf
		sumelf=0
	else:
		sumelf += int(line)

print("Biggest: ", biggest)
