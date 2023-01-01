# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:20:46 2022

@author: SKUP
"""

"""
Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.

Hints
Use def methodName(self) to define a method.

"""

class Circle:
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius
        
    
    def area(self):
        return self.PI*(self.radius**2)
    
    

c = Circle(5)

print(c.area())
    
    
    