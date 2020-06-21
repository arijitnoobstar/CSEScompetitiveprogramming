#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

n = int(input())

def can_empty(a, b):

	if a > 2*b or b > 2*a:
		return "NO"
	if (a+b)%3 != 0:
		return "NO"
	if a+b == 0:
		return "YES"

	return "YES"

bool_list = []
for i in range(n):
	pile = [int(x) for x in input().split()]
	bool_list.append(can_empty(pile[0], pile[1]))

for x in bool_list:
	print(x)

