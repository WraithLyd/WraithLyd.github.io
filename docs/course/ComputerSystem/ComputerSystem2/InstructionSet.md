## 指令集设计原则
兼容性
多功能性
高效率性
安全性
### ISA的分类
针对CPU的内部存储可以将ISA分为：栈型、累加器型、寄存器型

!!! note "架构类型"
	栈架构、累加器架构、通用型寄存器架构(General-Purpose Register Architecture)

#### 栈架构(Stack Architecture)
Implicit Operands
在栈顶执行(the **T**op **O**f the **S**tack, TOS)
第一个操作数从栈顶移除，第二个操作数被替换为结果。
**哪个操作数在前面先push哪个寄存器。**
??? example "执行A+B"
	push A
	push B
	add
	pop C

	结果输出在C中
??? example "执行A*(B+C)"
	push A
	push B
	push C
	add
	mul

	结果储存在栈中
I
#### 累加器架构(Accumulator Architecture)
累加器架构拥有一个临时存储单元，先将第一个操作数放到临时存储单元中，然后将其与另一个操作数直接就像处理。
??? example "执行A+B"
	load A
	add	B
	store C

	A存在临时存储单元中，计算出结果后结果替换A被放置在临时存储单元中，最后经过store结果输出在C中.

#### 通用目的寄存器架构(General-Purpose Register Architecture)
只有显式操作数

通用目的寄存器还会分为几类，常规的两类如：
+ 寄存器-内存架构(Register-memory architecture)**（RM架构）**
任何的指令都可以访问内存
+ 读写架构(Load-store architecture)**（RR架构）**
只有load和store指令可以访问内存


??? example "以RM架构为例执行A+B"
	load R1, A
	add	R3, R1, B
	store R3, C

	一个操作数是经过寄存器赋值，而另一个操作数是直接从内存中访问。

??? example "以RR架构为例执行A+B"
	load R1, A
	load R2, B
	add	R3, R1, R2
	store R3, C

	只有load和store能够访问内存，所以所有的值都必须从内存中转存到寄存器中。

##### 通用目的寄存器架构的分类
用操作数的多少来划分类型，分别有0-3不同个数的操作数。


#### 以D=A\*B-(A+C\*B)为例了解四种架构的运算方式

=== "栈架构"
	
	```asm
	push A
	push B
	mul
	push A
	push C
	push B
	mul
	add
	sub
	pop D
	```

=== "累加器架构"
	
	```
	load B
	mul C
	add A
	store D
	load A
	mul B
	sub D
	store D 
	```
=== "RM架构"

	```
	load R1, A
	mul R1, B
	load R2, B
	mul R2, C
	add R2, A
	sub R1, R2
	store R1, D
	```

## 其他有关ISA
### 数据存放
### 控制指令流
四种控制流改变：
+ 有条件跳转(Branch)
+ 无条件跳转(Jump)
+ 程序调用
+ 程序返回

地址

## RISC-V ISA
RISC-V 寻址
+ 立即数寻址
+ 寄存器寻址
+ 基地址寻址(Base Addressing)
+ PC相关寻址(PC-relative addressing)

寄存器
+ r0 零寄存器，不会存入任何数据，当有不需要返回的地址时，可以直接将地址赋给r0而不是其他寄存器来占用空间。

## 计算机硬件操作数
32进制的系统使用字(word, 4 bytes)来作为基础单元。
RISC-V为小端序。


### 1.9 计算机进程的硬件支持
调用者保存（主函数保存）Caller Saving
被调用者保存Callee Saving

### 四条ISA设计原则

让常见的指令运行更快