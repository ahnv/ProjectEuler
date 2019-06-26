# Problem #494: Collatz prefix families 

## Problem Statement 


The Collatz sequence is defined as:
$a_{i+1} = \left\{  \large{\frac {a_i} 2 \atop 3 a_i+1} {\text{if }a_i\text{ is even} \atop \text{if }a_i\text{ is odd}} \right.$.


The Collatz conjecture states that starting from any positive integer, the sequence eventually reaches the cycle 1,4,2,1....
We shall define the sequence prefix p(n) for the Collatz sequence starting with a1 = n as the sub-sequence of all numbers not a power of 2 (20=1 is considered a power of 2 for this problem). For example:p(13) = {13, 40, 20, 10, 5} p(8) = {}
Any number invalidating the conjecture would have an infinite length sequence prefix.


Let Sm be the set of all sequence prefixes of length m. Two sequences {a1, a2, ..., am} and {b1, b2, ..., bm} in Sm are said to belong to the same prefix family if ai < aj if and only if bi < bj for all 1 ≤ i,j ≤ m.


For example, in S4, {6, 3, 10, 5} is in the same family as {454, 227, 682, 341}, but not {113, 340, 170, 85}.
Let f(m) be the number of distinct prefix families in Sm.
You are given f(5) = 5, f(10) = 55, f(20) = 6771.


Find f(90).

