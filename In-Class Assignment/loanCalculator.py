#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:08:32 2021

@author: zwen
"""

#in-class assignment 01 - 01/25/2021 loan calculator 



loanAmount = eval(input("What is your loan amount: "))
monthlyInterestRate = eval(input("What is the interest rate: ")) / 12
numberOfYears = eval(input("What is the duration in years: "))
MONTH = 12


#for the convenience of coding (so that your code is actually readable...)
numerator = loanAmount * monthlyInterestRate
denominatorPart1 = (1 + monthlyInterestRate) ** (numberOfYears * 12)

monthlyPayment = numerator / (1 - 1/denominatorPart1)

totalPayment = monthlyPayment * MONTH * numberOfYears

print("monthly payment is :", monthlyPayment)

print("total payment is :", totalPayment)


monthlyinterestrate = float((input("Enter the monthly interest rate: ")))
loanamount = int((input("Enter the loan amount: ")))
numberofyears = int((input("Enter the amount of years for the loan:")))


monthlypayment = ((loanamount*monthlyinterestrate)/(1-(1/((1+monthlyinterestrate)**(numberofyears*12)))))

 
print(monthlypayment)