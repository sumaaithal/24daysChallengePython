# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:10:52 2022

@author: SKUP
"""

"""
You are given words. Some words may repeat. For each word, output its 
number of occurrences. The output order should correspond with the input 
order of appearance of the word. See the sample input/output for clarification.

If the following string is given as input to the program:

4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:

3
2 1 1
Hints
Make a list to get the input order and a dictionary to count the word frequency
"""

s = input("enter the string:>> ").split(",")

d = {}

for i in s:
    if i not in d:
        d[i]=1
    
    else:
        d[i]+=1
        

for k,v in d.items():
    print(v,end=" ")

