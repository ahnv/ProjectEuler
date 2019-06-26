# Problem #535: Fractal Sequence 

## Problem Statement 

Consider the infinite integer sequence S starting with:S = 1, 1, 2, 1, 3, 2, 4, 1, 5, 3, 6, 2, 7, 8, 4, 9, 1, 10, 11, 5, ...
Circle the first occurrence of each integer.S = ①, 1, ②, 1, ③, 2, ④, 1, ⑤, 3, ⑥, 2, ⑦, ⑧, 4, ⑨, 1, ⑩, ⑪, 5, ...
The sequence is characterized by the following properties:
The circled numbers are consecutive integers starting with 1.
Immediately preceding each non-circled numbers ai, there are exactly ⌊√ai⌋ adjacent circled numbers, where ⌊⌋ is the floor function.
If we remove all circled numbers, the remaining numbers form a sequence identical to S, so S is a fractal sequence.Let T(n) be the sum of the first n elements of the sequence.
You are given T(1) = 1, T(20) = 86, T(103) = 364089 and T(109) = 498676527978348241.
Find T(1018). Give the last 9 digits of your answer.
