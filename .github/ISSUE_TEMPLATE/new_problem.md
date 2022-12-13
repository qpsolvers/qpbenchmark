---
name: Submit a new problem
about: Propose a new problem for a given test set
title: ''
labels: ''
assignees: ''
---

I propose to add the following problem to the GitHub free-for-all (``github_ffa``) test set. The problem can be built and tested as follows:

```python
import numpy as np
from qpsolvers import solve_qp

def build_problem():  # add parameters if applicable
    P = ...
    q = ...
    G = ...
    h = ...
    A = ...
    b = ...
    lb = ...
    ub = ...
    return P, q, G, h, A, b, lb, ub

if __name__ == "__main__":
    args = build_problem()
    x = solve_qp(*args, solver="...")
```

### Motivation

This problem is interesting because...

### Solution

The solution $x^\*$ to this problem is...

### References

See also...
