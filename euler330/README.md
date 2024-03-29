# Problem #330: Euler's Number 

## Problem Statement 

An infinite sequence of real numbers a(n) is defined for all integers n as follows:
$$a(n) = \begin{cases}
1 & n \lt 0\\
\sum \limits_{i = 1}^{\infty}{\dfrac{a(n - i)}{i!}} & n \ge 0
\end{cases}$$

For example,a(0) = 
11!
+
12!
+
13!
+ ... = e − 1 
a(1) = 
e − 11!
+
12!
+
13!
+ ... = 2e − 3 
a(2) = 
2e − 31!
+
e − 12!
+
13!
+ ... =
72
e − 6 

with e = 2.7182818... being Euler's constant.


It can be shown that a(n) is of the form 
    
A(n) e + B(n)n!
for integers A(n) and B(n). 
    
For example a(10) = 
    
328161643 e − 65269448610!
.

Find A(109) + B(109) and give your answer mod 77 777 777.

