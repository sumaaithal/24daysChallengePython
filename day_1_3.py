# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:26:25 2022

@author: SKUP
"""

"""
With a given integral number n, write a program to generate a 
dictionary that contains (i, i x i) such that is an integral number 
between 1 and n (both included). and then the program should print 
the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be 
assumed to be a console input.Consider use dict()
"""
# =============================================================================
# try:
#     
#     num = int(input())
#     
# except ValueError as err:
#     print(err)
#     
# a = {}
# 
# for i in range(num+1):
#     if i == 0:
#         continue
#     else:
#         
#         a[i] = i*i
#     
# print(a)
# =============================================================================


n = int(input())

print(dict(enumerate([i*i for i in range(1,n+1)],1)))