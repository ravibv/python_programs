#!/usr/bin/python

seq=['1','2','3','4','5','6']

sep='* '

print sep.join(seq)

##############

dirs = '','usr','bin','env'
sep='/'
print sep.join(dirs)

type(dirs)
dir=list(dirs) # CONVERT TO LIST
print dir
dir.remove('') # REMOVE THE STARTING '', THIS WILL KNOCK OFF THE STARTING / IN NEXT LINE
print dir
sep.join(dir)
