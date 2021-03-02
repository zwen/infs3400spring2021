# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:52:59 2021

@author: zwena
"""


import string 
import time
import os
import pandas as pd

# Return current working directory
os.getcwd()

# Change current working directory
os.chdir("d:/")

password = "&z6!"

candidate = string.printable
#https://docs.python.org/3/library/string.html
dictionary = []

startTime = time.time()
for i in range(len(candidate)):
    for j in range(len(candidate)):
        for k in range(len(candidate)):
            for l in range(len(candidate)):
                newKey = candidate[i] + candidate[j] + candidate[k] + candidate[l]
                dictionary.append(newKey)

searchStartTime = time.time()
for i in range(len(dictionary)):
    if dictionary[i] == password:
        key = dictionary[i]
        print(i)
        break

searchEndingTime = time.time()

endingTime = time.time()

totalTime = endingTime - startTime 
searchTime = searchEndingTime - searchStartTime

print(key)
print("time spent", totalTime, "seconds")
print("time used for search", searchTime, "seconds")

dictionaryFile = pd.DataFrame(dictionary)
dictionaryFile.to_csv("dictionary4letters.csv")
#To test repeatedly, use del dictionary to remove dictionary list to free up memory. 

x = time.time()
ll = 'a' + 'b'
y = time.time()
print(y-x)


