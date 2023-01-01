# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:45:45 2022

@author: SKUP
"""

"""
By using list comprehension, please write a program to print the 
list after removing the value 24 in [12,24,35,24,88,120,155].

Hints
Use list's remove method to delete a value.
"""
l = [12,24,35,24,88,120,155]

new_list = [v for v in l if v!=24]

print(new_list)