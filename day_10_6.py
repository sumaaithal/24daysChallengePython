# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:03:21 2022

@author: SKUP
"""

"""
Define a function which can generate a list where the values are square 
of numbers between 1 and 20 (both included). Then the function needs to 
print the last 5 elements in the list.

Hints:
Use ** operator to get power of a number.Use range() for loops.
Use list.append() to add values into a list.Use [n1:n2] to slice a list
"""

def sq_list():
    l1 = []
    for i in range(1,21):
        l1.append(i**2)
        
    return l1[-5:]

res = sq_list()

print(res)