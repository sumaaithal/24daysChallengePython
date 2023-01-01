# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:17:19 2022

@author: SKUP
"""

"""
Please write a program which accepts a string from console and print the 
characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld
"""

s = input("enter the string:>>")

list1 = []

for i,v in enumerate(s):
    if i%2==0:
        list1.append(v)
        
        
res = "".join(list1)

print(res)
        

