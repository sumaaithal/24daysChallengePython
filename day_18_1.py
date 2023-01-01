# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:25:23 2022

@author: SKUP
"""

"""
Please write a program to output a random even number between 
0 and 10 inclusive using random module and list comprehension.

Hints
Use random.choice() to a random element from a list.
"""

import random

res = [i for i in range(0,11,2)]

#print(res)

print(random.choice(res))



