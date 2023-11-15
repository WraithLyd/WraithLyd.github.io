# Algorithm Analysis
## Algorithm Definition
??? note
	# 算法
	## 算法定义
	一个算法必须满足以下要求：

	+ 输入：0个或更多的参数
	+ 输出：
	+ 确定的：每一条指令都应是清晰的
	+ 有限的：算法一定是要终止的
  
A algorithm must satisfy:

+ Input: zero or more 
+ Output:
+ 
## How to Analyze

+ Machine & compiler-dependent run time.
+ Time & space complexities: Machine & compiler-independent

### Time Complexities
Typically the following two functions are analyzed:
$T_{avg}(N)$&$T_{wrost}(N)$:the average and worst case time complexities, N means input size.

??? example "Time Complexities"
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
	$T_{sum}(n)=2n+3$

### Asymptotic Notation  ( $\Omega,\Theta,\o,\O$ )

$T(N)=O(f(N))$ if there are positive constants $c$ and $n_0$ such that $T(N)\leq c f(N)$ for all $N\geq n_0$
$T(N)=\Omega(g(N))$ if there are positive constants $c$ and $n_0$ such that $T(N)\geq c g(N)$ for all $N\geq n_0$
$T(N)=\Theta(h(N))$ if and only if $T(N)=O(h(N))$ and $T(N)=\Omega(h(N))$
$T(N)=\Theta(h(N))$ if and only if $T(N)=O(h(N))$ and $T(N)\neq\Theta(h(N))$


### Rules of Asymptotic Notation
If $T_1(N)=O(f(N))$ and $T_2(N)=O(g(N))$, then
+ $T_1(N)+T_2(N)=max{O(f(N)),O(g(N))}$
+ $T_1(N)*T_2(N)=O(f(N)*g(N))$

If $T(N)$ is a polynomial of degree $k$, then $T(N)=\Theta(N^k)$



## Check your analysis

When $T(N)=O(N)$, check if $T(2N)/T(N)=2$

When $T(N)=O(N^2)$, check if $T(2N)/T(N)=4$

When $T(N)=O(N^3)$, check if $T(2N)/T(N)=8$