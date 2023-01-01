# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:14:26 2022

@author: SKUP
"""

"""
You are given a string.Your task is to count the frequency of letters of 
the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde
Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1
Hints
Count frequency with dictionary and sort by Value from dictionary Items
"""

s = input("enter the string:>>")

d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
        
    
temp = sorted(d.items(),key=lambda x:(-x[1],x[0]))

for i in temp:
    print(i[0]+" "+str(i[1]))