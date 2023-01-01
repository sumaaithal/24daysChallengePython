# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:47:54 2022

@author: SKUP
"""

"""
Write a program which can map() and filter() to make a list whose 
elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:
Use map() to generate a list.Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
"""

filtered_list = list(filter(lambda x: x%2==0,[1,2,3,4,5,6,7,8,9,10]))

square_of_list = list(map(lambda x: x**2, filtered_list))

print(square_of_list)