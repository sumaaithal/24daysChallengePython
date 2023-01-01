# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:41:17 2022

@author: SKUP
"""

"""
Please write a program which accepts basic mathematic expression from 
console and print the evaluation result.

Example: If the following n is given as input to the program:

35 + 3
Then, the output of the program should be:

38
"""


n = input("enter the input").split(" ")

#print(n)

print(int(n[0])+int(n[1]))