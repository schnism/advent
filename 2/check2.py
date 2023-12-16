#!/usr/bin/python

import sys

total=0

for line in sys.stdin:
	game, hands = line.split(':')
	game = int(game.split(' ')[1])
	maxred=0
	maxgreen=0
	maxblue=0
	for hand in hands.split('; '):
		for cubes in hand.split(','):
			amount, color = cubes.strip().split(' ')
			amount=int(amount)
			if color == "red" and amount>maxred: maxred=amount
			if color == "green" and amount>maxgreen: maxgreen=amount
			if color == "blue" and amount>maxblue: maxblue=amount
	total += maxred*maxgreen*maxblue

print(total)

