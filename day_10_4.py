# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:00:12 2022

@author: SKUP
"""

"""
Define a function which can generate and print a list where the values
 are square of numbers between 1 and 20 (both included).

Hints:
Use ** operator to get power of a number.Use range() for loops.
Use list.append() to add values into a list.
"""

def dict_list():
    l1 = []
    for i in range(1,21):
        l1.append(i**2)
    
    return l1

res = dict_list()
print(res)        