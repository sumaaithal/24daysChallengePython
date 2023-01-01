# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:12:03 2022

@author: SKUP
"""

"""
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checkin
At least 1 letter between [A-Z]
At least 1 character from [$#@]g the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1

"""
import re

s = input("enter the series of passwords:>>").split(",")

lst = []
count = 0

for e in s:
    count+= bool(len(e)>=6 and len(e)<=12)
    count+= bool(re.search(r"[A-Z]", e))
    count+= bool(re.search(r"[$#@]", e))
    count+= bool(re.search(r"[a-z]", e))
    count+= bool(re.search(r"[0-9]", e))
    
    if count == 5:
        lst.append(e)

print(lst)



