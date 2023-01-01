# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:38:05 2022

@author: SKUP
"""

"""
Please write a program using generator to print the numbers which can be 
divisible by 5 and 7 between 0 and n in comma separated form while n is 
input by console.

Example: If the following n is given as input to the program:

100
Then, the output of the program should be:

0,35,70
In case of input data being supplied to the question, it should be assumed to 
be a console input.
"""

def div_5_7(n):
    
    for i in range(n+1):
        
        if i%5==0 and i%7==0:
            
            yield i
            

val = []
n = int(input())

for i in div_5_7(n):
    val.append(i)
    
print(val)