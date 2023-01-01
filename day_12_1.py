# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:42:06 2022

@author: SKUP
"""

"""
Write a program which can map() to make a list whose elements are 
square of numbers between 1 and 20 (both included).

Hints:
Use map() to generate a list. Use lambda to define anonymous functions.
"""

res = list(map(lambda x: x**2, range(1,21)))

print(res)