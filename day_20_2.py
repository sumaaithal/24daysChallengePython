# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:58:58 2022

@author: SKUP
"""

"""
By using list comprehension, please write a program to print the list 
after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.
"""

non_div_5_7 = [i for i in [12,24,35,70,88,120,155] if i%7!=0 and i%5!=0]

print(non_div_5_7)