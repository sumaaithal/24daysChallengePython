# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:59:19 2022

@author: SKUP
"""
"""
Use a list comprehension to square each odd number in a list. The list 
is input by a sequence of comma-separated numbers. >Suppose the following 
input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
"""
l1 = input("enter the integers: >> ").split(",")

res = [str(int(i)**2) for i in l1 if int(i)%2!=0]

print(",".join(res))