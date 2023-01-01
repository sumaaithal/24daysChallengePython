# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:03:20 2022

@author: SKUP
"""

"""
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.
You can init an object with construct parameter or set the value later

"""


class myClass:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name,":",self.age)
        
        
c = myClass("suma", 24) 

c.display()    