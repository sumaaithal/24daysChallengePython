# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:36:50 2022

@author: SKUP
"""

"""
Please write assert statements to verify that every number in 
the list [2,4,6,8] is even.

Hints
Use "assert expression" to make assertion.
"""

for i in [2,4,5,6,8]:
   assert i%2==0,"{} is not an even number".format(i)