#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

n = int(input())

num_list = [str(n)]

while n!= 1:

	if n%2 == 0:
		n //= 2
		num_list.append(str(n))
	else:
		n = 3*n +1
		num_list.append(str(n))

print(" ".join(num_list))