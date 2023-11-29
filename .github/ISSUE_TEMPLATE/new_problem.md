---
name: Submit a new problem
about: Propose a new problem for the GitHub-FFA test set
title: ''
labels: ''
assignees: ''
---

### Problem

I propose to add the following problem to the *GitHub free-for-all* test set.
The problem can be built and tested as follows:

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

### Parameter range

<!--
    If the problem has parameters, explain what their sensible values are.
-->

### Motivation

This problem is interesting because...

### Solution and optimal cost

<!--
    If you know a formula for the solution of the problem, or the optimal cost,
    write them down here. This is not a requirement but it can help us debug
    solver outputs later on.
-->

- Solution: $x^\* = ...$
- Optimal cost: $\frac12 x^{\*T} P x^\* + q^T x^\* = ...$

### References

<!--
    If the problem arose in a specific context, such as an engineering problem
    or a research paper, put the relevant references here.
-->

1. Foo Bar *et al.*, "...", 2022.
