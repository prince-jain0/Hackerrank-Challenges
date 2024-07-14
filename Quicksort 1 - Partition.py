#!/bin/python3

import math
import os
import random
import re
import sys

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    for i in arr:
        if  i < pivot:
            left.append(i)
        if i > pivot:
            right.append(i)
    
    return quickSort(left) + [pivot] + quickSort(right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
