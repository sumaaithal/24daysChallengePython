# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:00:11 2022

@author: SKUP
"""

"""
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function

Hints:
The built-in document method is __doc__
"""

def square(n):
    """
    returns the square of the number when 'n' is passed inside the funtion
    """
    return n**2

print(square.__doc__)