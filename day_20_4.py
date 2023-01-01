# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:03:40 2022

@author: SKUP
"""

"""
By using list comprehension, please write a program to print the 
list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list. Use
enumerate() to get (index, value) tuple.
"""

list_indx = [v for i,v in enumerate([12,24,35,70,88,120,155]) if i!=2 and i!=4]

print(list_indx)