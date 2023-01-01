# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:46:29 2022

@author: SKUP
"""

"""
Write a program which can map() to make a list whose elements are 
square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.Use lambda to define anonymous functions.
"""

res = list(map(lambda x:x**2, [1,2,3,4,5,6,7,8,9,10]))

print(res)