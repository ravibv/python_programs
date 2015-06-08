#!/usr/bin/python

mystring="Python"
mylist=[1,2,3,4,5,6]
mytuple=(1,2,3,4,5,6)
mydict={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}

print "string loop.."
for i in mystring:
	print i,

print "\n"

print "list loop.."
for i in mylist:
	print i

print "tuple loop.."
for i in mytuple:
	print i

print "dictionary loop.."
for i in mydict.keys():
	print mydict[i]

print "done"
