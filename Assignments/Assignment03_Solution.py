#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:29:56 2021

@author: zwen
"""


userName = "aaron"
password = "4356"

userNamefromInput = "aaron"

msg = "Hi, " + userNamefromInput + ", What is your password? "
promptCount = 0

passwordfromInput = input(msg)


while (passwordfromInput != password) and (promptCount < 3):
    print("Looks like you entered a wrong password, please enter again.")
    passwordfromInput =  input("What is your password: ")
    promptCount += 1
    print(promptCount)    



if promptCount >= 3:
    print("You have used too many attempts. Please call us for login.")
else:
    print("Welcome to the system.")
