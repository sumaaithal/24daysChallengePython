# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:15:41 2022

@author: SKUP
"""

"""
Please write a program which accepts a string from console and 
print it in reverse order.

Example: If the following string is given as input to the program:*

rise to vote sir
Then, the output of the program should be:

ris etov ot esir
"""

s = input("enter the string:>>")

new_s = s[::-1]

print(new_s)