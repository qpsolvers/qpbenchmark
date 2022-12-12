---
name: Submit a new problem
about: Propose a new problem for a given test set
title: ''
labels: ''
assignees: ''
---

I propose to add the following problem to the GitHub free-for-all (``github_ffa``) test set. The problem can be constructed and solved as follows:

```python
import numpy as np
from qpsolvers import solve_qp

P = ...
q = ...
G = ...
h = ...
A = ...
b = ...
lb = ...
ub = ...

x = solve_qp(P, q, G, h, A, b, lb, ub, solver="...")
```

### Motivation

This problem is interesting because...

### Solution

The solution $x^\*$ to this problem is...

### References

See also...
