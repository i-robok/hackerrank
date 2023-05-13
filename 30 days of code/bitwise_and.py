#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    max_ab = 0

    for a in range(1,N):
        for b in range(a+1,N+1):
            if ((a & b) < K):
                max_ab = max(max_ab, a & b)
                if max_ab == K-1:
                    return max_ab

    return max_ab

def bitwiseAndWhat(N, K):
    if (K | (K - 1)) > N:
        return K - 2
    else:
        return K - 1

if __name__ == '__main__':
    fptr = open('/home/jacuevasp/Learning/HackerRank/30 days of code/input03.txt', 'r')

    t = int(fptr.readline().strip())

    for t_itr in range(t):
        # first_multiple_input = input().rstrip().split()
        first_multiple_input = fptr.readline().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        # res = bitwiseAnd(count, lim)
        res = bitwiseAndWhat(count, lim)

        # fptr.write(str(res) + '\n')
        print(f'{res}')

    fptr.close()
