#!/usr/bin/env python
import sys
dm={}
da=''
for line in sys.stdin:
	item=line.split('\t')
	val=item[1].split('-')
	#print(val)
	if item[0] not in dm:
		dm[item[0]]=val
	if val[0] == 'A':
		#print(item[0])
		da+=dm[item[0]][1]+dm[item[0]][2].strip()+'\n'
print(da.strip())
#sys.stdout.write(str(da))
		
	
    