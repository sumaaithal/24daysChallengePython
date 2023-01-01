# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:08:40 2022

@author: SKUP
"""

"""
Please write a program which count and print the numbers of each 
character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

"""

s = input("enter the string>>")

d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+= 1
        
for k,v in d.items():
    print(k+","+str(v))