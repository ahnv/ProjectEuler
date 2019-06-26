# Problem #499: St. Petersburg Lottery 

## Problem Statement 

A gambler decides to participate in a special lottery. In this lottery the gambler plays a series of one or more games.
Each game costs m pounds to play and starts with an initial pot of 1 pound. The gambler flips an unbiased coin. Every time a head appears, the pot is doubled and the gambler continues. When a tail appears, the game ends and the gambler collects the current value of the pot. The gambler is certain to win at least 1 pound, the starting value of the pot, at the cost of m pounds, the initial fee.
The gambler cannot continue to play if his fortune falls below m pounds.
Let pm(s) denote the probability that the gambler will never run out of money in this lottery given his initial fortune s and the cost per game m.
For example p2(2) ≈ 0.2522, p2(5) ≈ 0.6873 and p6(10 000) ≈ 0.9952 (note: pm(s) = 0 for s < m).
Find p15(109) and give your answer rounded to 7 decimal places behind the decimal point in the form 0.abcdefg.
