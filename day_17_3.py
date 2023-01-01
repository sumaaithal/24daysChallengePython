# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:47:19 2022

@author: SKUP
"""

"""
Please write a binary search function which searches an item in a 
sorted list. The function should return the index of element to be 
searched in the list.

Hints
Use if/elif to deal with conditions.
"""

def bin_search(li,key):
    low = 0
    high = len(li)-1
    
    mid = 0
    
    while low <= high:
        
        mid = (low+high)//2
        
        if li[mid] < key:
            low = mid + 1
            
        elif li[mid] > key:
            high = mid - 1
        
        else:
            return mid
    
    return -1
    
res = bin_search([5,8,10,11,15,18,20], 18)

print(res)
            
        
    

