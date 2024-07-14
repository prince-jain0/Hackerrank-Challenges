#!/bin/python3

import math
import os
import random
import re
import sys

def unboundedKnapsack(k, arr):
    t = [0] * (k + 1)
    for x in arr:
        for y in range(x, k + 1):
            t[y] = max(t[y], t[y - x] + x)
    return t[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    results = []
    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)
        results.append(result)
    
    for res in results:
        fptr.write(str(res) + '\n')

    fptr.close()
