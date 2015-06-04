#!/usr/bin/python

# SCRIPT TO ACCEPT MIN AND MAX FROM USER AND PRINT PRIME IN THAT RANGE

import sys

total=0

min=int(raw_input("Enter the start number from which prime is needed:"))
if min <= 1:
	print "Wrong input .. please re-run the program"
	sys.exit()

max=int(raw_input("Enter the end number to which prime is needed:"))

for i in range(min,max):
	for j in range(2,i):
		if i%j == 0:
			break
	else:
		print i
		total+=1

print "Total number of primes from " , min , " to " , max , " is " , str(total)

