
# These are not total solutions. But they are complete enough to give you a clear idea how to get things work. I have dicussed the problem-solving logic during 02/11 class.


# approach 1. Loop through until find a match
import sys

password = "mz"

# This code only cracks two-character password, to crack a longer length password, you need to implement for layers of loop. 

candidate = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()~`-_=+\|<>,.:;"'/?'
key = ""

while key != password:
    for i in range(len(candidate)):
        for j in range(len(candidate)):
            key = candidate[i] + candidate[j]
            if key == password:
                print(key)
                sys.exit()    #It interrupts the entire program as soon as a match is found.


# approach 2. Build a dictionary, then find a match from dictionary

dictionary = []   #This is a dictionary (a list) that will contain all the possible permutations.

for i in range(len(candidate)):
    for j in range(len(candidate)):
        for k in range(len(candidate)):
            for l in range(len(candidate)):
                newKey = candidate[i] + candidate[j] + candidate[k] + candidate[l]
                dictionary.append(newKey)

#I did not complete the rest. But it is clear that you will be looping through the dictionary to find a match. 
