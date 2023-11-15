# 条件语句
## 布尔数据类型
布尔只有True和False两个值，且True和False的首字母必须是大写。

在Python中空字符串（""）和0都可以转换为False。
### 比较运算符
Python有六个比较运算符，且通过比较运算符创建布尔。

|运算符|说明|运算符|说明|运算符|说明|
|:--:|:--:|:--:|:--:|:--:|:--:|
|==|等于|!=|不等于|<|小于|
|>|大于|<=|不大于|>=|不小于|

### 逻辑运算符
|运算符|说明|解释|
|:--:|:--:|:--:|
|not|非|对布尔值取非|
|and|与|如果两个布尔值都为真，则为真，否则为假|
|or|或|如果两个布尔值至少有一个为真，则为真，都为假时为假|

### if条件语句
Python中**if条件语句**时根据if后的条件去选择执行某些代码或不执行某些代码。

!!! tip "基本结构"
	```linenums='1'
	if 布尔值的条件语句:	# if中的条件语句后面必须加上冒号(:)。  
		当布尔值为True时执行的语句	# if条件语句的下一行语句输入时需要先输入4个空格或一个制表符；  
		当布尔值为True时执行的语句	# 如果后续还有条件执行的语句也需要加上制表符，直到结束该条件分支。  
	```

!!! example inline end "执行结果"
	```linenums='1'
	5
	>
	4
	end
	```
```python linenums='1'
if 5>4:
	print("5")
	print(">")
	print("4")
# 条件分支结束
print("end")
```
### else条件语句
else语句用于if条件语句执行之后，当if条件语句中的条件为假时执行该语句。

!!! tip "基本结构"
	```linenums='1'
	if 布尔值的条件语句:	# if中的条件语句后面必须加上冒号(:)。  
		当布尔值为True时执行的语句	# if条件语句的下一行语句输入时需要先输入4个空格或一个制表符；  
		当布尔值为True时执行的语句	# 如果后续还有条件执行的语句也需要加上制表符，直到结束该条件分支。  
	else:	# else后必须加上冒号(:)。
		当布尔值为False时执行的语句	# 如果后续还有条件执行的语句也需要加上制表符，直到结束该条件分支。  
	```

!!! example inline end "执行结果"
	```linenums='1'
	请输入整数 9
	奇数
	```
```python linenums='1'
number = input("请输入整数 ")
number = int(number)
if number % 2 == 0:
	# 条件为真
	print("偶数")
else:
	# 条件为假
	print("奇数")
```
### elif语句
有时if语句会有两个或以上的条件，不同的条件组合会得到不同的结果时，第一个分支用if语句，最后一个分支用else语句，那么中间的分支就需要用到elif语句，elif语句相当于是else语句和if语句的结合。

!!! tip "基本结构"
	```linenums='1'
	if 布尔值的条件语句A:
		当布尔值A为True时执行的语句
	elif 布尔值的条件语句B:
		当A为False且B为True时执行的语句
	else:
		当A,B均为False时执行的语句
	```

??? warning "Indentation Error 报错"
	Indentation Error指的是“缩进错误”。  

	Python中if条件语句中必须要有四个缩进来编写代码，否则会导致Indentation Error。如果在缩进处编写注释或是回车，也无法解决该错误。如果输入随便的一条语句“0”或是关键字pass，则会运行正常。
	
	pass关键字可以理解为什么都不做，后续会补充功能的地方。
	=== "error-none"
		```python linenums='1'
		if number > 0:
		else:
		```
	=== "error-comment"
		```python linenums='1'
		if number > 0:
			# 正数
		else:
			# 负数
		```
	=== "正常运行-0"
		```python linenums='1'
		if number > 0:
			0
		else:
			0
		```
	=== "正常运行-pass"
		```python linenums='1'
		if number > 0:
			pass
		else:
			pass
		```
