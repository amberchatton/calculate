#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 21:05:19 2023

Program to calculate celsius and meters per second

@author: AmberC
"""

#this is the function that calculates the celsius.
def func1(f):
    c = 0
    c = ((f - 32) * 0.5556)
    return (c)


#this is the function that calculates the meters per second.   
def func2(mph):
    m = 0
    m = (mph * 0.0447038)
    return (m)
    
#this is the main function.
def main():
    print ("Enter 1 to convert Fahrenheit temperature to Celsius")
    print ("Enter 2 to convert speed from miles per hour(MPH) to meters per second(MPS)")
    condition = int(input('Enter your number: '))

    if(condition == 1):
        f = float(input('Enter temperature in fahrenheit: '))
        c = func1(f)
        print('The value of temperature in celcius: ',c)
    elif(condition == 2):
        mph = float(input('Enter speed in mph: '))
        m   = func2(mph)
        print('The value of speed in metres per second: ',m)
    else:
        print('Error, input must be 1 or 2')

#calling the main funciton to execute program.
main()
