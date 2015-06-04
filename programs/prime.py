#!/usr/bin/python

# TO FIND PRIME NUMBERS FROM 2 TO 200

max=50
min=2

for i in range(min,max):
	for j in range(min,i):
		if i%j == 0:
			break
	else:
		print i
