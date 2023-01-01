# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:49:34 2022

@author: SKUP
"""

"""
With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate 
values with original order reserved.

Hints
Use set() to store a number of values without duplicate.
"""

l1 = [12,24,35,24,88,120,155,88,120,155]

new_li = []
#seen = set()

for i in l1:
    
    if i not in new_li:
        
        
        new_li.append(i)
        

print(new_li)
#print(seen)