# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:44:07 2022

@author: SKUP
"""

"""
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.There are also two 
more methods.
"""


class American:
    
    @staticmethod
    def printNationality():
        print("I'm American")
        
    
    
a = American()

a.printNationality()