#!/usr/bin/python

import sys

total=0

currval = 0 
valid = False

lines = sys.stdin.readlines()

for lineno in range(0,len(lines)):
	for colno in range(0,len(lines[lineno])):
		c = lines[lineno][colno]
		if c.isnumeric():
			currval = currval*10+int(c)

			a='.'
			if lineno>1 and colno>1: a = lines[lineno-1][colno-1]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if colno>1: a = lines[lineno+0][colno-1]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if lineno<len(lines)-1 and colno>1: a = lines[lineno+1][colno-1]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if lineno>1: a = lines[lineno-1][colno+0]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if lineno<len(lines)-1: a = lines[lineno+1][colno+0]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if lineno>1 and colno<len(lines[lineno])-2: a = lines[lineno-1][colno+1]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if colno<len(lines[lineno])-2: a = lines[lineno+0][colno+1]
			if a!='.' and not(a.isnumeric()):
				valid=True
			if lineno<len(lines)-1 and colno<len(lines[lineno])-2: a = lines[lineno+1][colno+1]
			if a!='.' and not(a.isnumeric()):
				valid=True



		if not c.isnumeric() or colno==len(lines[lineno]):
			if currval>0: print(currval,valid)
			if valid : total+=currval
			currval=0
			valid=False

print(total)
