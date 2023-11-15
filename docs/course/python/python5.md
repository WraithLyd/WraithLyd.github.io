# 函数
## 创建函数
### 函数的基本格式
定义函数的基本格式如下：
```
def 函数名(参数, 参数, ...):
	函数体代码
```
??? warning "TypeError报错"
	定义并创建函数后，在调用函数时，输入的参数过少或过多都会出现TypeError报错。
### 参数类型
#### 可变参数
当输入的参数的个数不确定时，可以使用可变参数。格式如下：
```
def 函数名(参数, 参数1, ..., *可变参数):
	函数体代码
```
使用可变参数的规则如下：

+ 可变参数后面不能再有其他一般参数。
+ 一个函数只能使用一个可变参数。

下面是一个可变参数的例子：
```python linenums='1'
# values为可变参数
def print_n(n, *values):
	# 循环n次
	for i in range(n):
		for value in values:
			print(value)
	# 换行
	print()

# 调用函数
print_n(3, "Hello", "world", "!")
```
#### 默认参数
默认参数是在函数定义时赋值的变量，在调用函数可以对它进行赋值也可以不进行赋值，如果重新赋值，那么默认参数用新赋的值，如果没有赋值，那么用函数定义时的值。默认参数和可变参数一样后面不能有一般参数。
```python linenums='1'
def print_n(value, n=2):
	# 循环n次
	for i in range(n):
		print(value)

# 循环"Hello"两次
print_n("Hello")
# 循环"Hello"三次
print_n("Hello", 3)
```
#### 关键字参数
关键字参数是指在为参数赋值时，直接指定参数名称并输入值，**一般都是为默认参数赋值**。

当可变参数和默认参数同时存在时，可以用关键字参数为默认参数赋值，避免歧义。
```python linenums='1'
def print_n(*values, n=2):
	for i in range(n):
		for value in values:
			print(value)
		print()

# Hello World循环三次
print_n("Hello", "World", n=3)
```
在多个默认参数中只输入有需要的值，用关键字参数精准赋值需要改变的默认参数。
```python linenums='1'
def test(a, b=0, c=0):
	print(a*100+b*10+c)

# 默认格式
test(1, 2, 3)				# output -> 123
# 全部参数都是关键字参数的格式
test(a=1, b=5, c=7)			# output -> 157
# 指定任意排序关键字参数格式
test(c=1, a=3, b=4)			# output -> 341
# 部分参数时关键字参数的格式
test(5, c=6)				# output -> 506
```
### 返回
函数内使用return关键字可以回到函数执行的位置，也就意味着函数结束。当return后面没有接返回值时，返回值为None。
```python linenums='1'
def test():
	print("A")
	return
a = test()
print(a)					# output -> None
```
??? warning "UnboundedLocalError报错"
	由于Python在函数内部不能引用函数外部的变量，直接使用就会出现UnboundedLocalError报错。所以在函数内部需要使用外部变量时需要用到global关键字，就像如下代码。
	```python linenums='1'
	counter = 0

	# 定义函数
	def test(n):
		global counter				# 声明counter变量
		counter += 1
		print(counter+n)

	# 调用函数
	test(10)
	```
## 递归函数
### 递归函数的应用
在进行以循环为主体的函数时，我们可以将其改写为递归函数，即高次函数调用低次函数的值进行运算，简化了代码。

这里用阶乘函数factorial( )函数为例。
```python linenums='1'
def factorial():
	# 若n是0，则返回1
	if n == 0:
		return 1
	# 若n不是0，则返回n*(n-1)!
	else:
		return n * factorial(n - 1)
```
### 递归函数的缺点
由于递归函数经常会出现几何级数次反复调用自身的问题，所以在参数较大时会出现运行时间非常长的情况。比如fibonacci问题就会出现这种情况。
```python linenums='1'
def fibonacci(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(15))
```
要解决这个问题就需要用到缓存的概念，将较小的参数的斐波那契数存放在内存中，需要调用时直接取出，相同的值只运算一次。
```python linenums='1'
# 创建缓存变量
dictionary = {
	1: 1,
	2: 1
}

# 定义函数
def fibonacci(n):
	if n in dictionary:
		# 若有缓存，则直接调用缓存
		return dictionary[n]
	else:
		# 若无缓存，则求值并将结果放入缓存
		output = fibonacci(n - 1) + fibonacci(n - 2)
		dictionary[n] = output
		return output
```
## 元组
### 元组的定义和使用
元组(tuple)是和列表类似的数据类型，与列表不同的一点是元组的元素不能修改。通常元组是和函数同时使用的数据类型。生成方法如下：
```
(数据, 数据, 数据, ...)
```
使用方法基本上是定义元组后输出各元素。
```python linenums='1'
tuple = (1, 2, 3)
print(tuple[0])			# output -> 1
print(tuple[1])			# output -> 2
print(tuple[2])			# output -> 3
```
元组的括号可以省略，比如：
```python linenums='1'
tuple = 1, 2, 3
print(tuple)			# output -> (1, 2, 3)
```
元组和列表一样，可以与 "+" 或 "*" 连用，不过和写列表时没有区别，所以一般不使用元组。
??? tip "只有一个元素的元组"
	和列表不同，只有一个元素的元组应该写为`(数据, )`而不是`(数据)`
### 列表和元组的特殊使用
```python linenums='1'
[a, b] = [1, 2]
(c, d) = (3, 4)
e, f, g = 10, 20, 30
```
这种格式可以方便定义和分配变量。
??? info "变量值的对调"
	在交换两个变量的值是，C语言需要设置一个临时变量来过渡，但是Python可以直接使用元组来交换。
	```python linenums='1'
	a, b = 10, 20
	a, b = b, a
	print("a =",a)			# output -> a = 20
	print("b =",b)			# output -> b = 10
	```
### 元组在函数中的应用
```python linenums='1'
def div(a, b):			# 和Python内置函数divmod( )功能等同
	c = a // b
	d = a % b
	return (c, d)

print(div(34, 5))		# output -> (6, 4)
```
### Lambda