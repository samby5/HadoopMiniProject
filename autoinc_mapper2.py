#!/usr/bin/env python
import sys
nl = ''
for item in sys.stdin:
	nl+=item.strip()+'*'+'1'+'\n'
print(nl.strip())