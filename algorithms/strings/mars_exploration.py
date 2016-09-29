#!/bin/python3

import sys
a = input().strip()
b ="SOS"*(len(a)//3)
print(sum ( a[i] != b[i] for i in range(len(a)) ))
