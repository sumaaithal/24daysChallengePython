# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:05:51 2022

@author: SKUP
"""

"""
By using list comprehension, please write a program generate a 
3*5*8 3D array whose each element is 0.

Hints
Use list comprehension to make an array.
"""

multi_dim_array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]

print(multi_dim_array)