#!/bin/python3

import sys

n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    print(len(set(list(s))))
