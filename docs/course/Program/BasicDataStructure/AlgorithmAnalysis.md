# 1. Algorithm Analysis
## 1.1 Algorithm Definition
A algorithm must satisfy:

+ Input: There are zero or more quantities that are externally supplied.
+ Output: At least one quantity is produced.
+ Definiteness: Each instruction is **clear and unambiguous**.
+ Finiteness: If we trace out the instructions of a algorithm, then for all cases, the algorithm **terminates** after **finite number of steps**.
+ Effectiveness: Every instrution must be basic enough to be carried out, in principle, by a person using only pencil and paper. It is not enough that each operation be definite as in (3). It also must be **feasible**.

!!! note
	A **program** is written in some programming language, and does not have to be finite.(e.g. an operation system)

	A **algorithm** can be described by human languages, or psdeudo-code.

## 1.2 How to Analyze

+ Machine & compiler-dependent run time.
+ Time & space complexities: Machine & compiler-**independent**

!!! note assumptions
	1. Instructions are executed sequentially(连续的).
	2. Each instruction is simple, and takes exactly one time unit.
	3. Integer size is fixed(固定的) and we have infinite(无穷的) memory.

### 1.2.1 Time Complexities
Typically the following two functions are analyzed:
$T_{avg}(N)$&$T_{wrost}(N)$:the average and worst case time complexities, a function of input size N.
!!! example "Matrix Addition"
	```c
	void add(int a[][MAX_SIZE], int b[][MAX_SIZE], int c[][MAX_SIZE], int rows, int cols)
	{
		int i,j;
		for(i=0;i<rows;i++)	/*rows+1*/
			for(j=0;j<cols;j++) /*rows(cols+1)*/
				c[i][j]=a[i][j]+b[i][j]; /*rows*cols*/
	}
	```
	T(rows, cols)=2rows·cols+2**rows**+1(**rows** can be selected in {rows, cols})

=== "Iterative function for summing a list of numbers"
	!!! example "Iterative function"
		```c linenums='1'
		float sum(float list[], int n)
		{
			/*add a list of numbers*/
			float tempsum = 0;		/*count++*/
			int i;
			for(i=0;i<n;i++)
				/*count++*/
				tempsum += list[i];	/*count++*/
			return tempsum;			/*count++*/
		}
		```
		T(n)=2n+3
=== "Recursive function for summing a list of numbers"
	!!! example "Recursive function"
		```c
		float rsum(float list[], int n)
		{
			/*add a list of numbers*/
			if(n) /*count++*/
				return rsum(list,n-1)+list[n-1];
				/*count++*/
			return 0; /*count++*/
		}
		```
		T(n)=2n+2

#### 1.2.1.1 FOR loops

The running time of a FOR loop is at most the running time of the statements inside the FOR loop(including tests) times the number of iterations.

#### 1.2.1.2 Nested(嵌套的) FOR loops

The total running time of a statement inside a group of nested loops is the running time of the statements multiplied by the product(乘积) of sizes of all the FOR loops.

#### 1.2.1.3 Consecutive statements

These just add (which means that the maximum is the one that counts).

#### 1.2.1.4 IF/ELSE

For the fragment if(Condition) S1; else S2; the running time is never more than the test plus the larger of the running tiem of S1 and S2.

### 1.2.2 Asymptotic(渐近的) Notation(符号)  ( $\Omega,\Theta,o,O$ )

#### 1.2.2.1 T(N)=O(f(N)) 
If there are positive constants $c$ and n such that T(N)<=cf(N) for all N>=n

#### 1.2.2.2 T(N)=$\Omega$(g(N))
If there are positive constants $c$ and n such that T(N)>=cg(N) for all N>=n

#### 1.2.2.3 T(N)=$\Theta$(h(N))
If and only if T(N)=O(h(N)) and T(N)=$\Omega$(h(N))

#### 1.2.2.4 T(N)=o(h(N))
If T(N)=O(p(N)) and T(N)!=$\Theta$(p(N))


### 1.2.3 Rules of Asymptotic Notation
+ If $T_1$(N)=O(f(N)) and $T_2$(N)=O(g(N)), then
    + $T_1$(N)+$T_2$(N)=max{O(f(N)),O(g(N))}
    + $T_1$(N)\*$T_2$(N)=O(f(N)\*g(N))
+ If T(N) is a polynomial of degree k, then T(N)=$\Theta$(N^k)
+ $log^kN$=O(N) for any constant k.

## 1.3 Check your analysis
### 1.3.1 Method 1

When $T(N)=O(N)$, check if $T(2N)/T(N)=2$

When $T(N)=O(N^2)$, check if $T(2N)/T(N)=4$

When $T(N)=O(N^3)$, check if $T(2N)/T(N)=8$

### 1.3.2 Method 2
When T(N)=O(f(N)), check if $\displaystyle\lim_{N\rightarrow\infty}\frac{T(N)}{f(N)}$=constant.