# Problem #326: Modulo Summations 

## Problem Statement 


Let $a_n$ be a sequence recursively defined by:$\quad a_1=1,\quad\displaystyle a_n=\biggl(\sum_{k=1}^{n-1}k\cdot a_k\biggr)\bmod n$.


So the first 10 elements of $a_n$ are: 1,1,0,3,0,3,5,4,1,9.

Let f(N,M) represent the number of pairs (p,q) such that: 

$$
\def\htmltext#1{\style{font-family:inherit;}{\text{#1}}}
1\le p\le q\le N \quad\htmltext{and}\quad\biggl(\sum_{i=p}^qa_i\biggr)\bmod M=0
$$


It can be seen that f(10,10)=4 with the pairs (3,3), (5,5), (7,9) and (9,10).


You are also given that f(104,103)=97158.

Find f(1012,106).

