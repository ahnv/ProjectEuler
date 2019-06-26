# Problem #553: Power sets of power sets 

## Problem Statement 

Let P(n) be the set of the first n positive integers {1, 2, ..., n}.
Let Q(n) be the set of all the non-empty subsets of P(n).
Let R(n) be the set of all the non-empty subsets of Q(n).
An element X ∈ R(n) is a non-empty subset of Q(n), so it is itself a set.
From X we can construct a graph as follows:
Each element Y ∈ X corresponds to a vertex and labeled with Y;
Two vertices Y1 and Y2 are connected if Y1 ∩ Y2 ≠ ∅.
For example, X = {{1}, {1,2,3}, {3}, {5,6}, {6,7}} results in the following graph:

This graph has two connected components.
Let C(n,k) be the number of elements of R(n) that have exactly k connected components in their graph.
You are given C(2,1) = 6, C(3,1) = 111, C(4,2) = 486, C(100,10) mod 1 000 000 007 = 728209718.
Find C(104,10) mod 1 000 000 007.
