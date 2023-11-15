### How to design CPU?
+ 理解ISA eg. RISC-V
    + CPU设计需要知道指令执行的规则是什么
    + 指令集(IS)：CPU能够执行的所有操作指令的集合
    + 指令集架构(ISA)：指令集设计的原则
    + RISC-V
        + opcode
        + rs1
        + rs2
        + rd
        + funct
        + immediate
+ 理解CPU指令执行流程
    + 取指(Fetch)：
        + 从指令内存中取指
        + 将PC赋值到下一条指令(PC+4)
    + 解码(Instruction) & 读取操作数(Read Operand)：
    + 执行(Executive Control)
+ 构建DataPath
    + 在指令执行时观察数据流动
+ 构建controller

### 单周期CPU

### 流水线CPU(pipeline)
+ 一项任务有一系列阶段
+ 阶段之间有关联 wash before dry
+ 多个任务overlapping stages
+ simulaneously use diff resource to speed up
+ 最慢的阶段决定了最终时间

5个阶段

+ IF: Instruction fetch from memory取指
+ ID: Instruction decode & register read 译码&读寄存器
+ EX: Execute operation or calculate address 执行
+ MEM: 访存
+ WB写回

### 流水线效率的衡量
#### 吞吐量(TP, Troughput):

$$TP=\frac{n}{T}(n表示指令条数，T表示运行总时长)$$

当$n>>m$时，TP达到最大，几位最大吞吐量：

$$TP_{max}=\frac{1}{\delta t_0}$$

#### 加速比(Speedup)

$$Sp=\frac{Execution Time_{non-piplined}}{Execution Time_{piplined}}$$

$$Sp=\frac{n\ m \cdot \delta t_0}{(m+n-1)\cdot \delta t_0}=\frac{n\cdot m}{m+n-1}$$

当$n>>m$时，$Sp_{max}=m$

#### 效率(effiency)

$\eta = \frac{Sp}{m}$



a1\*b1 a2\*b2 a3\*b3 a4\*b4


times: 4+2 t
add: 1+4+4

$$TP=\frac{7}{15\delta t}$$

$$Sp=\frac{4*3+3*4}{15}=1.6$$

!!! warning "周期问题"
	4\*3+3\*4计算的并不是单周期CPU，由于前半段加法周期为$4*\Delta t$，而后半段乘法周期为$3*\Delta t$，但是做题就按逐条执行。
	
$$\eta=\frac{4*3+3*4}{5\times15\Delta t}=32\%$$