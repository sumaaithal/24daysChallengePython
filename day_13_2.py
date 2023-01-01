# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:27:17 2022

@author: SKUP
"""

"""
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.
"""

class Rectangle:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    
    def area(self):
        return self.length*self.width
    
    
r = Rectangle(10, 5)

print(r.area())