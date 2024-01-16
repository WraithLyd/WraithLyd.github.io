# 6 Graph
## 6.1 Definitions
### G(V,E)
where  **G**::=graph, **V=V(G)**::=finite nonempty set of vertices, and **E=E(G)**::=finite set of edges.
### Undirected graph
Each edge is a pair `(v,w)`. If the pair is disordered, then the graph is a **undirected graph**. For edges in undirected graph, `(vi,vj)=(vj,vi)`.
### Directed graph (digraph)
If the pair is ordered, then the graph is a **directed graph**. For edges in directed graph, `<tail,head>`::= tail->head, `<vi,vj>!=<vj,vi>`.

**Restrictions**:

+ Self loop is illegal.
+ Multigraph is not considered.

### Complete graph
**Complete graph** is a graph which there is an edge between every pair of vertices.
### Adjacent(邻近的)
In an undirected graph, `v` and `w` are adjacent for a edge `(v,w)`. 

In a directed graph, v is adjacent to w while w is adjacent from v for a edge `<v,w>`.

### Subgraph
For a new graph G', if $V(G')\subseteq V(G)$ and $E(G')\subseteq E(G)$, G' is a subset of G.

### Path
A **path** in a graph is a sequence of vertices $v_1$,$v_2$,$v_3$,...,$v_N$ while $(v_i,v_i+1)\in E$ for $1\leq i<N$. **The length of a path** is the number of edges on the path. For the example above, its length is N-1.

### Simple Path
A simple path is a path such that all vertices are distinct(不重复).

### Cycle
A cycle in direct graph is a path that begin is the same as end. If the path is simple, the cycle is simple.

For undirected graph, we require that the edges are distinct(simple path).

### Connected
#### In undirected graph
`v` and `w` in an undirected G are connected if there is a path from `v` to `w`(and hence there is also a path from `v` to `w`).

An undirected graph G is connected if every pair of distinct `v` and `w` are connected.

**Connected component of an undirected graph** is the maximal connected subgraph. 
#### In directed graph
For every pair of `v` and `w`, if there exist directed paths from `v` to `w` and from `w` to `v`, the graph is **strongly connected**.

If the graph is connected without direction to the edges, then it is said to be **weakly connected**.

**Strongly connected component** is the maximal subgraph that is strongly connected.

### Degree
Degree of `v` is number of edges incident to `v`.  For a directed G, we have in-degree and out-degree. 

!!! tip
	A tree is a graph that is connected and acyclic.

### Adjacency Matrix

For each edge `(u,v)`, we set `A[u][v]=1`. Otherwise the entry in the array is 0. If the edge has a weight associated with it, we can set`` A[u][v]` equal to weight. For example,

$$adj\_mat[3][3]=\left[\begin{matrix}
0&1&0\\
1&0&1\\
0&0&0\\
\end{matrix}\right]$$

### Adjacency Lists
If we replace each row by a linked list in adjacency martix, there's adjacency lists. For the example above, 

```c
graph[0]->data = 1;
graph[1]->data = 0;
graph[1]->next->data = 2;
graph[2] = NULL;
```

!!! note
	The order of nodes in each list does not matter.

For undirected G:S = `n`heads+`2e`nodes = `(n+2e)`ptrs+`2e`ints.

### Adjacency Multilists

## 6.2  Topological Sort(拓扑排序)

### 6.2.1 AOV Network
**AOV network** is a digraph G in which V(G) represents activities and E(G) represents precedence(优先级) relations.

`i` is a **predecessor**(前驱) of `j` if there's a path from `i` to `j`.

`i` is an **immediate predecessor** of `j` if $<i,j>\in E(G)$. Then `j` is called a **successor**(**immediate successor**) of `i`.

!!! hint
	Feasible(可行的) AOV network must be a **DAG**(directed acyclic graph).

### 6.2.2 Topological Order
A topological order is a linear ordering of the vertices of a graph such that, for any two vertices, `i`, `j`, if `i` is a predecessor of `j` in the network then `i` precedes `j` in the linear ordering.

```c
void Topsort( Graph G )
{   
	Queue  Q;
	int  Counter = 0;
	Vertex  V, W;
	Q = CreateQueue( NumVertex );  
	MakeEmpty( Q );
	for ( each vertex V )
		if ( Indegree[ V ] == 0 )   Enqueue( V, Q );
	while ( !IsEmpty( Q ) ) 
	{
		V = Dequeue( Q );
		TopNum[ V ] = ++ Counter; /* assign next */
		for ( each W adjacent to V )
			if ( – – Indegree[ W ] == 0 )  
				Enqueue( W, Q );
	}  /* end-while */
	if ( Counter != NumVertex )
		Error( “Graph has a cycle” );
	DisposeQueue( Q ); /* free memory */
}
```

## 6.3 Shortest Path Algorithms
Given a digraph G = (V,E), and a cost function `c(e)` for $e\in E(G)$. The length of a path `P` from source to destination is $\displaystyle\sum_{e\in E(G)}c(e_i)$(also called weighted path length).

### 6.3.1 Unweighted Shortest Paths - BFS

Breadth-first search implementation is below:

```c
Table[i].Dist ::= distance from s to vi/* initialized to be infty except for s */
Table[i].Known ::= 1 if vi is checked; or 0 if not
Table[i].Path ::= for tracking the path   /* initialized to be 0 */
```

```c
void Unweighted( Table T )
{   
	int  CurrDist;
	Vertex  V, W;
	for ( CurrDist = 0; CurrDist < NumVertex; CurrDist ++ ) {
		for ( each vertex V )
			if ( !T[ V ].Known && T[ V ].Dist == CurrDist ) {
				T[ V ].Known = true;
				for ( each W adjacent to V )
					if ( T[ W ].Dist == Infinity ) {
						T[ W ].Dist = CurrDist + 1;
						T[ W ].Path = V;
					} /* end-if Dist == Infinity */
			} /* end-if !Known && Dist == CurrDist */
	}  /* end-for CurrDist */
}
```

