# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:30:22 2022

@author: SKUP
"""

"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to 
print the first half values in one line and the last half values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""

t = (1,2,3,4,5,6,7,8,9,10)

len_tuple = len(t)

first_half = int(len_tuple/2)

#print(first_half)

#print(t[first_half])

print(t[:first_half])
print(t[first_half:])

