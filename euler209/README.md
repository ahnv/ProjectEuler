# Problem #209: Circular Logic 

## Problem Statement 

A k-input binary truth table is a map from k input bits
(binary digits, 0 [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth tables for the logical AND and XOR functions are:

x
y
x AND y000010100111

x
y
x XOR y000011101110
How many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0
for all 6-bit inputs (a, b, c, d, e, f)?

