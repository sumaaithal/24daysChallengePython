# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:42:48 2022

@author: SKUP
"""

"""
By using list comprehension, please write a program to print the list 
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints
Use list comprehension to delete a bunch of element from a list.Use 
enumerate() to get (index, value) tuple.
"""

new_list = [v for i,v in enumerate([12,24,35,70,88,120,155]) if i!=0 and i!=4 and i!=5]

print(new_list)