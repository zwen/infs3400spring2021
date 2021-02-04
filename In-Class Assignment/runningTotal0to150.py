#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:18:52 2021

@author: zwen
"""

#While look approach to obtain the running total from 1 to 150.


#Variables need to be created before they are being used. 
total = 0
i = 0 

while i < 151:
    total += i
    #make sure the following line is must included when you write a white loop. (You can try to run it with or without the line see what is the difference.)
    i += 1

print(total)