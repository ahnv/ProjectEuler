#!/bin/python3

import sys
from operator import mul
from functools import reduce 


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    num = str(num)
    prod = []
    for i in range(0,n-k+1):
        tmp = num[i:i+k]
        tmp = list(tmp)
        tmp = [ int(x) for x in tmp ]
        p = reduce(mul, tmp, 1)
        prod.append(p)
    print(max(prod))
