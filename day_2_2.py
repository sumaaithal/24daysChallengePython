# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:15:55 2022

@author: SKUP
"""

"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
"""
class IOString:
    
    def __init__(self):
        self.s = ''
        
    
    def get_string(self):
        self.s = input()
        
    
    def get_upper_string(self):
        print(self.s.upper())
        
        
    

s = IOString()

s.get_string()

s.get_upper_string()