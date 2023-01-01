# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:55:44 2022

@author: SKUP
"""

"""
Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male 
class and "Female" for Female class.

Hints
Use Subclass(Parentclass) to define a child class.
"""

class Parent:
    
    pass

class Child(Parent):
    
    def __init__(self,gender):
        self.gender = gender
        
        
    def getGender(self):
        if self.gender == 'M':
            print("Male")
        
        else:
            print("Female")
            
            
c = Child('F')

c.getGender()