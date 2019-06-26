# Problem #524: First Sort II 

## Problem Statement 

Consider the following algorithm for sorting a list:
1. Starting from the beginning of the list, check each pair of adjacent elements in turn.
2. If the elements are out of order:
a. Move the smallest element of the pair at the beginning of the list.
b. Restart the process from step 1.
3. If all pairs are in order, stop.For example, the list { 4 1 3 2 } is sorted as follows:
4 1 3 2  (4 and 1 are out of order so move 1 to the front of the list)
1 4 3 2  (4 and 3 are out of order so move 3 to the front of the list)
3 1 4 2  (3 and 1 are out of order so move 1 to the front of the list)
1 3 4 2  (4 and 2 are out of order so move 2 to the front of the list)
2 1 3 4  (2 and 1 are out of order so move 1 to the front of the list)
1 2 3 4  (The list is now sorted)Let F(L) be the number of times step 2a is executed to sort list L. For example, F({ 4 1 3 2 }) = 5.
We can list all permutations P of the integers {1, 2, ..., n} in lexicographical order, and assign to each permutation an index In(P) from 1 to n! corresponding to its position in the list.

Let Q(n, k) = min(In(P)) for F(P) = k, the index of the first permutation requiring exactly k steps to sort with First Sort. If there is no permutation for which F(P) = k, then Q(n, k) is undefined.
For n = 4 we have:
PI4(P)F(P){1, 2, 3, 4}10Q(4, 0) = 1{1, 2, 4, 3}24Q(4, 4) = 2{1, 3, 2, 4}32Q(4, 2) = 3{1, 3, 4, 2}42{1, 4, 2, 3}56Q(4, 6) = 5{1, 4, 3, 2}64{2, 1, 3, 4}71Q(4, 1) = 7{2, 1, 4, 3}85Q(4, 5) = 8{2, 3, 1, 4}91{2, 3, 4, 1}101{2, 4, 1, 3}115{2, 4, 3, 1}123Q(4, 3) = 12{3, 1, 2, 4}133{3, 1, 4, 2}143{3, 2, 1, 4}152{3, 2, 4, 1}162{3, 4, 1, 2}173{3, 4, 2, 1}182{4, 1, 2, 3}197Q(4, 7) = 19{4, 1, 3, 2}205{4, 2, 1, 3}216{4, 2, 3, 1}224{4, 3, 1, 2}234{4, 3, 2, 1}243Let R(k) = min(Q(n, k)) over all n for which Q(n, k) is defined.
Find R(1212).
