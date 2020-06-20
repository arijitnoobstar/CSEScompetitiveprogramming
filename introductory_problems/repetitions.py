#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

dna_seq = input()

max_rep = 1
cur_rep = 1

for i in range(1, len(dna_seq)):

	if dna_seq[i] == dna_seq[i-1]:
		cur_rep += 1
		if cur_rep > max_rep:
			max_rep = cur_rep
	else:
		if cur_rep > max_rep:
			max_rep = cur_rep
		cur_rep = 1

print(max_rep)