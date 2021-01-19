#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:55:11 2021

@author: zwen
"""

#Print the first program
print("hello, world!")


#Import time library to experiment time related functions.
import time

#Return the current time as seconds in GMT time zone. (time since 1970, January 01)
print(time.time())

#Concatenating three parameters
print("Since 1970, Jan 01 until now:", time.time(), "seconds have passed.")

#A short program that converts the time stamp into the current local time.
currentTime = time.time()
print("Local time is", time.ctime(currentTime))
