#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = sum([1 for i in [int(apple_temp) for apple_temp in input().strip().split(' ')] if i>0 and (i+a) >= s and (i+a) <= t], 0)
orange = sum([1 for j in [int(orange_temp) for orange_temp in input().strip().split(' ')] if j<0 and (b+j) <= t and (b+j) >= s], 0)

print(apple)
print(orange)
