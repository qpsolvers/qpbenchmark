---
name: Submit a new problem
about: Propose a new problem for the GitHub-FFA test set
title: ''
labels: ''
assignees: ''
---

### Problem

I propose to add the following problem to the *GitHub free-for-all* test set. The problem can be built and tested as follows:

```python
import numpy as np
from qpsolvers import solve_qp

def build_problem():  # add parameters if applicable
    # Cost: x^T P x + q^T x
    P = ...
    q = ...

    # Inequality constraints: G x <= h
    G = ...
    h = ...

    # Equality constraints: A x == b
    A = ...
    b = ...

    # Box constraints: lb <= x <= ub
    lb = ...
    ub = ...
    return P, q, G, h, A, b, lb, ub

if __name__ == "__main__":
    args = build_problem()
    x = solve_qp(*args, solver="...")
```

### Context

<!--
    Context around this problem: how did it arise? Why is it interesting to add
    it to the benchmark?
-->

This problem is interesting because...

### Solution

<!--
    If you know a formula for the solution of the problem, you can write it
    down here. This is not a requirement but it can help us debug solver
    outputs later on.
-->

The solution to this problem is:

```math
\begin{align*}
x^\* & = ... \\
y^\* & = ... \\
z^\* & = ... \\
z_{\mathit{box}}^\* & = ... \\
\end{align*}
```

where $x^\*$ is the primal vector, $y^\*$ the dual vector for equality constraints, $z^\*$ the dual vector for inequality constraints, and $z_{\mathit{box}}^\*$ the dual vector for box constraints.

### References

<!--
    If the problem arose in a specific context, such as an engineering problem
    or a research paper, put the relevant references here.
-->

1. Foo Bar *et al.*, "...", 2022.
