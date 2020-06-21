#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

n = int(input())

num_list = [x+1 for x in list(range(n))]
set_1 = []
set_2 = []

n_sum = sum(num_list) // 2

if n%4 == 1 or n%4 == 2:
	print("NO")

else:
	if n%4 == 0:
		for x in num_list:
			if x%4 == 1 or x%4 == 0:
				set_1.append(str(x))
			else:
				set_2.append(str(x))

	else:
		set_1.append('1')
		set_1.append('2')
		set_2.append('3')

		for x in num_list:
			if x > 3:
				if (x-3)%4 == 1 or (x-3)%4 == 0:
					set_1.append(str(x))
				else:
					set_2.append(str(x))

	print("YES")
	print(len(set_1))
	print(" ".join(set_1))
	print(len(set_2))
	print(" ".join(set_2))




