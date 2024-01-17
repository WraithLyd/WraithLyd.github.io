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

### 6.3.1 Breadth-first search(for Unweighted Shortest Paths)

BFS implementation is below:

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

### 6.3.2 Dijkstra’s Algorithm (for Weighted Shortest Paths)
#### Data Structure

Let `S` = { s and vi’s whose shortest paths have been found }

For any $u\in S$,  define `distance[u]` = minimal length of path $\{s,\dots,(v_i\in S ),\dots,u\}$. If the paths are generated in non-decreasing order.

#### Algorithm
The shortest path must go through ONLY $v_i\in S$;

u is chosen so that distance[u] = $\min\{ w\in S|distance[w]\}$  (If u is not unique, then we may select any of them) ;  /* Greedy Method */

If `distance[u1] < distance[u2]` and we add u1 into S, then distance[u2] may change. If so, a shorter path from s to u2 must go through u1 and `distance[u2] = distance[u1] + length`(length means the weight< u1, u2>).

```c
void Dijkstra( Table T )
{   /* T is initialized by Figure 9.30 on p.303 */
Vertex  V, W;
while(){
	V = smallest unknown distance vertex;
	if ( V == NotAVertex )
		break; 
	T[ V ].Known = true;
	for ( each W adjacent to V )
		if ( !T[ W ].Known )
			if ( T[ V ].Dist + Cvw < T[ W ].Dist ) {
				Decrease( T[ W ].Dist to [ V ].Dist + Cvw );// update distance
				T[ W ].Path = V;
			} /* end-if update W */
	} /* end-while*/
}
```

### 6.3.3 SPFA(for Graphs with Negative Edge Costs)

```c
void  WeightedNegative( Table T )
{   /* T is initialized by Figure 9.30 on p.303 */
	Queue  Q;
	Vertex  V, W;
	Q = CreateQueue (NumVertex );
	MakeEmpty( Q );
	Enqueue( S, Q ); /* Enqueue the source vertex */
	while ( !IsEmpty( Q ) ) {
		V = Dequeue( Q );
		for ( each W adjacent to V )
			if ( T[ V ].Dist + Cvw < T[ W ].Dist ) {
				T[ W ].Dist = T[ V ].Dist + Cvw;
				T[ W ].Path = V;
				if ( W is not already in Q )Enqueue( W, Q );
			} /* end-if update */
	} /* end-while */DisposeQueue( Q ); /* free memory */
}/* negative-cost cycle will cause indefinite loop */
```

## 6.4 AOE(Activity On Edge) Network
### Definitions
EC[j] / LC[j] is the **earliest / latest completion time** for node $v_j$.

The weight of edge is **lasting time**, which means the subtract of LC and EC. 

**Slack time** is the maximum delay in implementation. 

**Critical path** is a path consisting entirely of zero-slack edges.

### Calculations

EC: $EC[w]=\max_{<v,w>∈E}\{EC[v]+C_{v,w}\}$

LC: $LC[w]=\min_{<v,w>∈E}\{LC[v]-C_{v,w}\}$

Lasting time: $Lasting Time[v,w] = weight<v,w>$

Slack Time: $SlackTime<v,w>=LC[w]−EC[v]−C_{v,w}$

## 6.5 Network Flow Problems

The simple algorithm of network flow is below(s is the source while t is the sink. Gf means flow graph while Gr means residual graph):

+  Find any path s->t in Gr
+  Take the minimum edge on this path as the amount of flow and add to Gf;
+  Update Grand remove the 0 flow edges;
+   If (there is a path s->t in Gr ) Go to Step 1;Else End.

In a word, the flow on the augmenting path is the minimum edge right on the augmenting path, creating such a flow and updating the residual graph until the augmenting path is not found.

Analysis: $T=O(|E|^2|V|)$

## 6.6 Minimum Spanning Tree

A spanning tree of a graph G is a tree which consists of V(G) and a subset of E(G).

!!! hint
	+ The minimum spinning tree is a tree since it's acyclic. The number of edges is |V|-1.
	+ It's minimum for the total cost of edges is minimized.
	+ It's spanning because it covers  every vertex.
	+ A minimum spannning tree exists if and only if G is connected.
	+ Adding a non-tree edge to a spinning tree, we obtain a cycle.

### Greedy Method
Make the best decision for each stage, under the following constrains:

+ we must use only edges within the graph
+ we must use exactly |V|-1 edges
+ we may not use edges that would produce a cycle

#### Prim's Algorithm

Idea: we define two vertex sets, linked with the tree and unlinked with the tree. In the beginning, all of the vertex are in unlinked set. First, we choose the minimum weight edge and add in linked vertex set. Then through interating the remaining vertex, choose the minimum weight edge that links the vertex and the tree. At the end of traversal, the minimum spinning tree is built.

#### Kruskal's Algorithm

Idea: in Kruskal's Algorithm, we sort the edges by weight first. Following the order, we judge whether tree have a loop after adding the new edge. If no loop, add the edge in MST. Otherwise, discard the edge and try next edge. After judging all of the edge, MST is finished.

In Kruskal's Algorithm, we need to judge whether addition of a edge can lead a generation of loop. We can transform it into whether the two vertexs of edge have the same ancestor. It can use disjoint set to solve.

## 6.7 Depth-First Search
### Implementation
```c
void DFS ( Vertex V )  /* this is only a template */
{   
	visited[ V ] = true;  /* mark this vertex to avoid cycles */
	for ( each W adjacent to V )
		if ( !visited[ W ] )
			DFS( W );
} 
```

### 6.7.1 Biconnectivity

`v` is an **articulation point**(割点) if G’ = DeleteVertex( G, v ) has at least 2 connected components.

G is a **biconnected**(双连通) graph if G is connected and has no artculation points.

A **biconnected component**(双连通分量) is a maximal biconnected subgraph.

####  Tarjan's Algorithm
u is an articulation point iff(1)  u is the root and has at least 2 children;

u is not the root, and has at least 1 child such that Low(child) <= Num(u).

### 6.7.2 Euler Circuits
#### Description
**Euler tour**: Draw each line exactly once without lifting your pen from the paper.

**Euler curcuit**: Draw each line exactly once without lifting your pen from the paper, AND finish at the starting point.

#### Prerequisite
##### Undirected Graphs
An undirected graph G has an **Euler curcuit** if and only if G is connected and each vertex has even degree.
Undirected graph G has **Euler tour** if and only if G is connected and if and only if two vertices have odd degrees.

##### Directed graph
Directed graph G has **Euler circuit** if and only if G is weakly connected and each vertex has out-degree equal to in-degree.
Directed graph G has **Euler tour** if and only if G is weakly connected and there is and only one vertex whose out-degree is greater than the in-degree by 1, and there is and only one vertex whose in-degree is greater than the out-degree by 1, and the rest of the vertices whose out-degree is equal to the in-degree.

