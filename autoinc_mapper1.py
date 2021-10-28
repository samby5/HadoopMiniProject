#!/usr/bin/env python
import sys

for line in sys.stdin:
    #print(line)
    #l = line.strip()
    l = line.split(',')
    k=l[2]
    v=l[1]+ '-'+l[3]+'-'+l[5]
    print('{0}\t{1}'.format(k,v))