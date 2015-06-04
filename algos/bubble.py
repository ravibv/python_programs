#!/usr/bin/python

orig=[30,1,-3,50,2,43,322,12,42,21,76]

print "Before: Orig: ", orig

for j in range(len(orig)):
	for i in (range(len(orig)-1-j)):
		if orig[i]>orig[i+1]:
			orig[i],orig[i+1]=orig[i+1],orig[i]

print "After: Orig: ", orig
