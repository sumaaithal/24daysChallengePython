# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:29:47 2022

@author: SKUP
"""

"""
Define a class named Shape and its subclass Square. The Square class has an
 init function which takes a length as argument. Both classes have a area 
 function which can print the area of the shape where Shape's area is 0 by default.

Hints
To override a method in super class, we can define a method with the same 
name in the super class.
"""

class Shape:
    def __init__(self):
        pass
        
    def area(self):
        return 0
        
class Square(Shape):

    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length
        
    def area(self):
        return self.length*self.length
    
s = Square(5)
print(s.area())

sh = Shape()
print(sh.area())
    
    
    
    
