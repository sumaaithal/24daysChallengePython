# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:09:25 2022

@author: SKUP
"""
"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single 
line.Suppose the following input is supplied to the program: 8 Then, 
the output should be:40320

Hints:
In case of input data being supplied to the question, it should be 
assumed to be a console input.
"""
# =============================================================================
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# 
# a = factorial(8)
# print(a)
# =============================================================================

# =============================================================================
# def factorial(n):
#     i = 1
#     fact = 1
#     while i <= n:
#         fact *= i
#         i+=1
#         
#     return fact
# 
# a = factorial(8)
# print(a)
# =============================================================================

# =============================================================================
# n = int(input('enter the number: '))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
# =============================================================================

from functools import reduce


def fact(acc,item):
    return acc*item

num = int(input())
print(reduce(fact, range(1,num+1), 1))









