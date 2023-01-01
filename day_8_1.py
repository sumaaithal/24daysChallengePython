# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 22:41:24 2022

@author: SKUP
"""

"""
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

"""

s = input("enter the string:>>").split(' ')

new_dict = {}

for e in s:
    if e in new_dict:
        new_dict[e]+=1
    
    else:
        new_dict[e] = 1

d = dict(sorted(new_dict.items()))

for i in d:
    print(i,":",d[i])