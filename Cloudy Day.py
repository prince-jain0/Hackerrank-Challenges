#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#
def maximumPeople(p, x, y, r):
    x, p = zip(*sorted(zip(x, p)))
    not_visited=[i for i in range(len(y))]
    not_visited.sort(key=lambda x: y[x] - r[x])
    to_visit=[]
    sum_sunny=dict()
    max_pop=sum(p)
    cloud_pop=[0]*len(y)
    idx_x=0
    while idx_x < len(x):
        pos=x[idx_x]
        population=p[idx_x]
        j=0
        while j < len(not_visited):
            element = not_visited[j]
            if y[element] - r[element] <= pos:
                to_visit.append((element, y[element]+r[element]))
                del not_visited[j]
            else:
                break
        j=0
        to_check=None
        while j < len(to_visit):
            element, max_pos = to_visit[j]
            if max_pos - pos >= 0:
                to_check=element
                if idx_x not in sum_sunny:
                    sum_sunny[idx_x]=population
                else:
                    to_check=None
                    break
                j+=1
            else:
                del to_visit[j]
        idx_x+=1
        if to_check is not None:
            cloud_pop[to_check]+=population
    for pop in sum_sunny.values():
            max_pop-=pop
    return max(cloud_pop) + max_pop
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
