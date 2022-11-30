---
name: Submit a new problem
about: Propose a new problem for a given test set
title: ''
labels: ''
assignees: ''
---

I propose to add the following problem to the ``<test_set_name>`` test set.

Format:

$$
\begin{split}
\begin{array}{ll}
\mbox{minimize}
    & \frac{1}{2} x^T P x + q^T x \\
\mbox{subject to}
    & G x \leq h \\
    & A x = b \\
    & lb \leq x \leq ub
\end{array}
\end{split}
$$

The problem matrices are:

$$
\begin{split}
\begin{array}{ll}
    P & = ... \\
    q & = ... \\
    G & = ... \\
    h & = ... \\
    A & = ... \\
    b & = ... \\
    lb & = ... \\
    ub & = ...
\end{array}
\end{split}

This problem is interesting because ...
