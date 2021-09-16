# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:11:54 2021

@author: Himanshu Savargaonkar

Purpose: Test if detect.py can run as a module and can produce required output 
when called from a different python code.
"""

import detect

#Each single param can be modified from the call below


#Video 
#detect.run(source = "Second.mp4", classes=17)

#Single Image
detect.run(source = "Me.jpeg", classes=0)

print("Hello World")

