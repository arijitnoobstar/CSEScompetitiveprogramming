#!/usr/bin/python
# -*- coding: UTF-8 -*-
#------------------------------*
# Author: Arijit Dasgupta      |
# Email: arijit.dg@hotmail.com |
#------------------------------*

'''
After doing some eploratory analysis, I realised the number of zeros
is related to the number of times the factorial crosses 5^x where x>1 
and number > 5^x
'''

n = int(input())

n_zeros = 0
five_exponent = 1

while 5**five_exponent <= n:

	n_zeros	+= n // 5**five_exponent
	five_exponent += 1

print(n_zeros)