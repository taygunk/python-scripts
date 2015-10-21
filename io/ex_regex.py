# -*- coding: utf-8 -*-

#Python Reg-Ex examples

import re

# Find a substring starting with '*'
line = 'This is a *good day *to die'
p = re.compile(r'\*\w+')
result = p.search(line)
print(result.group())

# Find multiple substrings starting with '*'
result = p.findall(line)
print(result)

#Remove * from elems of list
result = [s.strip('*') for s in result]