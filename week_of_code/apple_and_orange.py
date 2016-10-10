#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
applesCount = 0
#print(apple, orange)
for i in apple:
    if i>0 and (i+a) >= s and (i+a) <= t:
        applesCount+=1
orangesCount =0
for j in orange:
    if j<0 and (b+j) <= t and (b+j) >= s:
        orangesCount+=1

print(applesCount)
print(orangesCount)
