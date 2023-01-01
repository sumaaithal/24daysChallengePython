# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:46:35 2022

@author: SKUP
"""
"""
Write a program that accepts sequence of lines as input and prints 
the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
"""
l1 = []

while True:
    s = input()
    
    if s:
        l1.append(s.upper())
        
    else:
        break
    
    
for l in l1:
    print(l)