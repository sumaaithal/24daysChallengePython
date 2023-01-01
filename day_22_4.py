# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:20:19 2022

@author: SKUP
"""

"""
Please write a program which prints all permutations of [1,2,3]

Hints
Use itertools.permutations() to get permutations of list.
"""

import itertools

for i in itertools.permutations([1,2,3]):
    print(i)