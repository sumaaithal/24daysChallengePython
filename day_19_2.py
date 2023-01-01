# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:23:12 2022

@author: SKUP
"""

"""
Please write a program to compress and decompress the string 
"hello world!hello world!hello world!hello world!".

Hints
Use zlib.compress() and zlib.decompress() to compress and decompress a strin
"""
import zlib

s = 'hello world!hello world!hello world!hello world!'

y = bytes(s,'utf-8')

c = zlib.compress(y)

print(c)

d = zlib.decompress(c)

print(d)
