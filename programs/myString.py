#!/usr/bin/python


first = "hi, %s" % raw_input("Enter name: ")
second = "the date today is: %d" % int(raw_input("Enter number: "))

print first, second

########### PI ###########

format  = "pi, with 3 decimals; %.3f" 

import math

print format % math.pi
