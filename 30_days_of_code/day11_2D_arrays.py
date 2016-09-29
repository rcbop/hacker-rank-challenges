#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

max, sum = -9999999,0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j-2>=0 and i-2>=0:
            sum = arr[i][j]+arr[i][j-1]+arr[i][j-2]+arr[i-1][j-1]+arr[i-2][j]+arr[i-2][j-1]+arr[i-2][j-2]
            if sum > max: max = sum

print(max)
