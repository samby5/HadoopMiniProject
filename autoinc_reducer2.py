#!/usr/bin/env python
import sys
d={}
for line in sys.stdin:
	item = line.split('*')
	k = item[0]
	#print(k)
	if k in d:
		d[k]+=1
	else:
		d[k]=1
print(d)
	
    