# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import string 
import time

password = "az6k"

candidate = string.ascii_letters + string.digits
#https://docs.python.org/3/library/string.html
dictionary = []

startTime = time.time()
for i in range(len(candidate)):
    for j in range(len(candidate)):
        for k in range(len(candidate)):
            for l in range(len(candidate)):
                newKey = candidate[i] + candidate[j] + candidate[k] + candidate[l]
                dictionary.append(newKey)


for i in range(len(dictionary)):
    if dictionary[i] == password:
        key = dictionary[i]
        print(i)
        break

endingTime = time.time()

totalTime = endingTime - startTime 
print(key)
print("time spent", totalTime, "seconds")
