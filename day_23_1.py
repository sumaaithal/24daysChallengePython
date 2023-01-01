# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:37:43 2022

@author: SKUP
"""

"""
Given the participants' score sheet for your University Sports Day,
 you are required to find the runner-up score. You are given scores. 
 Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5
Then, the output of the program should be:

5
Hints
Make the scores unique and then find 2nd best number
"""

s = input("enter the scores").split(" ")

num_list = []
for i in s:
    num_list.append(int(i))
    
unique_num = list(set(num_list))

print(unique_num[-2])

