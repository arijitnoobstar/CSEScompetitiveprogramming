#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

from itertools import permutations

# I am not satisfied with this solution as it relies 
# on an import, I hope to improve this in the future

line = input()

permlist = sorted(set(permutations(line)))

# permutations show all possible permutations (not accounting for same objects)
# set is used to only keep unique objects
# sorted is used to sort in alphabetical order

print(len(permlist))
for perm in permlist:
	print("".join(perm))