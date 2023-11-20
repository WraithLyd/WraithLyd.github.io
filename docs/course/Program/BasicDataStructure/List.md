# 2 Lists, Stacks and Queues
## 2.1 Abstract Data Type(ADT)
Data type={Objects} $\cup$ {Operations}

> For example, int = {0, 1, -1, ..., INT_MAX, INT_MIN} $\cup$ {+, -, *, /, %, ...}

Definition: An Abstract Data Type(ADT) is a data type that is organized in such a way that the specification(规范) on the objects and specification of the operations on the objects are separated from the representation(表示) of the objects and the implementation(实现) on the operations.
## 2.2 The List ADT
!!! note "ADT"
	Objects: (item 0, item 1, item 2, ..., item N-1)

	Operations: 

	+ Find the length, N, of a list.
	+ Printing all the items in a list
	+ Making an empty list
	+ Finding the k-th item from a list
	+ Inserting a new item after the k-th item of a list
	+ Deleting an item from a list
	+ Finding next of the current item from a list
	+ Finding previous of the current item from a list

### 2.2.1 Simple Array implementation of Lists
!!! hint "implementation"
	array[i]=item i

+ **MaxSize** has to be estimated.
+ **Find_Kth** takes O(1) time.
+ **Insertion** and **Deletion** not only take O(N) time, but also involve a lot of data movements which takes time.

### 2.2.2 Linked List
!!! hint "implementation"
	```c linenums='1'
	typedef struct list_node *list_ptr;
	typedef struct list_node{
		char data[4];
		list_ptr next
	}
	list_ptr ptr;
	```
#### 2.2.2.1 Onsertion
Insertion takes O(1) time.
```c
/*Insert temp after node in the list*/
temp->next=node->next;
node->next=temp;
```
#### 2.2.2.2 Deletion
Deletion takes O(1) time.
```c linenums='1'
/*Delete node*/
pre->next=node->next;
free(node);
```
#### 2.2.2.3 Find
Find takes O(N) time.

### 2.2.3 Doubly Linked Lists
!!! hint "implementation"
	```c linenums='1'
	typedef struct node *node_ptr;
	typedef struct node{
		node_ptr llink;
		element item;
		node_ptr rlink;
	};
	```
### 2.2.4 Circular Lists
The data structure is the same as Linked List. But circular list links head and tail.
A empty list is:
```c linenums='1'
node->llink=node;
node->rlink=node;
```
### 2.2.5 Cursor Implementation Linked List
The data are stored in a collection of structurees. Each structure contains data and a pointer to the next structure. A `int` type cursor can point the data you want, instead of the list pointer.

A new structure can be obtained from the system's global memory by a call to `malloc` and released by a call to `free`.

As a result of lack of memory management routines, The cursor implementation is faster than other linked list.

## 2.3 The Stack ADT

A stack is a Last-In-First-Out list, that is, an ordered list in which insertions and deletions are made at the top only.

!!! note "ADT"
	Objects: A finite ordered list with zero or more elements.

	Operations: 
	
	+ int IsEmpty(stack S)
	+ stack CreateStack()
	+ DisposeStack(stack S)
	+ MakeEmpty(stack S)
	+ **Push**(ElementType X, stack S)
	+ ElementType **Top**(stack)
	+ **Pop**(stack S)

### 2.3.1 Linked List Implementation (with a header node)

#### 2.3.1.1 Push
```c linenums='1'
TmpCell->Next = S->Next;
S->Next = TmpCell;
```
#### 2.3.1.2 Top
```c linenums='1'
return S->Next->Element;
```
#### 2.3.1.3 Pop
```c linenums='1'
FirstCell = S->Next;
S->Next = S->Next->Next;
free(FirstCell);
```
### 2.3.2 Array Implementation
```c linenums='1'
struct StackRecord{
	int Capacity;	/*size of stack*/
	int TopOfStack;	/*the top pointer*/
	/*++ for push, --for pop, -1 for empty stack*/
	ElementType *Array;/*array for stack elements*/
}
```
## 2.4 The Queue ADT
A queue is a First-In-First-Out (FIFO) list, that is, an ordered list in which insertions take place at one end and deletions take place at the opposite end.

!!! note "ADT"
	Objects: A finite ordered list with zero or more elements.

	Operations: 

	+ int IsEmpty(queue Q)
	+ queue CreateQueue()
	+ DisposeQueue(queue Q)
	+ MakeEmpty(queue Q)
	+ Enqueue(ELementType X, queue Q)
	+ ElementType Front(queue Q)
	+ Dequeue(queue Q)

### 2.4.1 Array Implementation
```c linenums='1'
struct QueueRecord{
	int Capacity;	/*max size of queue*/
	int Front;		/*the front pointer*/
	int Rear;			/*the rear pointer*/
	int Size;			/*Optional - the current size of queue*/
	ElementType *Array;	/*array for queue elements*/
}
```