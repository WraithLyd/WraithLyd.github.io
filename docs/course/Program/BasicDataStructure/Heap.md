# 4 Priority Queues(Heaps)
!!! note "ADT"
	Objects: A finite ordered list with zero or more elements.
	
	Operations:

	+ PriorityQueue Initialize(int MaxElements); 
	+ void Insert(ElementType X, PriorityQueue H);
	+ ElementType DeleteMin(PriorityQueue H);
	+ ElementType FindMin(PriorityQueue H); 

## 4.1 Simple Implementations
Linked list is better since there is never more deletions than insertion.

+ Array:
    + Insertion -- add one item at the end ~ $\Theta(1)$
    + Deletion
        + find the largest/smallest key ~ $\Theta(n)$
        + remove the item and shift array ~ $O(n)$
+ Linked List:
    + Insertion -- add to the front of the chain ~ $\Theta(1)$
    + Deletion
        + find the largest/smallest key ~ $\Theta(n)$
        + remove the item ~ $\Theta(1)$
+ Ordered Array:
    + Insertion
        + find the proper position ~ $O(n)$
        + shift array and add the item ~ $O(n)$
    + Deletion -- remove the item ~ $\Theta(1)$
+ Ordered Linked List:
    + Insertion
        + find the proper position ~ $O(n)$
        + add the item ~ $\Theta(1)$
    + Deletion -- remove the first/last item ~ $\Theta(1)$

## 4.2 Binary Heap
### 4.2.1 Structure Property:
A binary tree with $n$ nodes and height $h$ is complete if its nodes correspond(相对应) to the nodes numbered from 1 to $n$ in the perfect binary tree of height $h$.

> A complete binary tree of height $h$ has between $2^h$ and $2^{h+1}-1$ nodes. 
> 
> $h=[logN]$ if logN is not an integer, then h++.

We can use an array `BT[n+1]` to represent it.(BT[0] is not used)

If a complete binary tree with $n$ nodes is represented sequentially, then for any node with index $i$, $0<i<n$, we have:

index of $parent(i) = \left\{
\begin{matrix}
 [\frac{i}{2}]\ \ \  if\ \ i \neq 1 \\
 None\ \ \  if\ \ i=1
\end{matrix}
\right.$

index of $left\_child(i) = \left\{
\begin{matrix}
 2i\ \ \  if\ \ 2i \leq n \\
 None\ \ \  if\ \ 2i \geq n
\end{matrix}
\right.$

index of $right\_child(i) = \left\{
\begin{matrix}
 2i+1\ \ \  if\ \ 2i+1 \leq n \\
 None\ \ \  if\ \ 2i+1 \geq n
\end{matrix}
\right.$

### 4.2.2 Heap Order Property
A **min tree** is a tree in which the key value in each node is no larger than the key values in its children (if any). A **min heap** is a complete binary min tree.

### 4.2.3 Basic Heap Operations
#### 4.2.3.1 Insertion
The possible position for a new node is only since a heap must be a complete binary tree.

```c
/*H->Elements[0] is a sentinel*/
void Insert(ElementType X, PriorityQueue H)
{
	int i;
	if(IsFull(H))
	{
		Error("Priority queue is full");
		return;
	}
	for( i=++H->Size; H->Elements[i/2]; i/=2)
		H->Elements[i] = H->Elements[i/2];
	H->Elements[i]=X;
}
```
T(N)=O(log N)
#### 4.2.3.2 DeleteMin

```c
ElementType DeleteMin(PriorityQueue H)
{
	/*Percolate Down*/
	int i, Child;

	ElementType MinElement, LastElement;
	if(IsEmpty(H))
	{
		Error("Priority queue is empty");
		return H->Elements[0];
	}
	MinElement=H->Elements[1];
	LastElement=H->Elements[H->Size--];
	for(i=1;i*2<=H->Size;i=Child)
	{
		Child=i*2;
		if(Child!=H->Size && H->Elements[Child+1]<H->Elements[Child])
			Child++;
		if(LastElement>H->Elements[Child])
			H->Elements[i]=H->Elements[Child];
		else
			break;
	}
	H->Elements[i]=LastElement;
	return MinElement;
}
```
T(N)=O(log N)

#### 4.2.3.3 Other Heap Operations
Finding any key except the minimum one will have to take a linear scan through the entire heap.

##### 4.2.3.3.1 DecreaseKey(P,$\Delta$,H)
> Percolate up

##### 4.2.3.3.2 IncreaseKey(P,$\Delta$,H)
> Percolate down

##### 4.2.3.3.3 Delete(P,H)
DecreaseKey(P,$\infty$,H);DeleteMin(H)

##### 4.2.3.3.4 BuildHeap(H)

N successive Insertions
> Time complexity is too low.

First, use the keys build a complete binary tree. Then, percolate down from the last parent node in $h-1$ height.
Considering the worst case, the times of percolating down is the sum of height of each node. $sum=\displaystyle \sum^h_{i=0}(h-i)\times 2^i$

!!! note
	[Theorem] For the prefect binary tree of height $h$ containing $2^{h+1}-1$ nodes, the sum of heights of the nodes is $2^{h+1}-1-(h+1)$

	T(N) = O(N)

## 4.3 d-Heaps

> All nodes have $d$ children.

+ Shall we make $d$ as large as possible?
+ DeleteMin will take $d-1$ comparsions to find the smallest child. Hence the total time complexity would be $O(d\ log_dN)$
+ $*2$ or $/2$ is merely **a bit shift**, but $*d$ or $/d$ is not.
+ When the prtority queue is too large to fit entirely in main memory, a d-heap will become interesting.