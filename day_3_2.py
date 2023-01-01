# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:38:04 2022

@author: SKUP
"""
"""
Write a program which accepts a sequence of comma separated 
4 digit binary numbers as its input and then check whether they 
are divisible by 5 or not. The numbers that are divisible by 5 are to 
be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.
"""
def check(x):
    return int(x,2)%5==0


data =  input().split(',')

l1 = ",".join(list(filter(check,data)))

print(l1)