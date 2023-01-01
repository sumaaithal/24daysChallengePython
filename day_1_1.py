# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:59:16 2022

@author: SKUP
"""
"""
Write a program which will find all such numbers which are divisible by 
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence 
on a single line.

Hints:
Consider use range(#begin, #end) method.
"""
def div_7_not_5(low,high):
    result = []
    for i in range(low,high+1):
        if i%7 == 0 and i%5!=0:
            result.append(i)
            
        
    return ",".join([str(i) for i in result])
        
        


a = div_7_not_5(2000, 3200)
print(a)
            