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
