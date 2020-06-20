#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

len_arr = int(input())
arr = [int(x) for x in input().split()]

turns = 0

for i in range(1, len_arr):
	if arr[i] < arr[i-1]:
		turns += arr[i-1] - arr[i]
		arr[i] = arr[i-1]

print(turns)