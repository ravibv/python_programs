#!/usr/bin/python

dict={}
dict['one']="first"
dict['two']="second"

tinydict={'one':1,'two':2,'three':3,'four':4,'five':5}

print dict
print dict['one']
dict['one']="ondu"
print dict['one']

print tinydict['three']
print tinydict.keys()
print tinydict.values()

for i in tinydict.keys():
	print tinydict[i]
