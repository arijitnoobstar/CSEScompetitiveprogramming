#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

line = input()

char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
palindrome = []
odd_list = []
check_double_odd = 0
idx = 0

for char in char_list:
	if char in line:
		char_count = line.count(char)
		if char_count%2 != 0:
			check_double_odd += 1
			odd_list.append(char)
		palindrome.insert(idx, char*(char_count//2))
		palindrome.insert(idx + 1, char*(char_count//2))
		idx += 1

if check_double_odd > 1:
	print("NO SOLUTION")
else:
	if check_double_odd == 1:
		palindrome.insert(idx, odd_list[0])
	print("".join(palindrome))
