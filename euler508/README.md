# Problem #508: Integers in base i-1 

## Problem Statement 

Consider the Gaussian integer i-1. A base i-1 representation of a Gaussian integer a+bi is a finite sequence of digits dn-1dn-2...d1d0 such that:
a+bi = dn-1(i-1)n-1 + dn-2(i-1)n-2 + ... + d1(i-1) + d0
Each dk is in {0,1}
There are no leading zeroes, i.e. dn-1 ≠ 0, unless a+bi is itself 0
Here are base i-1 representations of a few Gaussian integers:
11+24i → 111010110001101
24-11i → 110010110011
8+0i → 111000000
-5+0i → 11001101
0+0i → 0

Remarkably, every Gaussian integer has a unique base i-1 representation!

Define f(a+bi) as the number of 1s in the unique base i-1 representation of a+bi. For example, f(11+24i) = 9 and f(24-11i) = 7.

Define B(L) as the sum of f(a+bi) for all integers a, b such that |a| ≤ L and |b| ≤ L. For example, B(500) = 10795060.

Find B(1015) mod 1 000 000 007.
