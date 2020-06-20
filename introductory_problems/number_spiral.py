#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

num_tests = int(input())

num_list = []

def num_spiral(x,y):

	if x >= y:
		if x%2 == 0:
			num = (x-1)**2 + y
		else:
			num = x**2 - y + 1			
	else:
		if y%2 == 0:
			num = y**2 - x + 1
		else:
			num = (y-1)**2 + x
			
	return num

for i in range(num_tests):
	coord = [int(x) for x in input().split()]
	num_list.append(num_spiral(coord[1], coord[0]))


for x in num_list:
	print(x)
