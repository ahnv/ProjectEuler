#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n / i
            if n == 3 or n == 5  or n == 7:
                break
        i = i + 1
    print(int(n))
    