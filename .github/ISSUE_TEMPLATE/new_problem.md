---
name: Submit a new problem
about: Propose a new problem for a given test set
title: ''
labels: ''
assignees: ''
---

I propose to add the following problem to the ``<test_set_name>`` test set.

The problem can be constructed as follows:

```python
def get_problem():
    return Problem(
        P=[...],
        q=[...],
        G=[...],
        h=[...],
        A=[...],
        b=[...],
        lb=[...],
        ub=[...],
        name="...",
        optimal_cost=[...],
    )
```

This problem is interesting because ...
