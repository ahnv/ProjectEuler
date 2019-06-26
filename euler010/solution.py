#!/bin/python3

import sys
from bisect import bisect

def SieveOfEratosthenes(n): 
      
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        if (prime[p] == True): 
              
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    l = [i for i in range(len(prime)) if prime[i] is True]
    l = l[2:]
    return l

t = int(input().strip())
primes = SieveOfEratosthenes(1000000)
for a0 in range(t):
    n = int(input().strip())
    ind = bisect(primes,n)
    s = sum(primes[:ind])
    print(s)
    