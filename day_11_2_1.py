# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:38:58 2022

@author: SKUP
"""

def evens(n):
    if n%2==0:
        return n
    

res = tuple(filter(evens, (1,2,3,4,5,6,7,8,9,10)))
print(res)
