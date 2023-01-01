# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:06:59 2022

@author: SKUP
"""

import datetime

before = datetime.datetime.now()


for i in range(100):
    x = 1+1
    

after = datetime.datetime.now()

exec_time = after - before

print(exec_time.microseconds)