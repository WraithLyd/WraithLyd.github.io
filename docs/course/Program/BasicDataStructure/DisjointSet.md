# 5 The Disjoint Set ADT
## 5.1 Equivalence relations
A relation $R$ is defined on a set $S$ if for every pair of elements (a, b), $a, b\in S$, a R b is either true or false.  If a R b is true, then we say that a is related to b.

A relation, ~, over a set, S, is said to be an equivalence(等价) relation over S if it is symmetric(对称), reflexive(反身), and transitive(传递) over S.

Two members x and y of a set S are said to be in the same equivalence class(等价类) if x ~ y.

## 5.2 The Dynamic Equivalence Problem

Given an equivalence relation ~, decide for any a and b if a ~ b.

+ Elements of the sets:  1, 2, 3, ..., N
+ Sets :  S1, S2, ... ...  and  $S_i\cap S_j = \phi$  ( if $i \neq j$) —— disjoint
+ Operations
    + Union(i, j) ::= Replace $S_i$ and $S_j$ by $S = S_i\cupS_j$
    + Find(i) ::= Find the set $S_k$ which contains the element i.