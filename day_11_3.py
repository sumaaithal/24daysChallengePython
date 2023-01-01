# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:38:15 2022

@author: SKUP
"""

"""
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:
Use if statement to judge condition.
"""


s = input("enter the string: >> ")

if (s == 'yes') or (s=='YES') :
    print('Yes')

else:
    print('No')