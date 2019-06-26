#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    r = 0
    for i in range(999,99, -1):
        for j in range(999,i, -1):
            prod = i * j
            if (r < prod and prod < n and str(prod) == str(prod)[::-1]):
                r = prod
                break
            elif (prod < r):
                break
    print(r)
