# Maros Meszaros problem files

These files originate from [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark/blob/86780921f82d5c7c04a8bddb66b03c85a1a1fbb8/problem_classes/maros_meszaros_data). They were converted to the MAT format from the Maros and Meszaros SIF problem files. See the original repository for conversion details.

All problems have the form:
```
minimize        0.5 x' P x + q' x + r
subject to      l <= A x <= u
```

where $x \in \mathbb{R}^n$ is the optimization variable. The objective function is defined by a positive semidefinite matrix $P \in \mathbb{S}^n_+$, a vector $q \in \mathbb{R}^n$ and a scalar $r \in R$. The linear constraints are defined by matrix $A \in \mathbb{R}^{m \times n}$ and vectors $l \in \mathbb{R}^m \cup \{-\infty\}^m$, $u \in \mathbb{R}^m \cup \{+\infty\}^m$.
