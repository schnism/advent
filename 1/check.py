#!/usr/bin/python

import sys

total=0

for line in sys.stdin:
	first='X'
	last='X'
	for c in line:
		if c.isdigit():
			if first=='X':
				first=c
				last=c
			else:
				last=c

	lineresult = int(first)*10+int(last)
	print(lineresult)
	total += lineresult

print(total)

