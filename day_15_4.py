# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:10:09 2022

@author: SKUP
"""

"""
Write a program to read an ASCII string and to convert it to a unicode 
string encoded by utf-8.

Hints
Use unicode()/encode() function to convert.
"""

s = input("enter the string:>>>")

s.encode("utf-8")

print(s)