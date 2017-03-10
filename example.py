#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# let us consider an example of clinic to understand Condition and control flow
"""
Created on Tue Jan 10 16:15:35 2017

@author: Creative
"""

# here we define the function of clinic

def clinic():
    print("You have just entered the clinic !")
    print("Do you take the door on left or right !")
    # taking input from th user
    answer = input("Type left or right and hit enter : ").lower()
    # now user response stored in answer
    
    # now have to use if, elif and else statement
    if answer=="left":
        print("This is verbal room!")
    elif answer=="right":
        print("This is argument room!")
    else:
        print("Invalid input....TRY_AGAIN!")
        clinic()
clinic()

# Symbols that is predefined in python
# == that is equal to
# != that is not equal to
# < that is less than
# <= that is less or equal to
# > that is greater than 
# >= that is greater than or equal to