#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

n = int(input())
num = n-1

beautiful = []

# 1st pass
while num > 0:
	beautiful.append(str(num))
	num -= 2


if len(beautiful) > 0 and int(beautiful[-1]) + 1 == n: # ensure starting of 2nd pass is not beside last of first pass
	print("NO SOLUTION")
else:
	num = n
	# 2nd pass
	while num > 0:
		beautiful.append(str(num))
		num -= 2

	print(" ".join(beautiful))
