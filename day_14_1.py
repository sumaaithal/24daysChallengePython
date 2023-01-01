# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:06:06 2022

@author: SKUP
"""

"""
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints
Use try/except to catch exceptions.
"""

def tryCatchExc():
    try:
        5/0
        
    except ZeroDivisionError :
        print("divide by zero error!")
        
    
tryCatchExc()