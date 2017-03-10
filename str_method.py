#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#String Method or Funtions
"""
Created on Tue Jan 10 12:00:25 2017

@author: Creative
"""
# len() function means length. Which shows the length
state = "Kiran Kumar want to be expert in data sciecne"
k = len(state)
print(k)

# lower() function which convert all string in lower case, it only works with string
name = "Kiran Kumar".lower()
print(name)

# or we can write in this way
kiran = "Kumar"
print(kiran.lower())


# upper() function which convert all string in upper case, it only works with string
thing = "htc desire".upper()
print(thing)

# str() function which turns non-string into string
price = str(12)
print(price)

# string formatting with +
print("Hello this is " + "Python " + "and it is used from 1989")