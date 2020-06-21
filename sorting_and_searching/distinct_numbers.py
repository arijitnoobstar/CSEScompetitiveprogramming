#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

input() # not needed

# Below is the one line solution
print(len(set([int(x) for x in input().split()])))
