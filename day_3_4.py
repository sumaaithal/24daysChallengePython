# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:08:39 2022

@author: SKUP
"""
"""
Write a program that accepts a sentence and calculate the number of 
letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
"""
s = input()
alpha_count = 0
digit_count = 0

for char in s:
    if char.isalpha():
        alpha_count+=1

    elif char.isdigit():
        digit_count+=1
    
    
print("number of letters:",alpha_count)
print("number of digits:",digit_count)

    