# Problem #443: GCD sequence 

## Problem Statement 

Let g(n) be a sequence defined as follows:
g(4) = 13,
g(n) = g(n-1) + gcd(n, g(n-1)) for n > 4.
The first few values are:

n4567891011121314151617181920...
g(n)1314161718272829303132333451545560...

You are given that g(1 000) = 2524 and g(1 000 000) = 2624152.
Find g(1015).
