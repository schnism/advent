#!/usr/bin/python

import sys

total=0

for line in sys.stdin:
	possible = True
	game, hands = line.split(':')
	game = int(game.split(' ')[1])
	for hand in hands.split('; '):
		for cubes in hand.split(','):
			amount, color = cubes.strip().split(' ')
			amount=int(amount)
			if color == "red" and amount>12: possible=False
			if color == "green" and amount>13: possible=False
			if color == "blue" and amount>14: possible=False
	if possible: total += game

print(total)

