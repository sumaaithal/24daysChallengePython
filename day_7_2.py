# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:40:37 2022

@author: SKUP
"""

"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:

2
"""
import math
res = [] 
pos = [0,0]

while True:
    s = input().split(" ")
    if s[0] == '':
        break
    
    res.append(tuple(s))
    

for i in res:
    if i[0] == 'UP':
        pos[1]+=int(i[1])
    elif i[0] == 'DOWN':
        pos[1]-=int(i[1])
    elif i[0] == 'LEFT':
        pos[0]-=int(i[1])
    elif i[0] == 'RIGHT':
        pos[0]+=int(i[1])
    else:
        pass
print(round(math.sqrt(pos[0]**2 + pos[1]**2)))
        
    
    
    