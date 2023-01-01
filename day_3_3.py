# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:54:49 2022

@author: SKUP
"""
"""
Write a program, which will find all such numbers between 1000 and 
3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a 
single line.

Hints:
In case of input data being supplied to the question, it should be assumed 
to be a console input.
"""

new_list = []
for item in range(1000,3001):
    
    item1 = str(item)
    if int(item1[0])%2==0 | int(item1[1])%2==0 | int(item1[2])%2==0 | int(item1[3])%2==0:
            
            new_list.append(item)
            
    else:
        pass
        

print(new_list)
            