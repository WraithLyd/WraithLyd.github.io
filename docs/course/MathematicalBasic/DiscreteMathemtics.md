### 1.命题逻辑
命题

+ **命题**是对确定的对象做出判断的陈述句
+ **真值**是命题真或假的属性  
+ **命题的三个识别点**是陈述句、判断、确定的对象
+ 自相矛盾不能作为命题

排中律

+ 真值是命题的固有属性，且非真即假
+ **反证法**的应用  
证明：素数有无穷多个  
证明：$\sqrt2$ 是无理数  

### 2.逻辑联接词集功能完备性
+ 逻辑连接词  
连接命题，对真值进运算的词
+ 原子命题  
不含有逻辑连接词的命题
+ 复合命题  
包括了原子命题和逻辑连接词的命题

- 常见逻辑连接词
    - 否定词：非 (not)  $\lnot$
    - 合取词：并且 (and) $\land$
    - 析取词：或 (or) $\lor$
    - 蕴涵词：如果……那么…… (if...then...) $\rightarrow$
        - $p\rightarrow q$ 中的 $p$ 称作蕴涵前件， $q$ 称作蕴涵后件
        - 在蕴涵式中，只有 $p$ 为真 $q$ 为假时，$p\rightarrow q$ 才为假，故和 $(\lnot  p \land q )$ 的真值表相同
    - 双向蕴涵词：当且仅当 (if and only if) $\leftrightarrow$
        - 当 $p$ 和 $q$ 真值相同的情况下，$p\leftrightarrow q$ 为真
    - 优先级
        - $(\lnot ) \Rightarrow (\land / \lor) \Rightarrow (\rightarrow) \Rightarrow (\leftrightarrow)$

#### 功能完备集
+ 如果任意一个真值函数都可以用仅包含某个联结词集中的联结词的命题公式表示，则称这个联结词集为功能完备集，如： 
    + $<\lnot ,\land,\lor,\rightarrow,\leftrightarrow>$  
    + $<\lnot ,\land,\lor>$  
+ 冗余联结词  
在一个联结词集中，如果某个联结词可以用集合中其他联结词来定义，则这个联结词称作冗余联结词
+ 功能完备集证明思路  
从一个已知的功能完备集中去掉冗余联结词，直到得到需证明的功能完备集 

极小功能完备集  

+ 如果一个功能完备集中不含冗余联结词，则称这个功能完备集为极小的，如：
    + $\{\lnot ,\rightarrow\}$
    + $\{\lnot ,\lor\}$
    + $\{\lnot ,\land\}$

仅包含单个联结词的功能完备集  

+ 定义联结词 $\downarrow$
+ $p\downarrow q\Leftrightarrow\lnot (p\lor q)$
+ $\{\downarrow\}$ 是功能完备集
+ 证明思路：用 $↓$ 去定义功能完备集中每一个联结词，如 $\{\lnot ,∨\}$
### 3.真值表
#### 真值表
+ 命题的真值
    + 为真用1来表示
    + 为假用0来表示
+ 逻辑连接词用**真值表**来定义
+ 真值表的内容
    + 原子命题的真值组合 $(0,1)$
    + 经过逻辑连接词作用后的真值
#### 命题公式
+ 定义
    + 命题常元和命题变元是命题公式，称作原子公式
    + 如果 $A$ ，$B$ 是命题公式，那么$（\lnot A）$，$（A∧B）$，$A∨B$，$（A→B）$，$A↔B$也是命题公式
    + 只有有限步引用上述两条所组成的符号串是命题公式
+ 赋值
    + 成真赋值  
当公式 $A$ 对赋值 $\alpha$ 为真时，称 $\alpha$ 是 $A$ 的成真赋值，或者 $\alpha$ 弄真 $A$，记做 $\alpha(A)=1$ 
    + 成假赋值  
当公式 $A$ 对赋值 $\alpha$ 为假时，称 $\alpha$ 是 $A$ 的成假赋值，或者 $\alpha$ 弄假 $A$，记做 $\alpha(A)=0$
+ 分类
    + 重言式（永真式）  
命题变元所有赋值都是命题公式的成真赋值
    + 矛盾式（永假式、不可满足式）  
命题变元所有赋值都是命题公式的成假赋值
    + 可满足式  
命题变元至少有一个成真赋值
    + **永真式也是可满足式**  
### 4.逻辑等价式
+ 定义  
当命题公式 $A\leftrightarrow B$ 是重言式时，则称 $A$ 逻辑等价于 $B$，记作 $A\Leftrightarrow B$
+ 一些重要的逻辑等价式（$A$，$B$，$C$ 是任意公式）
    + E1: $\lnot  \lnot  A\Leftrightarrow A$ （双重否定律）
    + E2: $A \land A \Leftrightarrow A,\ A\lor A \Leftrightarrow A$ （幂等律）
    + E3: $A∨B\Leftrightarrow B∨A，A∧B\Leftrightarrow B∧A$（交换律）
    + E4: $(A∨B)∨C \Leftrightarrow A∨(B∨C)，(A∧B)∧C\Leftrightarrow A∧(B∧C)$（结合律）
    + E5: $A∧(B∨C)\Leftrightarrow (A∧B)∨A∧C,A∨(B∧C)\Leftrightarrow (A∨B)∧(A∨C)$（分配律）
    + E6: $\lnot (A∨B)\Leftrightarrow \lnot A∧\lnot B，\lnot (A∧B)\Leftrightarrow \lnot A∨\lnot B$（德摩根律）
    + E7: $A∨(A∧B)\Leftrightarrow A，A∧(A∨B)\Leftrightarrow A$（吸收律）
    + E8: $A→B\Leftrightarrow\lnot A∨B$（蕴涵等值式）
    + E9: $A↔B\Leftrightarrow(A→B)∧(B→A)$（等价等值式）
    + E10: $A∨T\Leftrightarrow T，A∧F\Leftrightarrow F$（零律）
    + E11: $A∨F\Leftrightarrow A，A∧T\Leftrightarrow A$（同一律）
    + E12: $A∨\lnot A\Leftrightarrow T，A∧\lnot A\Leftrightarrow F$（排中律和矛盾律）
    + E13: $\lnot T\Leftrightarrow F，\lnot F\Leftrightarrow T$
    + E14: $A∧B→C\Leftrightarrow A→B→C$
    + E15: $A→B\Leftrightarrow \lnot B→\lnot A$（假言易位）
    + E16: $A→B∧A→\lnot B\Leftrightarrow \lnot A$（归谬论）
    + E17: $A↔B\Leftrightarrow (A∧B)∨(\lnot A∧\lnot B)$（等价等值式2）
### 5.逻辑蕴涵式
+ 定义  
当命题公式 $A\rightarrow B$ 为重言式时，则称 $A$ 逻辑等价 $B$，记作 $A \Rightarrow B$
+ 一些重要的逻辑蕴涵式（A，B，C，D是任意公式）
    + I1: $A\Rightarrow A∨B$
    + I2: $A∧B\Rightarrow A$
    + I3: $A∧(A→B)\Rightarrow B$
    + I4: $(A→B)∧\lnot B\Rightarrow\lnot A$
    + I5: $\lnot A∧(A∨B)\Rightarrow B$
    + I6: $(A→B)∧(B→C)\Rightarrow A→C$
    + I7: $(A→B)∧(C→D)\Rightarrow(A∧C)→(B∧D)$
    + I8: $(A↔B)∧(B↔C)\Rightarrow A↔C$

>**逻辑等价式和逻辑蕴涵式的区别**  
> 逻辑等价式 $\Leftrightarrow$ 左右两边的真值相等  
> 逻辑蕴涵式 $\Rightarrow$ 当左边为真的时候可以推出右边，而如果左边为假，逻辑蕴涵式一定为真，右边可真可假  

> **逻辑等价式和逻辑蕴涵式的性质**：自反性、对称性、传递性  

### 6.代入原理、替换原理
+ 带入原理
    + 将重言式 $A$ 中的某个命题变元 $p$ 的出现都代换为命题公式 $B$，得到的命题公式仍为重言式
    + **必须代换所有的命题变元 $p$**
+ 替换原理
    + 将命题公式中的子公式替换为逻辑等价的公式，得到的命题公式真值和原真值相同
    + **不要求全部替换**
### 7.（主）合取范式、（主）析取范式
#### 基础概念
+ 文字  
命题常元、变元和它们的否定
+ 析取子句  
文字或者若干文字的析取
+ 合取子句  
文字或者若干文字的合取
+ 互补文字对  
指一对正文字和负文字
#### 析取范式和合取范式
析取范式  

+ 如果 $A'\Leftrightarrow A$ 且  $A'$ 为合取子句或者若干合取子句的析取，那么 $A'$ 称为 $A$ 的析取范式

合取范式  

+ 如果 $A'\Leftrightarrow A$ 且  $A'$ 为析取子句或者若干析取子句的合取，那么 $A'$ 称为 $A$ 的合取范式

特例  

+ $p→q$ 的析取范式和合取范式都可以为 $\lnot p∨q$
    + $\lnot p∨q$ 是合取子句 $\lnot p$ 和 $q$ 的析取
    + $\lnot p∨q$ 也是析取子句

求析取范式或合取范式的一般步骤  

+ 消去公式中的联结词 $\rightarrow$ 和 $\leftrightarrow$
    + $p→q$ 化为 $\lnot p∨q$（蕴涵等值式）
    + $p↔q$ 化为 $(\lnot p∨q)∧(p∨\lnot q)$ 或者 $(p∧q)∨(\lnot p∧\lnot q)$（等价等值式）
+ 利用德摩根律将否定联结词 $\lnot$ 向内深入，最后只作用于文字  
+ 再将 $\lnot \lnot  p$ 化简为 $p$  
+ 利用分配律，最后得到需要的析取或合取范式
#### 主析取范式和主合取范式
主析取范式  

+ 如果 $A'$ 是 $A$ 的析取范式，且 $A'$ 中每一个合取子句里 $p1，p2，...，pn$ 均恰出现一次，那么公式 $A'$ 称作公式 $A(p1，p2，...，pn)$ 的主析取范式
+ 极小项只有唯一的成真赋值
+ 极小项的数量为 $N=2^n$
+ 由极小项组成的主析取范式的数量为 $2^N$

主合取范式  

+ 如果 $A'$ 是 $A$ 的合取范式，且 $A'$ 中每一个析取子句里 $p1，p2，...，pn$ 均恰出现一次，那么公式 $A'$ 称作公式 $A(p1，p2，...，pn)$ 的主合取范式
+ 极大项只有唯一的成假赋值
+ 极大项的数量为 $N=2^n$
+ 由极大项组成的主合取范式的数量为 $2^N$
### 8.谓词逻辑
个体  

+ 谓词逻辑中将一切讨论的对象都称作个体  

个体常元  

+ 确定的个体，常用 $a,b,c$ 来表示  

个体变元  

+ 不确定的个体，常用 $x,y,z,u,v,w$ 来表示

个体域  

+ 被讨论对象的全体

全总域  

+ 包含一切对象的个体

谓词

+ 表示个体性质或关系的语言成分
+ 元数

谓词中可以防止个体的空位个数称为谓词的元数

+ 谓词命名式
将谓词中的个体空位用变元字母代替，常用大写字母 $P,Q,R$ 来代表谓词，命名形式如同 $P(x),Q(x,y)$
+ 谓词填式
将谓词中的个体空位用个体变元或常元代替

> 谓词填式在形式上和命名式相同，但是属于不同的概念，需要根据上下文加以区分

> **区别**
> 类似于编程语言中的函数说明（形参）和函数调用（实参）之区分

#### 量词
$\forall \ \&\ \exists$

+ “所有”为全称量词，记作 $\forall$
+ “有一些”为存在量词，记作 $\exists$
+ 量词作用于谓词时需要引入一个指导变元，同时放在量词后面和谓词填式中：$\forall xP(x),\exists xP(x)$

约束变元和自由变元

+ 指导变元是不可取值代入的，称作约束变元，约束变元可以改名而不改变语句含义
+ 可以取值代入的个体变元称作自由变元

辖域

+ 量词所作用的谓词或者复合谓词表达式，称作量词的辖域
#### 谓词公式
+ 原子公式
    + 谓词填式和谓词常元（零元谓词）式公式，称为原子公式
+ 谓词公式
    + 由五个联结词和量词链接的有限个原子公式称为谓词公式  

>$\forall x A$ ，$\exists x A$ 中公式 $A$ 可以不包含变元 $x$ ，此时 $\forall x A$ ，$\exists x A$ 均等价于 $A$

谓词公式成为命题

+ 如果给定个体域，公式中的所有谓词都有明确意义，公式中的所有自由变元取定个体，谓词公式就成为一个命题
谓词公式真值条件
+ 给定个体域
+ 公式中的所有谓词都有明确意义（解释）
+ 公式中的所有自由变元取定个体
+ 永真式是逻辑中重要的概念

永真式

+ 给定个体域 $D$，公式 $A$ 中各谓词符号的解释 $I$，如果 $A$ 中的自由变元 $x_1,…,x_n$ 分别取值 $u_1,…,u_n$ 时 $A$ 为真，称 $A$ 在 $u_1,…,u_n$ 处为真
+ 如果 $A$ 在自由变元的任何取值下都为真，称 $A$ 在解释 $I$ 下为真
+ 如果 $A$ 在每个解释 $I$ 下均为真，称 $A$ 在 $D$ 上永真
+ 如果 $A$ 在任何个体域 $D$ 永真，称 $A$ 永真

可满足式

+ 如果对于某个个体域，谓词的某个解释，和自由变元的某个取值，公式 $A$ 在此处取值为真，则称公式 $A$ 是可满足式

永假式

+ 公式 $A$ 不可满足时也称 $A$ 是永假式

谓词公式的逻辑等价与逻辑蕴涵

+ 逻辑等价
    + $A \Leftrightarrow B$ 当且仅当对一切个体域，解释和变元取值状况，$A$ 和 $B$ 都具有相同的真值
+ 逻辑蕴涵
    + $A \Rightarrow B$ 当且仅当对一切个体域，解释，一切使 $A$ 成真的变元取值状况，均使 $B$ 成真
### 9.谓词演算的永真式
当A不含变元x时

+ $\forall x A \Leftrightarrow A，\exists x A \Leftrightarrow A$
+ $\forall x A x \Rightarrow A x ，A x \Rightarrow \exists x A x ，\forall x A x \Rightarrow \exists x A x$
+ $\lnot \exists x \lnot A x \Leftrightarrow \forall x A x$
+ $\lnot \forall x \lnot A x \leftrightarrow \exists x A x$
+ $\lnot \exists x A x \Leftrightarrow \forall x \lnot A x$
+ $\lnot \forall x A x \Leftrightarrow \exists x \lnot A x$

当公式B不含变元x时

+ $\forall x A x ∨ B \Leftrightarrow \forall x (A x ∨ B)$
+ $\forall x A x ∧ B \Leftrightarrow \forall x (A x ∧ B)$
+ $\exists x A x ∨ B \Leftrightarrow \exists x (A x ∨ B)$
+ $\exists x A x ∧ B \Leftrightarrow \exists x (A x ∧ B)$

当公式B含变元x时

+ $\forall x (A (x) ∧ B (x)) \Leftrightarrow \forall x A(x)∧ \forall x B(x)$
+ $\forall x A (x) ∨ \forall x B(x) \Rightarrow \forall x(A(x)∨B(x))$
+ $\exists x (A (x) ∧ B (x)) \Rightarrow \exists x A(x)∧ \exists x B(x)$
+ $\exists x (A (x) ∨ B (x)) \Rightarrow \exists x A(x)∨ \exists x B(x)$

量词的组合与顺序

+ $\forall x\forall y A (x, y) \Leftrightarrow \forall y\forall x A (x, y)$
+ $\forall x\forall y A (x, y) \Rightarrow \exists y\forall x A (x, y)$
+ $\exists y\forall x A (x, y) \Rightarrow \forall x\exists y A (x, y)$
+ $\forall x\exists y A (x, y) \Rightarrow \exists y\exists x A (x, y)$
+ $\exists x\exists y A (x, y) \Leftrightarrow \exists y\exists x A (x, y)$

### 10.公理化集合论
集合

+ 作为整体识别的、确定的、互相区别的一些对象的总体
    + 整体识别：不再分割
    + 确定：属于或者不属于整体
    + 互相区别：各异的对象
    + 组成集合的对象称为成员（member）或者元素（element）

分类

+ 空集：没有任何元素的特定集合称为空集，记作 𝜙
    + $\phi = \{\ \} = \{x｜x ≠ x\}$
+ 有限集（finite sets）：空集和只含有限多个元素的集合称作有限集
+ 否则，称作无限集（infinite sets）

基数

+ 有限集合中成员的个数称作集合的基数（无限集合的基数定义更为复杂），集合 $A$ 的基数记作 $|A|$

子集合

+ 集合 $A$ 称作集合 $B$ 的子集合，如果 $A$ 的每一个元素都是 $B$ 的元素
+ $\forall x (x ∈ A → x ∈ B)$
+ $A$ 是 $B$ 的子集，记作 $A ⊆ B$

#### 三大基本原理
##### 外延公理
+ 两个集合A和B相等当且仅当它们具有相同的元素
+ $A = B \Leftrightarrow \forall x (x ∈ A \Leftrightarrow x ∈ B)$
+ $0,1 = 1,0 = \{x｜x = 0 ∨ x = 1\}$
+ 说明集合元素的无序性，以及集合表示形式的不唯一性

##### 概括公理
+  对于任意个体域 $U$，任一谓词公式 $P$ 都确定一个以该域中的对象为元素的集合 $S$
+  $S = \{x | x ∈ U ∧ P(x)\}$
+  规定了集合成员的确定性
+ 空集：$P(x)$ 为永假式

##### 正规公理
+ 不存在集合$A1，A2，A3， ... ...$ 使得 $... ∈ A3 ∈ A2 ∈ A1$
+ 直观来说就是集合的有限可分，个体域的元素是“基本粒子”


> 集合的两个基本关系：隶属和包含
### 11.集合基本运算
集合运算指以集合为运算对象，结果还是集合的运算

+ 并运算（Union）：$∪$
+ 交运算（Intersection）：$∩$
+ 差运算（Difference）：$−$
+ 补运算（Complement）：$\sim$

运算律（后续补上）

幂集运算
+ 对于任意集合 $A$，$\rho(A)$ 称作 $A$ 的幂集，定义为 $\rho (A) = \{x｜x ⊆ A\}$
+ 幂集的基数：$|\rho (A) |=2^{|A|}$
### 12.归纳定义
归纳定义（inductive definition）：

+ 基础条款：规定某些元素为待定义集合成员，集合其他元素可以从基本元素出发逐步确定
+ 归纳条款：规定由已确定的集合元素去进一步确定其他元素的规则
+ 终极条款：规定待定义集合只含有基础条款和归纳条款所确定的成员

> 基础条款和归纳条款称作“完备性条款”，必须保证毫无遗漏产生集合中所有成员。
> 终极条款又称作“存粹性条款”，保证集合中仅包含满足完备性条款的那些对象
### 13.有序组
二元有序组

+ 设a，b为任意对象，称集合族${ a , {a, b}}$为二元有序组，简记为$< a, b >$
+ 称a为$<a,b>$的第一分量，b为第二分量
### 14.笛卡尔积
定义

+ 对任意集合 $A_1, A_2,…, A_n$， $A_1×A_2$ 称作集合 $A1, A2$ 的笛卡尔积，定义如下：
    + $A_1×A_2 = \{< u, v > ｜u ∈ A_1, v ∈ A_2\}$
    + $A_1×A_2×⋯×A_n = (A_1×A_2×⋯×A_{n-1})×An$

性质

+ 不满足交换律
    + $A×B ≠ B×A$
+ 不满足结合律
    + $A×(B×C) ≠ (A×B)×C$
+ 笛卡尔积对集合运算的分配律
设 $A，B，C$ 为任意集合，# 表示 $∪,∩$ 或者 $-$ 运算，那么
    + $A× B\#C = A×B\#(A×C)$
    + $B\#C ×A = B×A \#(C×A)$

笛卡尔积的基数

+ 对于任意有限集合 $A1, A2,…, An$，有 $|A_1×A_2×⋯×A_n | = |A_1| ∗ |A_2| ∗ ⋯∗ |A_n |$
### 15.关系、关系矩阵、函数
#### 关系
+ R称为集合 $A_1, A_2,…, A_{n-1}$ 到$A_n$ 的 $n$ 元关系，如果 $R$ 是$A_1×A_2×⋯×A_n$ 的一个子集，当 $A_1 = A_2 = ⋯ = A_n$ 时，也称 $R$ 为 $A$ 上的 $n$ 元关系
+ 如果 $R$ 是 $A×B$ 的一个子集，称 $R$ 是 $A$ 到 $B$ 的二元关系，如果 $R$ 是 $A×A$ 的一个子集，则称 $R$ 是 $A$ 上的二元关系
#### 关系矩阵
+ 前域和陪域都是有限集合
+ 设关系 $R ⊆ A×B，A = {a1,…, am}， B = {b1,…, bn}$
+ 关系 $R$ 的关系矩阵 $M_R$ 的定义：
    + $m_{ij}=1$ 当且仅当 $a_iRb_j$
    + $m_{ij}=0$ 当且仅当 $\lnot a_iRb_j$
### 16.等价关系、等价类、划分
#### 等价关系
+ 等价关系 $R$ 定义为：$A$ 上的自反、对称、传递的二元关系
+ 设 $R$ 为 $A$ 上的等价关系，对于每个 $a ∈ A$ ，$a$ 的等价类记做 $[a]_R$（简记$[a]$），定义为： $[a]_R = \{x|x ∈ A ∧ xRa\}$

!!! note "" 
    <br><br>
    <div align="center" style="font-size:32px;font-weight:bold">
        ~『以下内容待补充』~
    </div>
    <br><br>
### 17.序关系、哈斯图
### 18.图论、图的同构
### 19.欧拉图、哈密尔顿图
### 20.二分图、匹配算法
### 21.抽象代数、代数结构、同态
### 22.群、环、域
### 23.语言分析、有限状态自动机
### 24.图灵机、停机问题