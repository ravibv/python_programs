#!/usr/bin/python

# TO READ DOB, DOA FILE AND ALERT ON DAY.

with open('dob_list.txt') as f:
	lines = f.read().splitlines()

print lines
