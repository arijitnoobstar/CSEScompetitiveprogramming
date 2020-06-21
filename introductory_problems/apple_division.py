#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

# Note that this algorithm is inefficient and works just well enough within the constraints

from itertools import combinations

n = int(input())

weights = [int(x) for x in input().split()]

if n == 1:
	print(weights[0])
else:
	grp_1 = []
	sum_1 = 0
	grp_2 = weights
	sum_2 = sum(weights)
	count = 1

	while True:

		if sum_2 > sum_1:
			diff = sum_2 - sum_1
			temp_grp_2 = grp_2.copy()

			for i in range(2, len(grp_2)):
				for comb in combinations(grp_2, r = i):
					temp_grp_2.append(comb)

			diff_grp_2 = [abs(x-diff/2) if type(x) == int else abs(sum(x)-diff/2) for x in temp_grp_2]

			if min(diff_grp_2) < diff / 2:
				swap_idx = diff_grp_2.index(min(diff_grp_2))
				swap_val =temp_grp_2[swap_idx]
				if type(swap_val) == tuple:
					for x in swap_val:
						grp_1.append(x)
						sum_1 += x
						grp_2.remove(x)
						sum_2 -= x
				else:
					grp_1.append(swap_val)
					sum_1 += swap_val
					grp_2.remove(swap_val)
					sum_2 -= swap_val
			else:
				break
		else:
			diff = sum_1 - sum_2
			temp_grp_1 = grp_1.copy()

			for i in range(2, len(grp_1)):
				for comb in combinations(grp_1, r = i):
					temp_grp_1.append(comb)

			diff_grp_1 = [abs(x-diff/2) if type(x) == int else abs(sum(x)-diff/2) for x in temp_grp_1]

			if min(diff_grp_1) < diff / 2:
				swap_idx = diff_grp_1.index(min(diff_grp_1))
				swap_val =temp_grp_1[swap_idx]
				if type(swap_val) == tuple:
					for x in swap_val:
						grp_2.append(x)
						sum_2 += x
						grp_1.remove(x)
						sum_1 -= x
				else:
					grp_2.append(swap_val)
					sum_2 += swap_val
					grp_1.remove(swap_val)
					sum_1 -= swap_val
			else:
				break
	print(abs(sum_2 - sum_1))



