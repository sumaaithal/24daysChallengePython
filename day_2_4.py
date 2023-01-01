# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:36:09 2022

@author: SKUP
"""
"""
_Write a program which takes 2 digits, X,Y as input and generates a 
2-dimensional array. The element value in the i-th row and j-th column o
f the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given 
to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question, 
it should be assumed to be a console input in a comma-separated form.
"""
input_string = input()

dimentions = [int(x) for x in input_string.split(',')]


row_num = dimentions[0]
col_num = dimentions[1]

multilist = [[0 for col in range(col_num)] for row in range(row_num)]

for r in range(row_num):
    for c in range(col_num):
        multilist[r][c] = r*c
        
        
print(multilist)
