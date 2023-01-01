# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:01:48 2022

@author: SKUP
"""
"""
Write a program that accepts a sentence and calculate the number of 
upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
"""
def upper_lower(s):
    count_upper = 0
    count_lower = 0
    for i in s:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
            
    print("Upper case: {}".format(count_upper))
    print("Lower case: {}".format(count_lower))


upper_lower("Hello world")