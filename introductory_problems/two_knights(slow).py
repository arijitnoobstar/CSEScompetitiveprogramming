#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*
n = int(input())

for k in range(1,n+1): # all the possible chessboard sizes
	count = 0 
	for i in range(k): # x-direction
		for j in range(k): # y-direction
			count += k**2 - 1 # assume all other positions on board are not attackable
			# check all 8 possible knight atatck positions and see if they are on the board
			# If they are, reduce count by 1
			if i+2 < k and j-1 >= 0:
				count -= 1
			if i+2 < k and j+1 < k:
				count -= 1
			if i+1 < k and j+2 < k:
				count -= 1
			if i-1 >= 0 and j+2 < k:
				count -= 1
			if i-2 >= 0 and j+1 < k:
				count -= 1
			if i-2 >= 0 and j-1 >= 0:
				count -= 1
			if i-1 >= 0 and j-2 >= 0:
				count -= 1
			if i+1 < k and j-2 >= 0:
				count -= 1
	count //= 2 # as both knights are identical, we must account for duplicated combinations
	print(count)
