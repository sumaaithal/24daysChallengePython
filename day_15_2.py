# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:05:46 2022

@author: SKUP
"""

"""
Write a program which accepts a sequence of words separated by whitespace as 
input to print the words composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.
Then, the output of the program should be:

['2', '3']
"""

l = input("enter the string: >>").split(" ")

res = []

print(l)

for i in l:
    if i.isdigit():
        res.append(i)
    
    else:
        pass
    
print(res)