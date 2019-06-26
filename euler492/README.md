# Problem #492: Exploding sequence 

## Problem Statement 

Define the sequence a1, a2, a3, ... as:
a1 = 1
an+1 = 6an2 + 10an + 3 for n ≥ 1.

Examples:
a3 = 2359
a6 = 269221280981320216750489044576319
a6 mod 1 000 000 007 = 203064689
a100 mod 1 000 000 007 = 456482974


Define B(x,y,n) as ∑ (an mod p) for every prime p such that x ≤ p ≤ x+y.


Examples:
B(109, 103, 103) = 23674718882
B(109, 103, 1015) = 20731563854

Find B(109, 107, 1015).
