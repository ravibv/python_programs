#!/usr/bin/python

# TO REMIND THE DOB AND DOA

people = {
	'Ravi' : {
		'phone':'26682223',
		'addr':'BTM'
	},	

	'Vilaas' : {
		'phone':'1234',
		'addr':'Kengeri'
	},

	'Harish': {
		'phone':'5678',
		'addr':'Arekere' 
	}
}

# LABELS, FOR OUTPUT
labels = {
	'phone': 'Phone number',
	'addr': 'Address'
}

# GET THE INPUT NAME	
name = raw_input("Enter name: ")

# GET IF YOU NEED THE PHONE NUMBER OR ADDRESS
request = raw_input("Do you want the phone number (p) or address(a): ")

if request.lower() == 'p':
	key = 'phone'
if request.lower() == 'a':
	key = 'addr'

if name in people:
	print "%s's %s is %s" % (name, labels[key], people[name][key])
