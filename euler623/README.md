# Problem #623: Lambda Count 

## Problem Statement 

The lambda-calculus is a universal model of computation at the core of functional programming languages. It is based on lambda-terms, a minimal programming language featuring only function definitions, function calls and variables. Lambda-terms are built according to the following rules:
Any variable $x$ (single letter, from some infinite alphabet) is a lambda-term.
If $M$ and $N$ are lambda-terms, then $(M N)$ is a lambda-term, called the application of $M$ to $N$.
If $x$ is a variable and $M$ is a term, then $(\lambda x. M)$ is a lambda-term, called an abstraction. An abstraction defines an anonymous function, taking $x$ as parameter and sending back $M$.
A lambda-term $T$ is said to be closed if for all variables $x$, all occurrences of $x$ within $T$ are contained within some abstraction $(\lambda x. M)$ in $T$. The smallest such abstraction is said to bind the occurrence of the variable $x$. In other words, a lambda-term is closed if all its variables are bound to parameters of enclosing functions definitions. For example, the term $(\lambda x. x)$ is closed, while the term $(\lambda x. (x y))$ is not because $y$ is not bound.
Also, we can rename variables as long as no binding abstraction changes. This means that $(\lambda x. x)$ and $(\lambda y. y)$ should be considered equivalent since we merely renamed a parameter. Two terms equivalent modulo such renaming are called $\alpha$-equivalent. Note that $(\lambda x. (\lambda y. (x y)))$ and $(\lambda x. (\lambda x. (x x)))$ are not $\alpha$-equivalent, since the abstraction binding the first variable was the outer one and becomes the inner one. However, $(\lambda x. (\lambda y. (x y)))$ and $(\lambda y. (\lambda x. (y x)))$ are $\alpha$-equivalent.
The following table regroups the lambda-terms that can be written with at most $15$ symbols, symbols being parenthesis, $\lambda$, dot and variables.

\[\begin{array}{|c|c|c|c|}
\hline
(\lambda x.x) & (\lambda x.(x x)) & (\lambda x.(\lambda y.x)) & (\lambda x.(\lambda y.y)) \\
\hline
(\lambda x.(x (x x))) & (\lambda x.((x x) x)) & (\lambda x.(\lambda y.(x x))) & (\lambda x.(\lambda y.(x y))) \\
\hline
(\lambda x.(\lambda y.(y x))) & (\lambda x.(\lambda y.(y y))) & (\lambda x.(x (\lambda y.x))) & (\lambda x.(x (\lambda y.y))) \\
\hline
(\lambda x.((\lambda y.x) x)) & (\lambda x.((\lambda y.y) x)) & ((\lambda x.x) (\lambda x.x)) & (\lambda x.(x (x (x x)))) \\
\hline
(\lambda x.(x ((x x) x))) & (\lambda x.((x x) (x x))) & (\lambda x.((x (x x)) x)) & (\lambda x.(((x x) x) x)) \\
\hline
\end{array}\]

Let be $\Lambda(n)$ the number of distinct closed lambda-terms that can be written using at most $n$ symbols, where terms that are $\alpha$-equivalent to one another should be counted only once. You are given that $\Lambda(6) = 1$, $\Lambda(9) = 2$, $\Lambda(15) = 20$ and $\Lambda(35) = 3166438$.
Find $\Lambda(2000)$. Give the answer modulo $1\,000\,000\,007$.
