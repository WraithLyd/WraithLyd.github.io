# 3 Trees
## 3.1  Terminology
A tree is a collection of nodes. The collection can be empty. Otherwise, a tree consists of: 

+ a distinguished node `r`, called the root;
+ zero or more nonempty (sub)trees T1,... Tk, each of whose roots are connected by a directed edge from `r`.

!!! note
	+ Every node in the tree is the root of some subtree.
	+ There are N-1 edges in a tree with N nodes.
	+ Normally the root is drawn at the top.

#### 3.1.1 degree of a node
Number of subtrees of the node.

#### 3.1.2 degree of a tree
The maximum among degrees of all nodes in the tree.

#### 3.1.3 parent
A node that has subtrees.

#### 3.1.4 children
The roots of the subtrees of a parent.

#### 3.1.5 siblings
Children of the same parent.

#### 3.1.6 leaf(terminal node)
A node with degree 0.

#### 3.1.7 path from n1 to nk
A (unique) sequence of nodes $n_1$, $n_2$,...,$n_k$ such that $n_i$ is the parent of $n_{i+1}$

#### 3.1.8 length of path
Number of edges on the path.

#### 3.1.9 depth of $n_i$
Length of the unique path from the root to $n_i$.

depth(root)=0

#### 3.1.10 height of $n_i$
Length of the longest path from $n_i$ to a leaf.

height(leaf)=0

#### 3.1.11 height(depth) of a tree

Equal to height(root) and depth(deepest leaf).

#### 3.1.12 ancestors of a node
All the nodes along the path from the node up to the root.

#### 3.1.13 descendants of a node
All the nodes in its subtrees.

## 3.2 Implementation - List representation
```c linenums='1'
typedef struct *node node_ptr;
typedef struct node{
	ElementType value;
	node_ptr child1;
	node_ptr child2;
	...
}
```
The number of children is unclear, so we select **FirstChild-NextSibling Representation** to translate the tree into a **binary tree**.

```c linenums='1'
typedef struct *node node_ptr;
typedef struct node{
	ElementType value;
	node_ptr FirstChild;
	node_ptr NextSibling;
}
```

## 3.3 Binary Tree
### 3.3.1 Introduction
A binary tree is a tree in which no node can have more than two children.

```c linenums='1'
typedef struct *node node_ptr;
typedef struct node{
	ElementType value;
	node_ptr Left;
	node_ptr Right;
}
```
### 3.3.2 Tree Traversal
#### 3.3.2.1 Preorder Traversal
Access the current node first and then access the left and right child as follow.

```c linenums='1'
void  preorder(tree_ptr tree)
{
	if(tree)
	{
		visit(tree);
		for(each child C of tree )
			preorder(C);
	}
}
```
#### 3.3.2.2 Postorder Traversal
Access the left and right child first and then access the current node as follow.

```c linenums='1'
void postorder(tree_ptr tree)
{
	if(tree)
	{
		for(each child C of tree)
			postorder(C);
		visit(tree);
	}
}
```
#### 3.3.2.3 Levelorder Traversal
Put the root into a empty queue. Then insert its children into the queue, and the node dequeues. Then follow the order inqueue the first node's children and dequeue the node.

```c linenums='1'
void levelorder(tree_ptr tree)
{
	enqueue(tree);
	while (queue is not empty)
	{
		visit(T=dequeue( ));
		for (each child C of T)
			enqueue ( C );
	}
}
```
#### 3.3.2.4 Inorder Traversal
Access the left child first and then access the current node, access the right child at last as follow.

```c linenums='1'
void inorder(tree_ptr tree)
{  
	if(tree)   
	{
		inorder(tree->Left);
		visit(tree->Element);
		inorder(tree->Right);
	}
}
```
### 3.3.3 Threaded Binary Trees
Rule 1: If Tree->Left is null, replace it with a pointer to the inorder predecessor of Tree.(The predecessor of the first leaf node is head node)

Rule 2: If Tree->Right is null, replace it with a pointer to the inorder successor of Tree.

Rule 3: There must not be any loose threads. Therefore, a threaded binary tree must have a head node of which the left child points to the first node.

```c linenums='1'
typedef struct ThreadedTreeNode *PtrTo ThreadedNode;
typedef struct PtrToThreadedNode ThreadedTree;
typedef struct ThreadedTreeNode
{
	int LeftThread;		/* if it is TRUE, then Left */
	ThreadedTree Left;/* is a thread, not a child ptr. */
	ElementType Element;
	int RightThread;	/* if it is TRUE, then Right */
	ThreadedTree  Right;    /* is a thread, not a child ptr.   */
}
```
### 3.3.4 Properties of Binary Trees(二叉线索树)
The maximum number of nodes on level i is $2^{i-1}$, $i\geq 1$.

The maximum number of nodes in a binary tree of depth k is $2^k-1$, $k\geq 1$.

For any nonempty binary tree, $n_0 = n_2 + 1$ where $n_0$ is the number of leaf nodes and $n_2$ the number of nodes of degree 2.

## 3.4 The Search Tree ADT - Binary Search Trees
### 3.4.1 Definition
A binary search tree is a binary tree. It may be empty. If it is not empty, it satisfies the following properties:

+ Every node has a key which is an integer, and the keys are distinct.
+ The keys in a nonempty left subtree must be smaller than the key in the root of the subtree.
+ The keys in a nonempty right subtree must be larger than the key in the root of the subtree.
+ The left and right subtrees are also binary search trees.

!!! note "ADT"
	Objects: A finite ordered list with zero or more elements.

	Operations:

	+ SearchTree MakeEmpty(SearchTree T);
	+ Position Find(ElementType X, SearchTree T);
	+ Position FindMin(SearchTree T);
	+ Position FindMax(SearchTree T);
	+ SearchTree Insert(ElementType X, SearchTree T);
	+ SearchTree Delete(ElementType X, SearchTree T);
	+ ElementType Retrieve(Position P);

### 3.4.2 Implementation
#### 3.4.2.1 Insert
+ check if the element is already in the tree.
+ compare the element and nodes in the tree.

```c linenums='1'
// insert X into Search Tree T
SearchTree Insert(ElementType X, SearchTree T)
{
	if(T==NULL)
	{
		/* Create and return a one-node tree */
		T=malloc(sizeof(struct TreeNode));
		if(T == NULL) 
			FatalError("Out of space!!!");
		else 
		{
			T->Element = X; 
			T->Left = T->Right = NULL; 
		} 
	}/* End creating a one-node tree */
	else/* If there is a tree */
		if(X < T->Element) 
			T->Left = Insert(X, T->Left); 
		else if(X > T->Element) 
			T->Right = Insert(X, T->Right); 
		/* Else X is in the tree already; we'll do nothing */
		return T;   /* Do not forget this line!! */}
```

#### 3.4.2.2 Delete
Delete a leaf node: Replace the node with NULL.

Delete a degree 1 node: Replace the node with its child.

Delete a degree 2 node: 

+ Replace the node by the largest one in its left subtree or the smallest one in its right subtree.
+ Delete the replacing node from the subtree.

```c
SearchTree Delete(ElementType X, SearchTree T)
{    
	Position TmpCell;
	if(T == NULL)   
		Error("Element not found");
	else if(X < T->Element)/* Go left */
		T->Left = Delete(X, T->Left);
	else if(X > T->Element)/* Go right */
		T->Right = Delete(X, T->Right);
	else/* Found element to be deleted */
		if (T->Left && T->Right)
		{
			/* Two children */
			/* Replace with smallest in right subtree */
			TmpCell = FindMin(T->Right);
			T->Element = TmpCell->Element;
			T->Right = Delete(T->Element, T->Right);  
		}/* End if */
		else{
			/* One or zero child */
			TmpCell = T;
			if(T->Left == NULL)/* Also handles 0 child */
				T = T->Right;
			else if(T->Right == NULL)
				T = T->Left;
			free(TmpCell);
	  }  /* End else 1 or 0 child */
	return  T;
}
```

