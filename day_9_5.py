# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:06:54 2022

@author: SKUP
"""

"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

Hints:
Use len() function to get the length of a string.
"""

def max_string_len_display(s1,s2):
    len_1 = len(s1)
    len_2 = len(s2)
    
    if len_1 > len_2:
        return s1
    else:
        return s2
    
    
res = max_string_len_display("archipelagio", "summacumlaude")

print(res)