# Problem #538: Maximum quadrilaterals 

## Problem Statement 

Consider a positive integer sequence S = (s1, s2, ..., sn).
Let f(S) be the perimeter of the maximum-area quadrilateral whose side lengths are 4 elements (si, sj, sk, sl) of S (all i, j, k, l distinct). If there are many quadrilaterals with the same maximum area, then choose the one with the largest perimeter.
For example, if S = (8, 9, 14, 9, 27), then we can take the elements (9, 14, 9, 27) and form an isosceles trapezium with parallel side lengths 14 and 27 and both leg lengths 9. The area of this quadrilateral is 127.611470879... It can be shown that this is the largest area for any quadrilateral that can be formed using side lengths from S. Therefore, f(S) = 9 + 14 + 9 + 27 = 59.
Let un = 2B(3n) + 3B(2n) + B(n+1), where B(k) is the number of 1 bits of k in base 2.
For example, B(6) = 2, B(10) = 2 and B(15) = 4, and u5 = 24 + 32 + 2 = 27.
Also, let Un be the sequence (u1, u2, ..., un).
For example, U10 = (8, 9, 14, 9, 27, 16, 36, 9, 27, 28).
It can be shown that f(U5) = 59, f(U10) = 118, f(U150) = 3223.
It can also be shown that Σ f(Un) = 234761 for 4 ≤ n ≤ 150.
Find Σ f(Un) for 4 ≤ n ≤ 3 000 000.
