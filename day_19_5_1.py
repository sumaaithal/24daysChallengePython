# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:38:12 2022

@author: SKUP
"""

import itertools


list1 = ["I", "You"]
list2 = ["Play", "Love"]
list3 = ["Hockey","Football"]

sent = [list1,list2,list3]


l = itertools.product(*sent)

for i in l:
    print(i)