#!/bin/python3
# ------------
# NOT WORKING
# ------------
import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
number = input().strip()
arr = list(number)
no_match = []

for i in range(n//2):
    # store unmatches idx
    if arr[i] != arr[len(arr)-i-1]:
        no_match.append(i)
if (k < len(no_match)):
    print(-1)
else:
    # TODO increase leftmost
    #extra_moves = k - len(no_match)
    #if extra_moves > 0:
        #if extra_moves % 2 == 0:

        #else:

    # this will fix palindrome
    for j in no_match:
        if arr[j] < arr[len(arr)-j-1] and k > 0:
            arr[j] = arr[len(arr)-j-1]
            k-=1
        elif arr[j] > arr[len(arr)-j-1] and k > 0:
            arr[len(arr)-j-1] = arr[j]
            k-=1
    print(''.join(arr))
