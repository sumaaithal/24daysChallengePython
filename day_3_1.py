# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:34:00 2022

@author: SKUP
"""
"""
Write a program that accepts a sequence of whitespace separated words as 
input and prints the words after removing all duplicate words and sorting 
them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
"""
s = input()

s1 = s.split(' ')

s2 = sorted(set(s1))

s3 = " ".join(s2)

print(s3)