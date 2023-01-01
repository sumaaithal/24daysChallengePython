# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:41:13 2022

@author: SKUP
"""

"""
You are given a string S and width W. Your task is to wrap the string 
into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
Hints
Use wrap function of textwrap module
"""

import textwrap

string = input("enter the string: >> ")

width = int(input("enter the width: >> "))

res = textwrap.wrap(string,width)

for i in res:
    print(i)