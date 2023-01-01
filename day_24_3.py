# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:21:35 2022

@author: SKUP
"""

"""
Write a Python program that accepts a string and calculate the 
number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8
"""

dig = 0
lett = 0

s = input("enter the string:>>")

for i in s:
    if i.isalpha():
        lett+=1
    
    elif i.isdigit():
        dig+=1
        
    else:
        pass

print("digit - {} \nLetter - {}".format(dig, lett))