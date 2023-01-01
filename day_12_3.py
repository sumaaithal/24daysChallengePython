# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:48:12 2022

@author: SKUP
"""

"""
Define a class named American and its subclass NewYorker.

Hints:
Use class Subclass(ParentClass) to define a subclass.*
"""

class American:
    
    @staticmethod 
    def printNationality():
        print("I'm american")
        
class NewYorker(American):
    pass


n = NewYorker()

n.printNationality()
            