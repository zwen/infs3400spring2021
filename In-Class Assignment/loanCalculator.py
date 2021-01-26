#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:32 2021

@author: zwen
"""

#in-class assignment 01 - 01/25/2021 loan calculator 


#I am doing this intentionally to show you what a constant is.
MONTH = 12

#Getting input
loanAmount = eval(input("What is your loan amount: "))
monthlyInterestRate = eval(input("What is the interest rate: ")) / MONTH
numberOfYears = eval(input("What is the duration in years: "))


#for the convenience of coding (so that your code is actually readable...)
numerator = loanAmount * monthlyInterestRate
denominatorPart1 = (1 + monthlyInterestRate) ** (numberOfYears * MONTH)


#For the final answers
monthlyPayment = numerator / (1 - 1/denominatorPart1)

totalPayment = monthlyPayment * MONTH * numberOfYears

print("monthly payment is :", monthlyPayment)

print("total payment is :", totalPayment)


