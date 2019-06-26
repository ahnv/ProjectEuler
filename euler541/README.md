# Problem #541: Divisibility of Harmonic Number Denominators 

## Problem Statement 

The nthharmonic number Hn is defined as the sum of the multiplicative inverses of the first n positive integers, and can be written as a reduced fraction an/bn.
$H_n = \displaystyle \sum_{k=1}^n \frac 1 k = \frac {a_n} {b_n}$, with $\text {gcd}(a_n, b_n)=1$.
Let M(p) be the largest value of n such that bn is not divisible by p.
For example, M(3) = 68 because $H_{68} = \frac {a_{68}} {b_{68}} = \frac {14094018321907827923954201611} {2933773379069966367528193600}$, b68=2933773379069966367528193600 is not divisible by 3, but all larger harmonic numbers have denominators divisible by 3.
You are given M(7) = 719102.
Find M(137).
