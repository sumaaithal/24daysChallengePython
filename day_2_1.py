# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:58:22 2022

@author: SKUP
"""
"""
Write a program which accepts a sequence of comma-separated numbers 
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
a = input("enter the numbers:")

list1 = a.split(',')

list2 = list(list1)
print(list2)

print(tuple(list2))
