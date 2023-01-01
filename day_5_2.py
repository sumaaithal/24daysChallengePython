# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:05:56 2022

@author: SKUP
"""
"""
Write a program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown as 
following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
"""
amount = 0 

while True:
    
    a = input("enter the input W/D amount: >>").split(" ")
    
    if a[0] == 'D':
        
        amount+=int(a[1])
        
    
    elif a[0] == 'W':
        
        amount-=int(a[1])
        
        if amount < 100:
            print("you've reached maximum limit as the balance is low")
            
    elif a[0] == '':
        print("total amount in bank {}".format(amount))
        break
    
    
            
            
            
    