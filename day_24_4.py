# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:24:16 2022

@author: SKUP
"""

"""
Given a number N.Find Sum of 1 to N Using Recursion

Input

5
Output

15
Hints
Make a recursive function to get the sum
"""

def rec(n):
    
    if n == 1:
        return 1
    
    else:
        return n+rec(n-1)
    

print(rec(5))