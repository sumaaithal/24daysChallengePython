# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:54:28 2022

@author: SKUP
"""

"""
Define a function which can print a dictionary where the keys are
 numbers between 1 and 20 (both included) and the values are square of keys.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** 
operator to get power of a number.Use range() for loops.
"""

def square_dict():
    d = {}
    for i in range(1,21):
        d[i] = i**2
        
    return d


res = square_dict()
print(res)
        


