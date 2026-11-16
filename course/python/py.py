print(type("hello"))
# <class >
print(type(124))
print("Hello\npython")

print("name\tage\taddress")
print("Tom\t8\tWhite House")
print("Jerry\t8\tWhite House")

print("""\
壮岁旌旗拥万夫
锦襜突骑渡江初
燕兵夜娖银胡䩮
汉箭朝飞金仆姑\
""")

print(len("Hello world!"))


print('Hello'+' '+'world')

str='Wraith'
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])

print(str[2:7])

print("1 - 2 =",1-2)


# 定义变量并赋初值
pi = 3.1415926
r  = 10
# 变量引用
print("圆周率 =",pi)
print("半径 =",r)
print("圆的周长 =",2*pi*r)
print("圆的面积 =",pi*r**2)


num = 100
num += 10
print(num)
num -= 5
print(num)
num *= 2
print(num)
num //= 5
print(num)

str = 'o'
str += 'h'
str += 'h'
print(str)
str *= 2
print(str)

p = input()
print(p)

str = input("string:")
print("The type of",str,"is",type(str))
num = input("number:")
print("The type of",num,"is",type(num))
bool = input("bool:")
print("The type of",bool,"is",type(bool))


str = input("number:")
int = int(str)
print("int( ):",int)
print("int( ):",type(int))
float = float(str)
print("float( ):",float)
print("float( ):",type(float))


str = str(123)
print(str)
print(type(str))

str1 = "第{}次尝试".format(1003)
print(str1)
str2 = "{}{}is{}".format("string",2,True)
print(str2)

str = "{:g}".format(21.20)
print(str)

str1 = "{:d}".format(123)
print(str1)
str2 = "{:f}".format(21.712)
print(str2)
str3 = "{:g}".format(24.50)
print(str3)
str4 = "{:g}".format(12.00)
print(str4)

str1 = "{:+d}".format(123)
print(str1)
str2 = "{:+d}".format(-123)
print(str2)
str3 = "{:+f}".format(123.456)
print(str3)
str4 = "{:+f}".format(-123.456)
print(str4)

str1 = "{:5d}".format(123)
print(str1)
str2 = "{:10d}".format(123)
print(str2)
str3 = "{:05d}".format(123)
print(str3)
str4 = "{:010d}".format(123)
print(str4)
str5 = "{:10d}".format(-123)
print(str5)
str6 = "{:=10d}".format(-123)
print(str6)

str = "Welcome to Python!"
print(str.upper())
print(str.lower())

str = """
		Hello!
Welcome to Python!

"""
print(str)
print("#strip")
print(str.strip())


# 判断是否由字母组成，是则输出True，不是则输出False
print("Python".isalpha())
# 判断是否由小写字母组成，是则输出True，不是则输出False
print("Python".islower())

str = "decide your destiny"
print(str.find("de"))
print(str.rfind("de"))

str = "decide your destiny"
print("your" in str)
print("my" in str)
    
str = "decide your destiny"
print(str.split(" "))

str[0] = 'c'
print(str)


list1 = [1,2]
list2 = [4,5]
#基本运算符
print("#基本运算符")
print("list1+list2=",list1+list2)
print("list1*2=",list1*2)
#函数
print("#函数")
print("len(list1) =",len(list1))

list = [1,2,3]
print("#在列表的最后端添加元素")
list.append(4)
list.append(5)
print(list)
print("#在列表的指定位置添加元素")
list.insert(0,0)
print(list)
listn = [6,7]
list.extend(listn)
print(list)

a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(a)
a.extend(b)
print(a)

list = [1,2,3,4,5]
print("#del删除第2个元素")
del list[1]
print(list)
print("#pop删除最后一个元素")
list.pop(-1)
print(list)

list = [1,2,3,4,5]
print(1 in list)
print(2 in list)
print(6 in list)
print('1' in list)

list = [1,2,3,4,5]
print(1 not in list)		# output -> False
print(not 2 in list)		# output -> False
print(6 not in list)		# output -> True
print(not '1' in list)		# output -> True

print(list(range(4)))
print(list(range(3,7)))
print(list(range(0,10,2)))
print(list(range(0,10,3)))
print(list(range(5,-1,-1)))


array = [24, 56, 74, 97, 108]
for i in range(len(array)):
	print("第{}次循环：{}".format(i,array[i]))

i = 0
while True:
	# 输出是第几次循环
	print("第{}次循环".format(i))
	i = i + 1
	text = input(">是否退出？(y/N)")
	if text in ['y', 'Y']:
		print("退出成功")
		break


numbers = [0, 1, 2, 3, 4, 5, 6]

for number in numbers:
	if number % 5 == 0:
		continue
	print(number)

numbers = [53, 108, 97, 26, 320]
print(min(numbers))			# output -> 26
print(max(numbers))			# output -> 320
print(sum(numbers))			# output -> 604


list1 = [1, 2, 3, 4, 5, 6]
print(list(reversed(list1)))

list1 = ["element1", "element2", "element3"]
print(list(enumerate(list1)))	# output -> [(0, 'element1'), (1, 'element2'), (2, 'element3')]

list1 = ["element1", "element2", "element3"]
for i, value in enumerate(list1):
	print("No.{} element is {}".format(i,value))


dictionary = {
	"key1": "value1",
	"key2": "value2",
	"key3": "value3",
}
for key, value in dictionary.items():
	print("Value of {} is {}".format(key,value))

def test():
	print("A")
	return
a = test()
print(a)

tuple = (1, 2, 3)
print(tuple[0])
print(tuple[1])
print(tuple[2])