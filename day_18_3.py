# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:34:26 2022

@author: SKUP
"""

"""
Please write a program to generate a list with 5 random numbers between 
100 and 200 inclusive.

Hints
Use random.sample() to generate a list of random values.
"""

import random

vals = [i for i in range(100,201)]

print(random.sample(vals, 5))