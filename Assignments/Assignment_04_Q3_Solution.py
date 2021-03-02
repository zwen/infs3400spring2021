# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:31:53 2021

@author: zwena
"""

import string
import time
import sys

password = "az"
#password = "a#&Jz6!098"
candidate = string.printable
#alternatively, if you have experienced some issues with this candidate, we can limit it to the first 95 characters that are printable.
#candidate = string.printable[0:94]

def check(key):
    if key == password:
        finalize(key)

def finalize(key):
    print(key)
    endTime = time.time()
    print("time to find a match", endTime - startTime)
    sys.exit()



#https://docs.python.org/3/library/string.html

newKey = ""

startTime = time.time()

for i1 in candidate:
    newKey = i1
    check(newKey)

    for i2 in candidate:
        newKey = i1 + i2
        check(newKey)

        for i3 in candidate:
            print(newKey)
            newKey = i1 + i2 + i3
            check(newKey)

            for i4 in candidate:
                newKey = i1 + i2 + i3 + i4
                check(newKey)

                for i5 in candidate:
                    newKey = i1 + i2 + i3 + i4 + i5
                    check(newKey)

                    for i6 in candidate:
                        newKey = i1 + i2 + i3 + i4 + i5 + i6
                        check(newKey)

                        for i7 in candidate:
                            newKey = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            check(newKey)

                            for i8 in candidate:
                                newKey = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
                                check(newKey)

                                for i9 in candidate:
                                    newKey = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9
                                    check(newKey)

                                    for i10 in candidate:
                                        newKey = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10
                                        check(newKey)
