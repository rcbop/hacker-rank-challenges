#!/bin/python3

import re

N = int(input().strip())
pattern = re.compile(r'.*@gmail.com')
nameList = []

for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    search = pattern.search(emailID)
    if search is not None:
        nameList.append(firstName)

print("\n".join(sorted(nameList)))
