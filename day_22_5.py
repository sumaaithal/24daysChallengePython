# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:21:48 2022

@author: SKUP
"""

"""
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?

Hints
Use for loop to iterate all possible solutions.
"""

heads = 35
legs = 94

rabitlegs = 4

rabits = legs//rabitlegs

chiken = heads - rabits

print(rabits, chiken)