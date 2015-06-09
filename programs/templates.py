#!/usr/bin/python

from string import Template

s = Template("Hi $x, how are you")
name=raw_input("Enter name ")

myString=s.substitute(x=name)

print myString
