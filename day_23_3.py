# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:44:10 2022

@author: SKUP
"""

"""
You are given an integer, N. Your task is to print an alphabet rangoli 
of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
Hints
First print the half of the Rangoli in the given way and save each 
line in a list. Then print the list in reverse order to get the rest.

"""

import string

def rangoli_pattern(n):
    L = []
    
    s = ''
    for i in range(n):
        alpha = string.ascii_lowercase
        
        s = "-".join(alpha[i:n])
        
        
        
        L.append((s[::-1]+s[1:]).center(4*n-3 , '-'))
        
        print(L)
    
    print('\n'.join(L[:0:-1]+L))
    

rangoli_pattern(8)
    
    






