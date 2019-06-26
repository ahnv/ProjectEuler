# Problem #556: Squarefree Gaussian Integers 

## Problem Statement 

A Gaussian integer is a number z = a + bi where a, b are integers and i2 = -1.
Gaussian integers are a subset of the complex numbers, and the integers are the subset of Gaussian integers for which b = 0.
A Gaussian integer unit is one for which a2 + b2 = 1, i.e. one of 1, i, -1, -i.
Let's define a proper Gaussian integer as one for which a > 0 and b ≥ 0.
A Gaussian integer z1 = a1 + b1i is said to be divisible by z2 = a2 + b2i if z3 = a3 + b3i = z1/z2 is a Gaussian integer.
$\frac {z_1} {z_2} = \frac {a_1 + b_1 i} {a_2 + b_2 i} = \frac {(a_1 + b_1 i)(a_2 - b_2 i)} {(a_2 + b_2 i)(a_2 - b_2 i)} = \frac {a_1 a_2 + b_1 b_2} {a_2^2 + b_2^2} + \frac  {a_2 b_1 - a_1 b_2}  {a_2^2 + b_2^2}i = a_3 + b_3 i$
So, z1 is divisible by z2 if $\frac {a_1 a_2 + b_1 b_2} {a_2^2 + b_2^2}$ and $\frac  {a_2 b_1 - a_1 b_2}  {a_2^2 + b_2^2}$ are integers.
For example, 2 is divisible by 1 + i because 2/(1 + i) = 1 - i is a Gaussian integer.
A Gaussian prime is a Gaussian integer that is divisible only by a unit, itself or itself times a unit.
For example, 1 + 2i is a Gaussian prime, because it is only divisible by 1, i, -1, -i, 1 + 2i, i(1 + 2i) = i - 2, -(1 + 2i) = -1 - 2i and -i(1 + 2i) = 2 - i.
2 is not a Gaussian prime as it is divisible by 1 + i.
A Gaussian integer can be uniquely factored as the product of a unit and proper Gaussian primes.
For example 2 = -i(1 + i)2 and 1 + 3i = (1 + i)(2 + i).
A Gaussian integer is said to be squarefree if its prime factorization does not contain repeated proper Gaussian primes.
So 2 is not squarefree over the Gaussian integers, but 1 + 3i is.
Units and Gaussian primes are squarefree by definition.
Let f(n) be the count of proper squarefree Gaussian integers with a2 + b2 ≤ n.
For example f(10) = 7 because 1, 1 + i, 1 + 2i, 1 + 3i = (1 + i)(2 + i), 2 + i, 3 and 3 + i = -i(1 + i)(1 + 2i) are squarefree, while 2 = -i(1 + i)2 and 2 + 2i = -i(1 + i)3 are not.
You are given f(102) = 54, f(104) = 5218 and f(108) = 52126906.
Find f(1014).
