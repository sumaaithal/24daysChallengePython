# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:33:27 2022

@author: SKUP
"""

"""
Please write a program using generator to print the even numbers between 
0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10
Then, the output of the program should be:

0,2,4,6,8,10
In case of input data being supplied to the question, it should be assumed 
to be a console input.

Hints
Use yield to produce the next value in generator.
"""

def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i

n = int(input())
val = []

for i in even(n):
    val.append(i)

print(val)
            
    