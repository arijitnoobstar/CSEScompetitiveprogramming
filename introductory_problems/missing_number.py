#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*
len_line = int(input())

sum_line = len_line*(len_line+1)//2

line = [int(x) for x in input().split()]

missing_num = sum_line - sum(line)

print(missing_num)
