# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:26:16 2022

@author: SKUP
"""

from itertools import product


list1 = ["I", "You"]
list2 = ["Play", "Love"]
list3 = ["Hockey","Football"]


prod = [p for p in product(range(2), repeat=3)]

for comb in prod:
    print(list1[comb[0]], list2[comb[1]],list3[comb[2]])