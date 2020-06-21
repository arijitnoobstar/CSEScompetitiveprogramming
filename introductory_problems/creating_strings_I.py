#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

def factorial(n):

	fac = 1
	while n != 1:
		fac *= n
		n -=1
	return fac

line = input()
len_line = len(line)
'''
char_list = 'abcdefghijklmnopqrstuvwxyz'



num_strings = factorial(len_line)

unique_chars = []
unique_count = []
strings = []

for x in line:
	if x not in unique_chars:
		unique_chars.append(x)
		unique_count.append(line.count(x))
		num_strings //= factorial(line.count(x))

unique_len = len(unique_chars)

print(num_strings)

'''
groups = [list(line)] * len_line
strings = [[]]
for i in groups:
	strings = [x + [y] for x in strings for y in i]

for i in range(len(strings)):
	strings[i] = "".join(strings[i])
print(list(strings))




