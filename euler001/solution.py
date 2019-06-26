#!/bin/python3

import sys

def sum(n,k):
    n = n - 1
    d = n // k
    return k * (d * (d+1)) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(n,3) + sum(n,5) - sum(n,15))