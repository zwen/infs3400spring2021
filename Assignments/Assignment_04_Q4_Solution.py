# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:23:14 2021

@author: zwena
"""

userName = "aaron"
password = "4356"

userNamefromInput = "aaron"

msg = "Hi, " + userNamefromInput + ", What is your password? "
promptCount = 0

passwordfromInput = input(msg)

#Adding this part to the original code -->   and (passwordfromInput != "king")

while (passwordfromInput != password) and (promptCount < 3) and (passwordfromInput != "king"):
    print("Looks like you entered a wrong password, please enter again.")
    passwordfromInput =  input("What is your password: ")
    promptCount += 1
    print(promptCount)



if promptCount >= 3:
    print("You have used too many attempts. Please call us for login.")
else:
    print("Welcome to the system.")