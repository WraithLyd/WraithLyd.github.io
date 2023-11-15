# Python入门
## 关键字

??? example "keyword"
	'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
运行以下代码也可得到关键字。
```python linenums="1"
import keyword
print(keyword.kwlist)
```

## 标识符
标识符需要遵循以下规则：

+ 不能使用关键字  
+ 特殊字符只允许使用下划线 `_`
+ 不能以数字开头
+ 不能包含空格

## 命名法

|名称|命名方法|备注|
|:--:|:--:|:--:|
|蛇形命名法|由 `_` 串接起全为小写的单词|一般用来表示**变量**和**函数**|
|驼峰命名法|由首字母大写的单词直接拼接而成|一般用来表示**类**|

## 注释

单行注释使用 `#` 来表示该行后面的为注释，使用三组引号代表字符串，如果不进行赋值，我们可以视为多行注释。

=== "单行注释"
	```python linenums="1"
	print("This is comment.") # This is comment1.
	```
=== "多行注释"
	```python linenums="1"

	'''
	This is comment2.
	'''

	"""
	This is comment3.
	"""
	```

## 输出

最基本的输出方式为使用 **print( )** 函数。

### 输出多项内容

	print(输出1，输出2，输出3，...)

这种情况下输出1，输出2，输出3，...可以为不同数据类型。

当输出全为字符串时，可以用

	print(输出1+输出2+输出3+...)

来输出，+ 表示字符串的拼接，如果有数据存在，应该用 **str( )** 转化为字符串，但是如果未转换，在字符串中混杂数据类型，会出现报错。

### 换行

```python linenums="1"
print() # 输出空行
```