# Problem #652: Distinct values of a proto-logarithmic function 

## Problem Statement 

Consider the values of $\log_2(8)$, $\text{log}_4(64)$ and $\text{log}_3(27)$. All three are equal to $3$.
Generally, the function $f(m,n)=\text{log}_m(n)$ over integers $m,n \ge 2$ has the property that 
$f(m_1,n_1)=f(m_2,n_2)$ if
$\, m_1=a^e, n_1=a^f, m_2=b^e,n_2=b^f \,$ for some integers $a,b,e,f \, \,$ or 
 $ \, m_1=a^e, n_1=b^e, m_2=a^f,n_2=b^f \,$ for some integers $a,b,e,f \,$ We call a function $g(m,n)$ over integers $m,n \ge 2$ proto-logarithmic  if 
$\quad  \, \, \, \, g(m_1,n_1)=g(m_2,n_2)$ if any integers $a,b,e,f$ fulfilling 1. or 2. can be found 
and $\, g(m_1,n_1) \ne g(m_2,n_2)$ if no integers $a,b,e,f$ fulfilling 1. or 2. can be found
Let $D(N)$ be the number of distinct values that any proto-logarithmic function $g(m,n)$ attains over $2\le m, n\le N$.
For example, $D(5)=13$, $D(10)=69$, $D(100)=9607$ and $D(10000)=99959605$.
Find $D(10^{18})$, and give the last 9 digits as answer.
Note: According to the four exponentials conjecture the function $\text{log}_m(n)$ is proto-logarithmic. While this conjecture is yet unproven in general, $\text{log}_m(n)$ can be used to calculate $D(N)$ for small values of $N$.
