# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:16:29 2022

@author: SKUP
"""

"""
Please write a program to generate all sentences where subject is 
in ["I", "You"] and verb is in ["Play", "Love"] and the object is 
in ["Hockey","Football"].

Hints
Use list[index] notation to get a element from a list.
"""

list1 = ["I", "You"]
list2 = ["Play", "Love"]
list3 = ["Hockey","Football"]

for i in list1:
    for j in list2:
        for k in list3:
            print(i+" "+j+" "+k)