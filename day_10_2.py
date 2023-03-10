# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:57:29 2022

@author: SKUP
"""

"""
Define a function which can generate a dictionary where the keys 
are numbers between 1 and 20 (both included) and the values are 
square of keys. The function should just print the keys only.

Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** 
operator to get power of a number.Use range() for loops.Use keys() 
to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

"""

def dict_keys():
    d = {}
    for i in range(1,21):
        d[i] = i**2
        
    return d.keys()

res = dict_keys()

print(res)

