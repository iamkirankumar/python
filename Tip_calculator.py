#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Tip Calculator
"""
Created on Tue Jan 10 12:31:21 2017

@author: Creative
"""

meal = 44.50
tax = 6.75
tip = 15

#calculation
rt = meal*tax/100
t = meal*tip/100
ob = meal + rt + t

print("Overall cost of the meal (including tax) = " + str(ob))