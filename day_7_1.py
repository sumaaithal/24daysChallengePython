# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:32:17 2022

@author: SKUP
"""

"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
"""

class DivBYSeven:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    
    def display(self):
        for i in range(self.start,self.end+1):
            if i%7==0:
                yield i
                

d = DivBYSeven(0, 14).display()

for i in d:
    print(i)