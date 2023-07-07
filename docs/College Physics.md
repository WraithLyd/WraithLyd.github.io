# College Physics
### 热力学基础
#### 准静态过程、可逆过程、不可逆过程
+ 无摩擦的准静态过程都是可逆过程
+ 实际上的宏观过程都是不可逆过程
#### 热力学第一定律

$$dQ=dE+dW,\ \ \ \ \ Q=E_2-E_1+W$$   

+ 理想气体的热力学增量:  $E_2-E_1=\displaystyle\frac{M}{\mu}C_{V,m}(T_2-T_1)$   
+ 内能:  $E=\displaystyle\frac{i}{2}\nu RT$   
+ 准静态理想气体做功: $W=\displaystyle\int_{V_1}^{V_2}pdV$   
+ 热量: $Q=\displaystyle\frac{M}{\mu}C_m(T_2-T_1)$

##### 四种准静态过程   

+ 等体（$V=C$）：
    + 过程方程：$\displaystyle\frac{p}{T}=C$
    + 能量转换关系：$Q=E_2-E_1$
    + 热力学增量：$E_2-E_1=\displaystyle\frac{M}{\mu}C_{V,m}(T_2-T_1)$
    + 功：$W=0$
    + 热量：$Q=\displaystyle\frac{M}{\mu}C_{V,m}(T_2-T_1)$
+ 等压（$p=C$）：
    + 过程方程：$\displaystyle\frac{V}{T}=C$
    + 能量转换关系：$Q=E_2-E_1+W$
    + 热力学增量：$E_2-E_1=\displaystyle\frac{M}{\mu}C_{V,m}(T_2-T_1)$
    + 功：$W=p(V_2-V_1)=\displaystyle\frac{M}{\mu}R(T_2-T_1)$
    + 热量：$Q=\displaystyle\frac{M}{\mu}C_{p,m}(T_2-T_1)$
+ 等温（$T=C$）：
    + 过程方程：$pV=C$
    + 能量转换关系：$Q=W$
    + 热力学增量：$E_2-E_1=0$
    + 功：$W=\displaystyle\frac{M}{\mu}RT\ln(\frac{V_2}{V_1})=\displaystyle\frac{M}{\mu}RT\ln(\frac{p_2}{p_1})$
    + 热量：$Q=\displaystyle\frac{M}{\mu}RT\ln(\frac{V_2}{V_1})=\displaystyle\frac{M}{\mu}RT\ln(\frac{p_2}{p_1})$
+ 绝热（$dQ=0$）：
    + 过程方程：$pV^\gamma=C,TV^{\gamma-1}=C,p^{\gamma-1}T^{-\gamma}=C$
    + 能量转换关系：$E_2-E_1=-W$
    + 热力学增量：$E_2-E_1=\displaystyle\frac{M}{\mu}C_{V,m}(T_2-T_1)$
    + 功：$W=\displaystyle\frac{M}{\mu}C_{V,m}(T_2-T_1)=\frac{p_1V_1-p_2V_2}{\gamma-1}$
    + 热量：$Q=0$
#### 热容量
+ 热容量: $C=\displaystyle\frac{dQ}{dT}$   
+ 比热容: $c=\displaystyle\frac{1}{M}\frac{dQ}{dT}$   
+ 摩尔热容: $C_m=\displaystyle\frac{1}{\nu}\frac{dQ}{dT}$   
+ 理想气体定体摩尔热容: $C_{V,m}=\frac{i}{2}R$   
+ 理想气体定压摩尔热容: $C_{p,m}=\frac{i+2}{2}R$
+ 比热容比: $\gamma=\displaystyle\frac{C_{p,m}}{C_{V,m}}=\frac{i+2}{i}$      
+ 迈尔公式   
    + $C_{p,m}-C_{V,m}=R$   
#### 循环
+ 循环特征
    + $\Delta E=0,\ \ W=Q_1-Q_2$
+ 热机效率
    + $\eta=\displaystyle\frac{W}{Q_1}=\frac{Q_2}{Q_1}$
+ 制冷机制冷系数
    + $\omega=\displaystyle\frac{Q_2}{W}=\frac{Q_2}{Q_1-Q_2}$
+ 卡诺循环
    + $\eta_卡=1-\displaystyle\frac{T_2}{T_1}$
+ 卡诺逆循环
    + $\omega_卡=\displaystyle\frac{T_2}{T_1-T_2}$
#### 热力学第二定律
+ 一切实际的宏观过程都是不可逆的
+ 在孤立系统或绝热系统中，$dS\geq0$
+ 总是向无序性增加的方向进行
#### 熵
+ 熵变
    + $dS=\displaystyle\frac{dQ_r}{T},\ \ S_B-S_A=\int_A^B\frac{dQ_r}{T}$
+ 玻尔兹曼关系
    + $S=k\ln(\Omega)$
### 气体动理论
#### 理想气体
+ 理想气体状态方程
    + $pV=\displaystyle\frac{M}{\mu}RT=\nu RT,\ \ p=nkT$
    + $n$ 位分子数密度， $k$ 为玻尔兹曼常量
+ 理想气体压强公式
    + $p=\displaystyle\frac{1}{3}nm\overline{v^2}=\frac{2}{3}n\overline{\epsilon_t}$
+ 理想气体温度方程
    + $\overline{\epsilon_t}=\displaystyle\frac{3}{2}kT$
+ 理想气体热力学能
    + $E=\displaystyle\frac{i}{2}\nu RT(i=3,5,6)$
#### 三种统计速率
+ 方均根速率: $\displaystyle\sqrt{\overline{v^2}}=\sqrt{\frac{3RT}{\mu}}$
+ 最概然速率: $\displaystyle\overline{v}=\sqrt{\frac{2RT}{\mu}}$
+ 平均速率: $\displaystyle v_p=\sqrt{\frac{8RT}{\pi\mu}}$
#### 碰撞频率和平均自由程
+ 碰撞频率: $\overline{Z}=\sqrt{2}\pi d^2\overline{v}n$
+ 平均自由程: $\overline{\lambda}=\displaystyle\frac{1}{\sqrt{2}\pi d^2n}=\frac{kT}{\sqrt{2}\pi d^2p}$
### 机械波
#### 简谐波
+ 平面简谐波: $y=A\displaystyle\cos[\omega(t-\frac x u)+\phi]$
+ 球面简谐波: $y=\displaystyle\frac{A}{r}\cos[\omega(t-\frac r u)+\phi]$
#### 能量和能流
+ 能量密度
    + $w=\rho A^2\omega^2\sin^2\omega(t-\displaystyle\frac x u)$
    + $w_{max}=\rho A^2\omega^2$
    + $\overline w=\displaystyle\frac 1 2\rho A^2\omega^2$
+ 波的强度
    + $I=\overline w u=\displaystyle\frac 1 2\rho A^2\omega^2u$
#### 波的干涉
+ 条件
    + 频率相同
    + 振动方向相同
    + 相位差恒定
    + $\Delta\varphi=\varphi_1-\varphi_2-2\pi\displaystyle\frac{r_2-r_1}\lambda$ 为 $\pi$ 的整数倍，奇数为相消，偶数为相长
+ 干涉波强度分布
    + $I=I_1+I_2+2\sqrt{I_1I_2}\cos\Delta\varphi$
#### 多普勒效应
+ $\nu_r=\displaystyle\frac{u\pm v_r}{u\mp v_s}\nu_s$
+ ($\nu$ means frequency)
### 静电场
#### 库仑定律
+ $\pmb F=\displaystyle\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\pmb{\hat r}$
+ $\pmb E=\displaystyle\frac {\pmb F}{q_0}=\frac{1}{4\pi\varepsilon_0}\frac{q_0}{r^2}\pmb{\hat r}$$
#### 高斯定理
+ 电通量
    + $\Delta\varPhi_E=E\Delta S\cos\theta=\pmb E\cdot\Delta \pmb S$
    + $\varPhi_E=\displaystyle\int_Sd\varPhi_E=\int_S\pmb E\cdot d\pmb S$
+ 高斯定理
    + 针对闭合曲面 $S$
    + $\displaystyle\oint_S\pmb E\cdot d\pmb S=\frac 1 {\varepsilon_0}\sum_i{q_{i(内)}}$