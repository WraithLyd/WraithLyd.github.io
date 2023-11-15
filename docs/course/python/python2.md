# 数据类型
!!! note "数据类型"
	Python中最基本的数据类型有：

	+ 字符串 (string) ，如：'hello','python'  
	+ 数字 (number) ，如：52,112  
	+ 布尔 (boolean) ，如：True,False  

## 数据类型的确认
```python linenums="1"
print(type("hello"))
# <class 'str'>
print(type(124))
# <class 'int'>
```
## 字符串
### 字符串内含引号
+ 使用**不同引号套用**
```python linenums="1"
print('the "wolves"')
# the "wolves"
print("the 'wolves'")
# the 'wolves'
```
+ 使用**转义字符**
```python linenums="1"
print('the \'wolves\'')
# the 'wolves'
print("the \"wolves\"")
# the "wolves"
```
??? example "其他转义字符"
	+ **换行符**：`\n`
	```python linenums="1"
	print("Hello\npython")
	# Hello
	# python
	```
	+ **制表符**：`\t`
	```python linenums='1'
	print("name\tage\taddress")
	print("Tom\t8\tWhite House")
	print("Jerry\t8\tWhite House")
	# name    age     address
	# Tom     8       White House
	# Jerry   8       White House
	```

### 创建多行字符串
重复三次使用单引号或双引号，则变成多行字符串。
```python linenums="1"
print("""壮岁旌旗拥万夫
锦襜突骑渡江初
燕兵夜娖银胡䩮
汉箭朝飞金仆姑""")
# 壮岁旌旗拥万夫
# 锦襜突骑渡江初
# 燕兵夜娖银胡䩮
# 汉箭朝飞金仆姑
```
!!! tip "在多行字符串中隐藏换行"
	在创建多行字符串时，有时字符串不需要换行，但是为了查看代码方便增加了换行，那么就需要将有些换行隐藏起来。
	=== "隐藏换行"
		```python linenums="1"

		print("""\
		壮岁旌旗拥万夫
		锦襜突骑渡江初
		燕兵夜娖银胡䩮
		汉箭朝飞金仆姑\
		""")
		# 壮岁旌旗拥万夫
		# 锦襜突骑渡江初
		# 燕兵夜娖银胡䩮
		# 汉箭朝飞金仆姑

		```
	=== "不隐藏换行"
		```python linenums="1"

		print("""
		壮岁旌旗拥万夫
		锦襜突骑渡江初
		燕兵夜娖银胡䩮
		汉箭朝飞金仆姑
		""")
		# 
		# 壮岁旌旗拥万夫
		# 锦襜突骑渡江初
		# 燕兵夜娖银胡䩮
		# 汉箭朝飞金仆姑
		# 
		```

### 字符串运算符
**字符串连接运算符 "+"**

字符串连接运算符执行结果是将两个字符串连接起来创建新的字符串。
```python linenums='1'
print('Hello'+' '+'world')
# Hello world
```
**字符串重复运算符 "*"**

字符串重复运算符连接字符串和数字，可以重复该字符串。
```python linenums='1'
print('Wraith'*3)
# WraithWraithWraith
print(3*'Wraith')
# WraithWraithWraith
```
!!! Info "字符串运算符优先级"
	和数字运算优先级类似，字符串重复运算符(`*`)优先级高于字符串连接运算符(`+`)。
	```python linenums='1'
	print('o'+'h'*3)
	# ohhh
	```

**字符串索引运算符 "[ ]"**

选取该字符串中的单个字符的运算符。在`[ ]`中指定要选取的位置，该数字称为索引。python中的索引和C语言一样，是从0开始的。而索引为负数时可以进行逆向计数。
=== "正数"
	!!! example inline end "执行结果"	
		```linenums='1'
		W
		r
		a
		i
		t
		h
		```
	```python linenums='1'
	str='Wraith'
	print(str[0])
	print(str[1])
	print(str[2])
	print(str[3])
	print(str[4])
	print(str[5])
	```
=== "负数"
	!!! example inline end "执行结果"
		```linenums='1'
		h
		t
		i
		a
		r
		W
		```
	```python linenums='1'
	str='Wraith'
	print(str[-1])
	print(str[-2])
	print(str[-3])
	print(str[-4])
	print(str[-5])
	print(str[-6])
	```
	
**字符串切片运算符 "[ : ]"**

字符串切片运算符是用来在某个字符串中选取特定范围的运算符，冒号隔开两个数字，代表上下界，其中左边的数字较小，右边数字较大。选取的字符串就是原字符串中从前面数字索引开始到后面数字索引的一段子字符串，不过前面数字索引的字符包括在内，而后面数字索引的字符不包括在内。

```python linenums='1'
print('Wraith'[1:4])
# rai
print('Wraith'[4:6])
# th
```
有时也省略方括号中两个数字其中一个。如果省略前面的数字，则表示此时自动指定最前面的位置（第一个字符）；如果省略后面的数字，则表示此时自动指定最后面的位置（最后一个字符）。
```python linenums='1'
print('Wraith'[1:])
# raith
print('Wraith'[:3])
# Wra
```
### 求字符串长度
!!! info inline end "warning"
	和C语言不同的是，python是没有字符串结束符的，不过C语言的strlen( )函数并不统计字符串结束符，所以和python的len( )的值相等。
使用 **len( )** 函数可以求得字符串的长度。
```python linenums='1'
print("The length of string is:")
print(len("Hello world!"))
# The length of string is:
# 12
```
## 数字
### 数字的种类
数字分为**整型**和**浮点型**，python中有小数点的称为浮点数(float)，没有小数点的称为整数(int)。
```python linenums='1'
print(type(0))
# <class 'int'>
print(type(0.0))
# <class 'float'>
```
### 数字运算符

**四则运算符 "+" "-" "*" "/"**

=== "加"
	```python linenums='1'
	print("1 + 2 =",1+2)
	# 1 + 2 = 3
	```
=== "减"
	```shell linenums='1'
	print("1 - 2 =",1-2)
	# 1 - 2 = -1
	```
=== "乘"
	```python linenums='1'
	print("1 * 2 =",1*2)
	# 1 * 2 = 2
	```
=== "除"
	```shell linenums='1'
	print("1 / 2 =",1/2)
	# 1 / 2 = 0.5
	```
**整除运算符 "//"**

整除运算符是将数字进行除法运算后向下取整，如果针对正数来说即为直接取整数部分。
```python linenums='1'
print("3 // 2 =",3//2)
# 3 // 2 = 1
print("-3 // 2 =",-3//2)
# -3 // 2 = -2
```
**求余运算符 "%"**

求余运算符即取两数做整数除法运算得到的余数。
```python linenums='1'
print("5 % 3 =",5%3)
# 5 % 3 = 2
```
**乘方运算符 "\*\*"**

乘方运算符用于求第一个数的第二个数次方。
```python linenums='1'
print("2 ** 3 =",2**3)
# 2 ** 3 = 8
```

## 变量和输入

### 变量的定义和引用
在Python当中，变量使用的一般过程为：定义变量 → 为变量赋值 → 引用变量
!!! Example inline end "执行结果"
	```linenums='1'
	圆周率 = 3.1415926
	半径 = 10
	圆的周长 = 62.831852
	圆的面积 = 314.15926
	```
```python linenums='1'
# 定义变量并赋初值
pi = 3.1415926
r  = 10
# 变量引用
print("圆周率 =",pi)
print("半径 =",r)
print("圆的周长 =",2*pi*r)
print("圆的面积 =",pi*r**2)
```

不过变量在Python中和C,Java等语言有所不同，Python中变量并没有固定的类型，而不像其他语言使用变量前必须定义便令的数据类型。

!!! example inline end "执行结果"
	```linenums='1'
	string
	True
	0
	```

```python linenums='1'
a = 'string'
print(a)	# string
a = True
print(a)	# boolean
a = 0
print(a)	# int
```

### 复合赋值运算符

<table>
<thead>
<tr>
<th style="text-align:center" colspan="2">应用于数字的复合运算符</th>
<th style="text-align:center" colspan="2">应用于字符串的复合运算符</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">运算符</td>
<td style="text-align:center">说明</td>
<td style="text-align:center">运算符</td>
<td style="text-align:center">说明</td>
</tr>
<tr>
<td style="text-align:center">+=</td>
<td style="text-align:center">数字加法后赋值</td>
<td style="text-align:center">+=</td>
<td style="text-align:center">字符串连接后赋值</td>
</tr>
<tr>
<td style="text-align:center">-=</td>
<td style="text-align:center">数字减法后赋值</td>
<td style="text-align:center">*=</td>
<td style="text-align:center">字符串重复后赋值</td>
</tr>
<tr>
<td style="text-align:center">*=</td>
<td style="text-align:center">数字乘法后赋值</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">/=</td>
<td style="text-align:center">数字除法后赋值</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">%=</td>
<td style="text-align:center">数字取余后赋值</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">//=</td>
<td style="text-align:center">数字整除后赋值</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">**=</td>
<td style="text-align:center">数字乘方后赋值</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
</tbody>
</table>

=== "应用于数字的复合运算符"
	!!! Example inline end "执行结果"
		```linenums='1'
		110
		105
		210
		42.0
		```
	```python linenums='1'
	num = 100
	num += 10
	print(num)
	num -= 5
	print(num)
	num *= 2
	print(num)
	num /= 5
	print(num)
	```
=== "应用于字符串的复合运算符"
	!!! Example inline end "执行结果"
		```linenums='1'
		ohh
		ohhohh
		```
	```python linenums='1'
	str = 'oh'
	str += 'h'
	str += 'h'
	print(str)
	str *= 2
	print(str)
	```

### 输入函数 "input( )"

输入在input函数括号内的内容被称为**提示字符串**，如下述代码运行时，会弹出“请输入内容：”，程序在未退出的状态下等待，直到user使用enter弹入输入。这种程序在运行的过程中的暂停叫做**阻塞**。
```python linenums='1'
input("请输入内容：")	
```
input函数输出的值称为input函数的**返回值**，如果需要使用这个返回值，那就可以用input函数直接对其他变量进行赋值。

```python linenums='1'
string = input("请输入内容：")
# 请输入内容：Hello
print(string)
# Hello
```
!!! tip "input( )函数输入的数据类型"
	无论输入的是什么内容，input( )函数的返回值都是**字符串**。
!!! example inline end "执行结果"
	```linenums='1'
	string:abc
	abc : <class 'str'>
	number:123
	123 : <class 'str'>
	bool:True
	True : <class 'str'>
	```

```python linenums='1'
# input( )
str = input("string:")		# 输入str为abc
print(str,":",type(str))
num = input("number:")		# 输入num为123
print(num,":",type(num))
bool = input("bool:")		# 输入bool为True
print(bool,":",type(bool))
```
### 字符串于数字的类型转换
#### 字符串转数字
由于input( )函数输入数据类型始终为字符串，因此在输入数字时，必须将输入的字符串转为数字，一般进行数学运算。主要使用以下两个函数。

+ **int( )函数**：将字符串转换为int（整数）数据类型。
+ **float( )函数**：将字符串转换为float（浮点数）数据类型。

??? warning "Value Error 报错"
	如果转换无法转换的数据类型，则会引发"Value Error"报错。
	
	+ int( )和float( )都无法转换非纯数字的输入。
	+ int( )无法转换带有小数点的纯数字输入。
!!! example inline end "执行结果"
	```linenums='1'
	input:123
	int(): 123
	int(): <class 'int'>
	float(): 123.0
	float(): <class 'float'>
	```
```python linenums='1'
str = input("input:")
# int( )
int = int(str)
print("int():",int)
print("int():",type(int))
# float( )
float = float(str)
print("float():",float)
print("float():",type(float))
```
#### 数字转为字符串
数字利用str( )函数可以转为字符串。
!!! example inline end "执行结果"
	```linenums='1'
	123
	<class 'str'>
	```
```python linenums='1'
# str( )
num = 123
str = str(num)
print(str)
print(type(str))
```

## 关于数字和字符串的函数
### 字符串format( )函数
在包含有"{ }"的字符串后面加上"."，再使用format( )函数，将字符串中的"{ }"替换为format( )函数中参数对应字符串，大括号的数量和format( )中参数的个数必须一致。

??? warning "Index Error 报错"
	如果"{ }"的数量大于format( )函数中参数的数量，则会引发Index Error报错。

	反之，"{ }"只替换相对于的参数的字符串形式，多余的参数不予处理。

!!! example inline end "执行结果"
	```linenums='1'
	第1003次尝试
	string 2 is True
	```
```python linenums='1'
# format( )
str1 = "第{}次尝试".format(1003)
print(str1)
str2 = "{} {} is {}".format("string",2,True)
print(str2)
```


format( )函数在处理数字时可以通过"{ }"中添加字符来对数字转字符串的表现形式加以限制。

**输出类型**

+ { }中加入`:d`，直接指定输出int类型的整数，不过处理时参数只能包含整数。
+ { }中加入`:f`，直接指定输出float类型的浮点数。
+ { }中加入`:g`，舍去小数后面的所有0，如果小数部分为0则直接输出int型。

!!! example inline end "执行结果"
	```linenums='1'
	123
	21.712000
	24.5
	12
	```
```python linenums='1'
str1 = "{:d}".format(123)
print(str1)
str2 = "{:f}".format(21.712)
print(str2)
str3 = "{:g}".format(24.50)
print(str3)
str4 = "{:g}".format(12.00)
print(str4)
```
**填充空格**

如果在`{:d}`中d的前面加上一个数字，那么就表示这个数字占多长的空间，用空格填充前面的空白；如果数字前有0，则用0填充。当应用空格填充时，符号的位置就需要去根据`:`后紧接着是否是`=`来决定，如果没有等号，那么符号紧跟在数字之前；如果有等号，那么符号写在空格之前。

!!! example inline end "执行结果"
	```linenums='1'
	  123
	       123
	00123
	0000000123
	      -123
    -      123
	```
```python linenums='1'
str1 = "{:5d}".format(123)
print(str1)
str2 = "{:10d}".format(123)
print(str2)
str3 = "{:05d}".format(123)
print(str3)
str4 = "{:010d}".format(123)
print(str4)
str5 = "{:010d}".format(-123)
print(str5)
str6 = "{:=010d}".format(-123)
print(str6)
```

**符号**

在`{:d}`的d前加上+后，`{:+d}`的"+"代表输出时数字必须带有符号，如果是正数，在数字前加"+"号，如果是负数，在数字前维持"-"。

!!! example inline end "执行结果"
	```linenums='1'
	+123
	-123
	+123.456000
	-123.456000
	```
```python linenums='1'
str1 = "{:+d}".format(123)
print(str1)
str2 = "{:+d}".format(-123)
print(str2)
str3 = "{:+f}".format(123.456)
print(str3)
str4 = "{:+f}".format(-123.456)
print(str4)
```

**排列顺序**

顺序一般为"{:[=][+][整数]d/f/g}".format(数)

### 替换大小写

upper( )函数使字符串中的字母变成大写，而lower( )函数使字符串中的字母变为小写。

!!! example inline end "执行结果"
	```linenums='1'
	WELCOME TO PYTHON!
	welcome to python!
	```
```python linenums='1'
str = "Welcome to Python!"
print(str.upper())
print(str.lower())
```

### 删除字符串两侧的空格

strip( )函数可以删除字符串两边的空格，包括空格、制表符和换行符。另外，lstrip( )函数可以删除字符串左侧的空格，rstrip( )函数可以删除字符串右边的空格。

!!! example inline end "执行结果"
	```linenums='1'
	# original

	                Hello!
	Welcome to Python!


	# strip
	Hello!
	Welcome to Python!
	```
```python linenums='1'
str = """
		Hello!
Welcome to Python!

"""
# original
print("# original")
print(str)
# strip
print("# strip")
print(str.strip())
```

### is系列函数
**is函数**一般用来确认字符串配置，具体功能如下：

+ isalnum( ):确认字符串是否只由字母和数字组成
+ isalpha( ):确认字符串是否只由字母组成
+ isidentifier( ):确认字符串是否可用作标识符
+ isdecimal( ):确认字符串是否为整数
+ isdigit( ):确认字符串是否可以识别为数字
+ isspace( ):确认字符串是否仅由空格组成
+ islower( ):确认字符串是否仅由小写字母组成
+ isupper( ):确认字符串是否仅由大写字母组成

!!! example inline end "执行结果"
	```linenums='1'
	True
	False
	```
```python linenums='1'
# 判断是否由字母组成
# 是则输出True，不是则输出False
print("Python".isalpha())
# 判断是否由小写字母组成
# 是则输出True，不是则输出False
print("Python".islower())
```

### find( )函数和rfind( )函数

使用**find( )函数**和**rfind( )函数**可以查找指定字符串在字符串内部的位置，输出的数字则为子字符串的第一个字符在原字符串中的索引。

+ find( )从左到右查找，输出第一个出现的位置
+ rfind( )从后到左查找，输出第一个出现的位置

!!! example inline end "执行结果"
	```linenums='1'
	0
	12
	```
```python linenums='1'
str = "decide your destiny"
print(str.find("de"))
print(str.rfind("de"))
```

### in运算符

**in运算符**可以确认字符串的内容。

!!! example inline end "执行结果"
	```linenums='1'
	True
	False
	```
```python linenums='1'
str = "decide your destiny"
print("your" in str)
print("my" in str)
```

### split( )函数

使用**split( )函数**可以将字符串拆分为特定子字符串，split( )函数括号中的是拆分的依据，示例是按照空格进行拆分。

!!! example inline end "执行结果"
	```linenums='1'
	['true', 'or', 'false']
	```
```python linenums='1'
str = "true or false"
print(str.split(" "))
```