# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:09:51 2022

@author: SKUP
"""

"""
Define a custom exception class which takes a string message as attribute.

Hints
To define a custom exception, we need to define a class inherited from Exception.
"""

class customException(Exception):
    
    def __init__(self,string) :
        self.string = string
        
    def display(self):
        print(self.string)
        

num = int(input("enter the number:>>"))

try:
    if num<10:
        raise customException("number is less than 10")
    
    elif num>10:
        raise customException("number is greater than 10")

except customException as ce:
    print("error raised:",ce)
    


    

