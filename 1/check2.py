#!/usr/bin/python

import sys

total=0

for line in sys.stdin:
	line = line.replace('one','one1one')
	line = line.replace('two','two2two')
	line = line.replace('three','three3three')
	line = line.replace('four','four4four')
	line = line.replace('five','five5five')
	line = line.replace('six','six6six')
	line = line.replace('seven','seven7seven')
	line = line.replace('eight','eight8eight')
	line = line.replace('nine','nine9nine')

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

