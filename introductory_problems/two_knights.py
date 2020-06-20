#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

n = int(input())

num_list = []

for k in range(1,n+1): # all the possible chessboard sizes
	if k <= 4: # Do the slow method from 1 - 4
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
		num_list.append(count)

	else: # cubic formula was derived after many headaches
		# Send me an email if you wish to know how this formula was derived
		num_list.append(4*k**3 - 12*k**2 - 2*k + 34 + num_list[-2])

for x in num_list:
	print(x)