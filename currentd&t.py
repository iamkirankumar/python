#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Getting current date and time
"""
Created on Tue Jan 10 16:02:50 2017

@author: Creative
"""
from datetime import datetime
# below command shows whole date and time
now = datetime.now()
print("\n")
print(now)
print("\n")

# getting cammands on date
print("DATE : " + str(now.year)+"/"+str(now.month)+"/"+str(now.day))

# getting commands on time
print("TIME : " + str(now.hour)+":"+str(now.minute)+":"+str(now.second))