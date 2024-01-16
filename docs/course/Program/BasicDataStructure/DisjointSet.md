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
    + Union(i, j) ::= Replace $S_i$ and $S_j$ by $S = S_i\cup S_j$
    + Find(i) ::= Find the set $S_k$ which contains the element i.

## 5.3 Basic Data Structure
### Implementation of Disjoint Set

```c
ElementType S[number];
S[root] = 0;
S[element] = the index of the element's parent;
```

### Union(i,j)

Idea: Make $S_i$ a subtree of $S_j$ or vice versa. That is, we can set the parent pointer of one of the roots to the other root.

Implementation:

```c
void SetUnion(DisjSet S, SetType Rtt1, SetType Rt2)
{
	S[Rt2] = Rt1;
}
```

### Find(i)

Idea: Find the parent of element by set and judge if the parent element is root. If not, find its parent continuously.

Implementation:

```c
SetType Find(ElementType X, DisjSet S)
{
	for(;S[X]>0;X=S[X]);
	return X;
}
```

## 5.4 Smart Union Algorithms - Union-by-Rank

### Union by Size

Always change the smaller tree. The algorithm needs a variable store the size of the set. We choose to store the size in S[root]. S[root] will be initialized to be -1 and subtract 1 while an element is linked with the set. Therefore, the element is a root while S[element] < 0. Besides, the opposite number of S[root] is the size of the set.

### Union by Height

Always change the shallow tree. Other is similar with Union-by-Size.

An algorithm for Union-by-Rank is below.

```c
void SetUnion(DisjSet S, SetType Root1, SetRoot Root2)
{
	if(S[Root2] < S[Root1])
		S[Root1] = S[Root2];
	else
	{
		if(S[Root2] == S[Root1])
			S[Root1]--;
		S[Root2] = S[Root1];
	}
}
```

## 5.5 Path Compression

```c
SetType Find(ElementType X, DisjSet S)
{
	ElementType root, trail, lead;
	for(root = X; S[root] > 0; root = S[root]);/*Find the root*/
	for(trail = X; trail != root; trail = lead)
	{
		lead = S[trail];
		S[trail] = root;
	}
}
```

Another algorithm in textbook is below.

```c
SetType Find(ElementType X, DisjSet S)
{
	if(S[X] <= 0)
		return X;
	else
		return S[X] = Find(S[X], S);
}
```

## 5.6 Worse Case for Union-by-Rank and Path Compression

Let T( M, N ) be the maximum time required to process an intermixed sequence of M (M >= N) finds and N - 1 unions.

**Tarjan Lemma** is below for some positive constants $k_1$ and $k_2$.

$$k1M \alpha ( M, N )\leq T( M, N ) \leq k2M \alpha ( M, N )$$

!!! hint Ackermann’s Function and  ( M, N )
	$A(1,j) = 2^j\ ( j\geq 1)$
	
	$A(i,1) = A(i-1,2)\ (i\geq 2)$
	
	$A(i,j) = A(i-1,A(i,j-1))\ (i\geq 2, j\geq 2)$

	For this, we define **inverse Ackermann function**:

	$\alpha(M,N) = \min\{i\geq1|A(i,[M/N])>\log N\}$

	For example, $ \min\{i\geq1|A(i,[M/N])>\log N\}\leq O(\log^*N)\leq 4$. Since $\log\log\log\log\log(2^{65536})=1$, $\log^*2^{65536}=5$.