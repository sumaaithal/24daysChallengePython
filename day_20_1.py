# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:51:37 2022

@author: SKUP
"""

"""
Please write a program to print the list after removing 
even numbers in [5,6,77,45,22,12,24].

Hints
Use list comprehension to delete a bunch of element from a
 list.
"""

non_even = [i for i in [5,6,77,45,22,12,24] if i%2!=0]

print(non_even)