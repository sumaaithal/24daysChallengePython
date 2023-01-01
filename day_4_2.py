# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:10:28 2022

@author: SKUP
"""
"""
Write a program that computes the value of a+aa+aaa+aaaa with a given 
digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
"""
a = input("enter the number:")
res = 0

for i in range(1,5):
    res+= int(a*i)
    
print(res)

