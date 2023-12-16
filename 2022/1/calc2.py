#!/usr/bin/python

import sys

sumelf = 0
sums = []

for line in sys.stdin:
	if len(line)==1:
		sums.append(sumelf)
		sumelf=0
	else:
		sumelf += int(line)

sums.sort(reverse=True)
print("Biggest: ",sums[0])
print("Biggest 3:",sums[0]+sums[1]+sums[2])
