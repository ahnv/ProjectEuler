# Problem #531: Chinese leftovers 

## Problem Statement 


Let g(a,n,b,m) be the smallest non-negative solution x to the system:x = a mod nx = b mod m
if such a solution exists, otherwise 0.


E.g. g(2,4,4,6)=10, but g(3,4,4,6)=0.


Let φ(n) be Euler's totient function.


Let f(n,m)=g(φ(n),n,φ(m),m)


Find ∑f(n,m) for 1000000 ≤ n < m < 1005000

