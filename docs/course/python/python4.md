# 循环语句
## 列表
### 定义列表并访问元素
Python中，通过方括号"[ ]"中输入以都好分隔的数据，可以定义为**列表**。在方括号内的数据称为**元素**。

如果需要调用列表中的数据，就需要用到**索引**，列表索引类似于字符串索引，第一个数据的索引为0，第二个数据的索引为1，以此类推。列表索引的性质也和字符串索引类似，都可以逆向访问，即list[-1]代表列表最后一个数据，list[-2]代表列表倒数第二个数据，以此类推。

!!! tip "基本结构"
	```python linenums='1'
	list = [element1, element2, element3, ...]
	print(list[index])		# 输出第（index+1）个数据
	```

### 更改列表元素
列表索引和字符串不同的一点就在于列表可以利用索引更改列表中元素。

!!! example inline end "执行结果"
	```linenums='1'
	['change','your','icon']
	```
```python linenums='1'
list = ["print","your","name"]
list[0] = "change"		# 更改list中第一个元素
list[-1] = "icon" 		# 更改list中第三个元素
print(list)
```
### 多重列表
列表中可以嵌套列表，将其变为多重列表。

!!! example inline end "执行结果"
	```linenums='1'
	list[1] = [4,5,6]
	list[1][1] = 5
	```
```python linenums='1'
list = [[1,2,3],[4,5,6],[7,8,9]]
# 双重列表的元素是普通列表
print("list[1] =",list[1])
# 嵌套使用索引可以得到具体的元素
print("list[1][1] =",list[1][1])
```

??? warning "Index Error 报错"
	当试图访问超过列表的索引来访问元素时，会发生Index Error报错。
	
	正常列表的索引应该在[-列表长度, 列表长度-1]内。

### 列表运算符 

+ **连接**("+")是将两个两个列表按照第二个列表拼接在第一个列表后的规则得到一个新的列表。
+ **重复**("*")是将整数个相同的列表相连接。
+ **len( )**将列表变量作为参数时，计算的是列表的元素个数

!!! example inline end "执行结果"
	```linenums='1'
	#基本运算符
	list1+list2= [1, 2, 4, 5]
	list1*2= [1, 2, 1, 2]
	#函数
	len(list1) = 2
	```
```python linenums='1'
list1 = [1,2]
list2 = [4,5]
#基本运算符
print("#基本运算符")
print("list1+list2=",list1+list2)
print("list1*2=",list1*2)
#函数
print("#函数")
print("len(list1) =",len(list1))
```

### 列表当中添加元素

在已定义列表中添加元素一般用**append( )**函数或**insert( )**函数。

+ **append( )**函数：只能在列表最后端添加元素。
```
列表名.append(元素)
```
+ **insert( )**函数：可以在列表指定位置添加元素。
```
列表名.insert(位置，元素)
```
+ **extend()**函数：可以在列表最后端添加多个元素。
```
列表名.extend(元素组成的列表)
```
!!! example inline end "执行结果"
	```linenums='1'
	#在列表的最后端添加元素
	[1, 2, 3, 4, 5]
	#在列表的指定位置添加元素
	[0, 1, 2, 3, 4, 5]
	#在列表的最后端添加多个元素
	[0, 1, 2, 3, 4, 5, 6, 7]
	```
```python linenums='1'
list = [1,2,3]
print("#在列表的最后端添加元素")
list.append(4)
list.append(5)
print(list)
print("#在列表的指定位置添加元素")
list.insert(0,0)
print(list)
print("#在列表的最后端添加多个元素")
listn = [6,7]
list.extend(listn)
print(list)
```
??? tip "列表连接运算符和插入元素之间的区别"
	**列表连接运算符**和**extend( )函数**的功能十分相似，但是在得到运算结果时有所不同。
	
	+ **列表连接运算符**在连接过程中不会对原列表变量的值做出改变
	+ **extend( )函数**会将连接后的新列表赋值给原列表变量
	```python linenums='1'
	a = [1,2,3,4]
	b = [5,6,7,8]
	c = a + b
	print(a)		# output -> [1, 2, 3, 4]
	a.extend(b)
	print(a)		# output -> [1, 2, 3, 4, 5, 6, 7, 8]
	```

### 从列表中删除元素
#### 利用索引删除列表元素
根据元素的位置信息删除元素一般引用**del关键字**或**pop( )函数**。

+ **del关键字**代码执行时可删除索引值所在位置的元素。
```
del 列表名称[索引]
```
+ **pop( )函数**也删除索引值指定位置中的元素，如果未输入参数，则删除最后一个元素。
```
列表名.pop(索引)
```
!!! example inline end "执行结果"
	```linenums='1'
	# del删除第2个元素
	[1, 3, 4, 5]
	# pop删除最后一个元素
	[1, 3, 4]
	```
```python linenums='1'
list = [1,2,3,4,5]
# del删除第2个元素
print("# del删除第2个元素")
del list[1]
print(list)
# pop删除最后一个元素
print("# pop删除最后一个元素")
list.pop(-1)
print(list)
```
两者不同的是**pop( )函数**作为**print( )函数**的参数可以输出删除的这个元素，如：
```python linenums='1'
list = [1,2,3,4,5]
print(list.pop(-1))			# output -> 5
print(list)					# output -> [1, 2, 3, 4]
```
当使用**del关键字**时，还可以删除列表中指定范围的元素，当del[ ]中的指定范围为[a:b] (a<b)时，不包含最后一个元素。
```python linenums='1'
list = [0,1,2,3,4,5,6]
del list[3:6]
print(list)					# output -> [0, 1, 2, 6]
```
#### 根据值删除
**remove( )函数**可以通过指定的一个值来删除列表中的元素，不过只删除最先找出来的一个，如果要删除所有该元素则需要调用循环。
```python linenums='1'
list = [1,2,1,2,1,2]
list.remove(1)
print(list)					# output -> [2, 1, 2, 1, 2]
```
#### 删除全部
**clear( )函数**可以删除列表中的所有元素。
```python linenums='1'
list = [1,2,3,4,5,6]
list.clear()
print(list)					# output -> []
```
### 确认列表中是否存在
**in 运算符**用来确认列表中是否存在某个特定值。
```python linenums='1'
list = [1,2,3,4,5]
print(1 in list)			# output -> True
print(2 in list)			# output -> True
print(6 in list)			# output -> False
print('1' in list)			# output -> False
```
**not in 运算符**和 **in 运算符**的作用相反。
```python linenums='1'
list = [1,2,3,4,5]
print(1 not in list)		# output -> False
print(not 2 in list)		# output -> False
print(6 not in list)		# output -> True
print(not '1' in list)		# output -> True
```

### 基于列表执行的for循环语句
!!! tip "基本结构"
	```
	for 循环体 in 可循环条件:
		代码
	```
	可循环的数据有字符串、列表、字典和范围等等。

这是一个用列表作为可循环数据的循环语句。
!!! example inline end "执行结果"
	```linenums='1'
	123
	432
	578
	9100
	```
```python linenums='1'
# 定义列表
array = [123, 432, 578, 9100]

for element in array:
	# 输出
	print(element)
```

## 字典
**列表**是基于**索引**存储值，**字典**是基于**键**存储值。
### 定义字典
定义字典使用大括号"{ }"，并使用逗号","连接"Key:Value"形式。键可以用字符串、数字、布尔类型定义，通常字符串居多。
!!! tip "基本结构"
	```
	变量 = {
		键1: 值,
		键2: 值,
		...
		键n: 值
	}
	```
具体应用代码如下：
```python linenums='1'
dict = {
	"name": "dict",
	"type": "dictionary"
}
```
??? warning "NameError 报错"
	当创建字典时使用字符串未加引号时，就代表了使用一个未定义的变量去创建字典，会出现NameError报错。
### 字典中元素的处理
#### 访问字典中的元素
!!! tip "基本结构"
	```
	字典变量名[键名]
	```
	**当键名为字符串时，一定要记得加上引号。**
如上述字典，调用如下：
```python linenums='1'
print(dict["name"])			# output -> 'dict'
print(dict["type"])			# output -> 'dictionary'
```
#### 添加/改变字典中元素
!!! tip "基本结构"
	```
	字典[键] = 值
	```
如果该键在字典中不存在，那么新增元素，反之只需要更改原键对应的值。
#### 删除字典中元素
删除字典中元素和列表一样，使用**del关键字**。
```python linenums='1'
del dict["type"]
```
??? warning "Key Error 报错"
	当访问字典中不存在的键时，会出现Key Error报错。类似列表Index Error报错。
### 检查字典中是否存在键
检查字典中存在键有两种方法，分别是**in关键字**和**get( )函数**。

+ in关键字
```python linenums='1'
if key in dict:
	print(dict[key])
```
+ get( )函数
```python linenums='1'
value = dict.get(key)	# 如果这个key在dict中不存在，那么会返回None而不会报错。
if value == none:
	print()
```
### 基于字典执行的for循环语句
!!! tip "基本结构"
	```
	for 键变量 in 字典:
		代码
	```
	针对指定字典中的所有键进行循环。

这是一个用列表作为可循环数据的循环语句。
!!! example inline end "执行结果"
	```linenums='1'
	name : dict
	type : dictionary
	```
```python linenums='1'
# 定义列表
dict = {
	"name": "dict",
	"type": "dictionary"
}

for key in dict:
	# 输出
	print(key,':',dict[key])
```
## 范围
### 范围的使用
范围(range)是一个经常与for循环语句同时使用的数据类型。一般有三种用法。

+ 在参数中加入一个数字
```python
# 定义从0到A-1的整数构成的范围
range(A)	# A是数字
```
+ 在参数中加入两个数字
```python
# 定义从A到B-1的整数构成的范围
range(A,B)	# A和B是数字
```
+ 在参数中加入三个数字
```python
# 定义从0到A-1的整数构成且前后数字之差为C的范围
# 也就是在range(A,B)中符合A+nC的数组成的范围(n为整数)
range(A,B,C)	# A,B和C是数字
```
list( )函数可以将范围(range)改为列表(list)，可以根据list( )函数进行输出。
!!! example inline end "执行结果"
	```linenums='1'
	[0, 1, 2, 3]
	[3, 4, 5, 6]
	[0, 2, 4, 6, 8]
	[0, 3, 6, 9]
	[5, 4, 3, 2, 1, 0]
	```
```python linenums='1'
# range(A)
print(list(range(4)))
# range(A,B)
print(list(range(3,7)))
# range(A,B,C)
print(list(range(0,10,2)))
print(list(range(0,10,3)))
# 反向范围，可应用到反向循环
print(list(range(5,-1,-1)))
```

```python linenums='1'
for i in range(5):
	print(i)
# output ↓
# 0
# 1
# 2
# 3
# 4
```
### 基于列表和范围的for循环语句
!!! example inline end "执行结果"
	```linenums='1'
	第0次循环：24
	第1次循环：56
	第2次循环：74
	第3次循环：97
	第4次循环：108
	```
```python linenums='1'
# 定义数组
array = [24, 56, 74, 97, 108]

# 执行循环
for i in range(len(array)):
	# 输出
	print("第{}次循环：{}".format(i,array[i]))
```
## while循环语句
!!! tip "基本结构"
	```
	while 布尔表达式:
		语句
	```
	当布尔表达式为True时，while就会不断循环循环体语句。
举个例子，在列表中说过remove( )函数一次只能删除最先找出来的一个，如果要删除所有该元素则需要调用循环，这里就是一个利用循环删除所有该元素的程序。
!!! example inline end "执行结果"
	```linenums='1'
	[1, 1]
	```
```python linenums='1'
list = [1, 2, 1, 2]
value = 2
# 如果list中仍存在value，则执行循环
while value in list:
	list.remove(value)
print(list)
```
### break关键字
在for或while循环语句中遇见break关键字，则会直接终止循环。
!!! example inline end "执行结果"
	```linenums='1'
	第0次循环
	>是否退出？(y/N)n
	第1次循环
	>是否退出？(y/N)n
	第2次循环
	>是否退出？(y/N)y
	退出成功
	```
```python linenums='1'
i = 0
while True:
	# 输出是第几次循环
	print("第{}次循环".format(i))
	i = i + 1
	# 输入字符，如果是y/Y则退出，否则继续
	text = input(">是否退出？(y/N)")
	if text in ['y', 'Y']:
		print("退出成功")
		break
```
### continue关键字
countiue关键字是跳过当前循环，直接进入下一个循环。
!!! example inline end "执行结果"
	```linenums='1'
	1
	2
	3
	4
	```
```python linenums='1'
numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:
	# 如果number是5的倍数，那么跳过
	if number % 5 == 0:
		continue
	print(number)
```
## 与字符串、列表、字典相关的函数
### 列表基本函数
|函数|说明|
|:--:|:--:|
|min( )|在列表中查找最小值|
|max( )|在列表中查找最大值|
|sum( )|将列表中所有值求和|

```python linenums='1'
numbers = [53, 108, 97, 26, 320]
print(min(numbers))				# output -> 26
print(max(numbers))				# output -> 320
print(sum(numbers))				# output -> 604
```
### reversed( )函数翻转列表
如果要在列表中翻转元素的顺序，可以利用reverse( )函数。不过由于reversed( )函数直接产生的数据是一个生成器而不是一个列表，所以需要用list( )函数将其转为列表。
```python linenums='1'
list1 = [1, 2, 3, 4, 5, 6]
print(list(reversed(list1)))	# output -> [6, 5, 4, 3, 2, 1]
```
当然，在for语句中使用逆向循环时可以直接使用reversed( )函数，但不能多次使用同一次函数产生的结果。
```python linenums='1'
numbers = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers):
	print("循环1：",i)

for i in reversed(numbers):
	print("循环2：",i)
```
??? tip "扩展切片"
	翻转列表的另一个方法是**扩展切片**，如果将[::-1]附加在列表上，则会翻转列表的内容。
	```python linenums='1'
	numbers = [1, 2, 3, 4, 5]
	print(numbers[::-1])		# output -> [5, 4, 3, 2, 1]
	```
### 使用enumerate( )函数简化循环语句
enumerate( )函数会将列表转换为携带索引的元组。不过由于enumerate( )函数直接产生的数据也是一个生成器而不是一个列表，所以需要用list( )函数将其转为列表。
```python linenums='1'
list1 = ["element1", "element2", "element3"]
print(list(enumerate(list1)))	# output -> [(0, 'element1'), (1, 'element2'), (2, 'element3')]
```
当使用经过enumerate( )函数处理过的列表来循环时，可以使用多了循环变量。
!!! example inline end "执行结果"
	```linenums='1'
	No0 element is element1.
	No1 element is element2.
	No2 element is element3.
	```
```python linenums='1'
list1 = ["element1", "element2", "element3"]

for i, value in enumerate(list1):
	print("No{} element is {}.".format(i,value))
```
### 使用items( )函数简化循环语句
像enumerate( )函数一样，items( )函数也可以将字典中的key和value结合起来，进行循环。
!!! example inline end "执行结果"
	```linenums='1'
	Value of key1 is value1.
	Value of key2 is value2.
	Value of key3 is value3.
	```
```python linenums='1'
dictionary = {
	"key1": "value1",
	"key2": "value2",
	"key3": "value3",
}

for key, value in dictionary.items():
	print("Value of {} is {}.".format(key,value))
```
### 列表嵌套
用已知列表经过加工生成新列表的过程中可以利用列表嵌套。基本格式如下：
```
列表名称 = [表达式 for 循环器 in 可循环的]
```
如果含有条件语句，那么可以为：
```
列表名称 = [表达式 for 循环器 in 可循环的 if 条件语句]
```
!!! example "举个例子（基础嵌套）"
	```python linenums='1'
	array = []
	for i in range(0, 20, 2):
		array.append(i * i)
	```
	```python linenums='1'
	array  = [i * i for i in range(0, 20, 2)]
	```
	这两条代码等价。
!!! example "举个例子（条件嵌套）"
	```python linenums='1'
	array = ["A", "B", "C", "D", "E"]
	output = [a for a in array if a != "B"]
	print(output)			# ['A', 'C', 'D', 'E']
	```
