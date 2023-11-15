# Calculus Review

### 7. 矢量代数和空间解析几何

#### 数量积 向量积 混合积
空间中点到直线的距离  

+ 求点 $R$ 到直线 $PQ$ 的距离.  
    + $d=\frac{\pmb{PQ}\times \pmb{PR}}{\pmb{PQ}}$.  

四面体体积

+ 求四面体 $ABCD$ 体积
    + $V=\frac{1}{6}[\pmb{AB}\times \pmb{AC}]\cdot \pmb{AD}$.
+ **平行六面体的体积是等于相邻三边的混积**，四面体的体积是对于平行六面体的1/6.

#### 空间中的平面和直线
+ 求过已知直线 $L:\begin{cases}A_1x+B_1y+C_1z+D_1=0\\ A_2x+B_2y+C_2z+D_2=0\end{cases}$ 的平面
    + 选择用平面束求解，因为求解平面包含在平面束 $\lambda(A_1x+B_1y+C_1z+D_1)+\mu(A_2x+B_2y+C_2z+D_2)=0$ 中，结合其他条件确定 $\lambda$ 和 $\mu$ 即可
+ 平面的夹角( $\pmb n_1$ 和 $\pmb n_2$ 是两平面的法向量)
    + $\cos\theta=\frac{|\pmb n_1\cdot\pmb n_2|}{|\pmb n_1||\pmb n_2|}$ 
+ 直线的夹角( $\pmb n_1$ 和 $\pmb n_2$ 是两直线的方向向量)
    + $\cos\theta=\frac{|\pmb n_1\cdot\pmb n_2|}{|\pmb n_1||\pmb n_2|}$ 
+ 平面和直线的夹角( $\pmb n_1$ 和 $\pmb n_2$ 分别是平面的法向量和直线的方向向量)
    + $\cos\theta=\frac{|\pmb n_1\cdot\pmb n_2|}{|\pmb n_1||\pmb n_2|}$ 

#### 二次曲面
......

### 8.多元微分及其应用
#### 基础知识
全微分存在（可微）的判定

+ $dz-f_x(x_0,y_0)dx-f_y(x_0,y_0)dy$ 是否为 $\rho$ 的高阶无穷小

隐函数组的偏导数

+ 方程组 $\begin{cases}F(x,y,u,v)=0\\ G(x,y,u,v)=0\end{cases}$ 中 $\begin{cases}u=u(x,y)\\ v=v(x,y)\end{cases}$
+ $J=\frac{\partial(F,G)}{\partial(u,v)}=\displaystyle \left| \begin{matrix}\frac{\partial F}{\partial u} & \frac{\partial F}{\partial v}\\ \frac{\partial G}{\partial u} & \frac{\partial G}{\partial v} \end{matrix}\right|$
+ $\frac{\partial u}{\partial x}=-\frac{1}{J} \frac{\partial(F,G)}{\partial(x,v)}$(就是在 $J$ 中把需要求偏导的上面的变量换成下面的变量再乘 $-\frac{1}{J}$)
+ ......（同上）

方向导数

+ 对于三元函数 $f(x,y,z)$ 来说，如果它在空间一点 $P_0(x_0,y_0,z_0)$ 可微，那么沿方向 $\pmb{e}_l=(cos\alpha,cos\beta,cos\gamma)$ 的方向导数为 
+ $\frac{\partial f}{\partial l}|_{(x_0,y_0,z_0)}=f_x(x_0,y_0,z_0)cos\alpha + f_y(x_0,y_0,z_0)cos\beta + f_z(x_0,y_0,z_0)cos\gamma$.

梯度

+ 记作 $grad f(x_0,y_0)$ 或 $\nabla f(x_0,y_0)$.
+ $grad\ f(x_0,y_0) = \nabla f(x_0,y_0)= f_x(x_0,y_0)\pmb i + f_y(x_0,y_0)\pmb j$.

切平面方程

+ 函数 $F(x,y,z)=0$ 在点 $P(x_0,y_0,z_0)$ 处的切平面方程是
+ $F_x(x_0,y_0,z_0)(x-x_0)+F_y(x_0,y_0,z_0)(y-y_0)+F_z(x_0,y_0,z_0)(z-z_0)=0$. 

求极值

+ 多元函数的极值
    + 函数 $f(x,y)$ 在点 $(x_0,y_0)$ 具有偏导数且在该点有极值，那么
    + $f_x(x_0,y_0)=0\ \ f_y(x_0,y_0)=0$
    + 令$A=f''_{xx}(x_0,y_0),B=f''_{xy}(x_0,y_0),C=f''_{yy}(x_0,y_0)$
        + $AC-B^2>0$ 时有极值，且当 $A<0$ 时有极大值， $A>0$ 时有极小值
        + $AC-B^2<0$ 时无极值
        + $AC-B^2=0$ 时不确定
+ 条件极值
    + 已知平面（曲面）方程，在平面（曲面）上求函数极限
    + **拉格朗日乘数法**
        + 要找函数 $z=f(x,y)$ 在附加条件 $\phi(x,y)=0$ 下的可能极值点，先做出拉格朗日函数 $L(x,y)=f(x,y)+\lambda \phi(x,y)$，$\lambda$ 为参数，求其一阶偏导数使之为 $0$，然后与 $\phi(x,y)=0$ 联合起来。
        + $\begin{cases}
					f_x(x,y)+\lambda \phi _x(x,y)=0\\
					f_y(x,y)+\lambda \phi _y(x,y)=0\\
					\phi(x,y)=0
					\end{cases}$
    + 还有一种情况，**三元拉格朗日乘数法**求函数 $f(x,y,z)$ 在 $\phi(x,y,z,t)=0,\psi(x,y,z,t)=0$ 的条件极值
        + $L(x,y,z,t)=f(x,y,z,t)+\lambda\phi(x,y,z,t)+\mu\psi(x,y,z,t)$

#### 解题技巧
+ 当需要关于偏导数的表达式时，先将偏导数表示出来，再带入化简（8.16）

### 9.重积分

曲面的面积($z=f(x,y)$)

+ $A=\displaystyle\iint_D\sqrt{1+(\frac{\partial z}{\partial x})^2+(\frac{\partial z}{\partial y})^2}dxdy$

### 10.曲线积分和曲面积分

第一类曲线积分

+ $ds=\sqrt{x'^2(t)+y'^2(t)}dt$
+ $ds=\sqrt{x'^2(t)+y'^2(t)+z'^2(t)}dt$

第二类曲线积分

+ $\displaystyle\int_LPdx+Qdy=\int^\beta_\alpha(P(x(t),y(t))x'(t)+Q(x(t),y(t))y'(t))dt$
+ $\displaystyle\int_LPdx+Qdy=\int^\beta_\alpha(P(x(t),y(t),z(t))x'(t)+Q(x(t),y(t),z(t))y'(t)+R(x(t),y(t),z(t))z'(t))dt$

格林公式

+ 当函数 $P(x_0,y_0)$ 和 $Q(x_0,y_0)$ 在 $D$ 上有一阶连续偏导数时，则有：   $\displaystyle\iint_D(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dxdy=\oint_LPdx+Qdy$
+ 但是需要注意：**必须有连续偏导，也就是说每一点都需要有意义**

斯托克斯公式

+ 当函数 $P,Q,R$ 在 $\Sigma$ 连同边界 $T$ 上有一阶连续偏导数时，则有：   $\displaystyle\iint_D(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z})dydz+(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x})dzdx+(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})dxdy=\oint_T Pdx+Qdy+Rdz$

第一类曲面积分

+ $dS=\displaystyle\sqrt{1+(\frac{\partial z}{\partial x})^2+(\frac{\partial z}{\partial y})^2}dxdy$

第二类曲面积分

+ $\displaystyle\iint_SP(x,y,z)dydz+Q(x,y,z)dxdz+R(x,y,z)dxdy=\iint[P(x,y,z)\cos\alpha+Q(x,y,z)\cos\beta+R(x,y,z)\cos\gamma]dS$

高斯公式

+ $\displaystyle\iiint_V(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z})dxdydz=\iint _SPdydz+Qdxdz+Rdxdy$
+ 注意：$P,Q,R$ 在 $V$ 上连续，且有连续偏导
+ *等号右边应该为二重环路积分*
### 11.无穷级数

级数收敛的必要条件

+ 如果级数 $\displaystyle \sum^{\infty}_{n=1}u_n$ 收敛，则一般项趋于0  
+ $\displaystyle \lim_{n\rightarrow \infty}u_n=0$  

审敛法（以正向数列 $\displaystyle \sum^{\infty}_{n=1}u_n$ 和 $\displaystyle \sum^{\infty}_{n=1}v_n$ 为例）
+ 比较审敛法   
    +  $u_n\leq v_n\ (n=1,2,...)$时  
    + 若级数 $\displaystyle \sum^{\infty}_{n=1}v_n$ 收敛，则级数 $\displaystyle \sum^{\infty}_{n=1}u_n$ 收敛；  
    + 若级数 $\displaystyle \sum^{\infty}_{n=1}u_n$ 发散，则级数 $\displaystyle \sum^{\infty}_{n=1}v_n$ 发散。  
+ 比较审敛法的极限形式  
    + $\displaystyle \lim_{n \rightarrow\infty}\frac{u_n}{v_n}=l$  
    + $l=0$ 时若 $\displaystyle \sum^{\infty}_{n=1}v_n$ 收敛，则 $\displaystyle \sum^{\infty}_{n=1}u_n$ 收敛  
    + $l=+\infty$ 时若 $\displaystyle \sum^{\infty}_{n=1}u_n$ 发散，则 $\displaystyle \sum^{\infty}_{n=1}v_n$ 发散  
    + $0<l<+\infty$ 时$\displaystyle \sum^{\infty}_{n=1}u_n$ 和 $\displaystyle \sum^{\infty}_{n=1}v_n$ 敛散性一致  
+ 比值审敛法  
    + 如果 $\displaystyle \lim_{n\rightarrow\infty}\frac{u_{n+1}}{u_n}=\rho$  
    + $\rho<1$ 时，级数收敛  
    + $\rho>1$ 时，级数发散  
    + $\rho=1$ 时，无法判断  
+ 根值审敛法  
    + $\displaystyle\lim_{n\rightarrow\infty}\sqrt[n]{u_n}=\rho$  
    + $\rho<1$ 时，级数收敛  
    + $\rho>1$ 时，级数发散  
    + $\rho=1$ 时，无法判断  
+ 极值审敛法  
    + 如果 $\displaystyle\lim_{n\rightarrow\infty}nu_n=l>0$ 则级数发散  
    + 如果 $p>1,\displaystyle\lim_{n\rightarrow\infty}n^pu_n=l$，且 $0<l<+\infty$，级数收敛  

**$p$ 级数**

+ $\displaystyle \sum^{\infty}_{n=1}\frac{1}{n^p}$ 为 $p$ 级数  
    + 当 $p\leq1$ 时，级数发散  
    + 当 $p>1$ 时，级数收敛  
+ 证明  
    + 当 $p\leq1$ 时，用比较审敛法和调和级数（$p=1$ 时的 $p$ 级数）比较可知  
    + 当 $p>1$ 时，需要求将级数放缩为积分来求部分和，发现有边界  
+ 调和级数的证明  
    + 用反证法假设余项极限为 $0$ ，在最高项变成两倍的时候便会出现余项的极限不为 $0$ ，矛盾可知  

交错级数判敛：**莱布尼兹定理**  

+ 如果交错级数 $\displaystyle\sum^{\infty}_{n=1}(-1)^{n-1}u_n$ 满足如下条件，那么该交错级数收敛，且其和 $s\leq u_1$，其余项 $r_n$ 的绝对值 $|r_n|\leq u_{n+1}$  
    + $u_n\geq u_{n+1}\ \ (n=1,2,3,...)$  
    + $\displaystyle\lim_{n\rightarrow\infty}u_n=0$  
  
任一项级数的审敛方法（以 $\displaystyle \sum^{\infty}_{n=1}u_n$ 为例）  
+ 如果 $\displaystyle \sum^{\infty}_{n=1}|u_n|$ 收敛，则级数 $\displaystyle \sum^{\infty}_{n=1}u_n$ 绝对收敛  
+ 如果 $\displaystyle \sum^{\infty}_{n=1}u_n$ 收敛，且 $\displaystyle \sum^{\infty}_{n=1}|u_n|$ 发散，则 $\displaystyle \sum^{\infty}_{n=1}u_n$ 条件收敛  
+ 如果级数 $\displaystyle \sum^{\infty}_{n=1}u_n$ 绝对收敛，那么 $\displaystyle \sum^{\infty}_{n=1}u_n$ 必定收敛  
+ 绝对收敛的函数改变项的位置后构成的级数也收敛  

#### 幂级数
相关定义

+ 正数 $R$ 称为收敛半径， 开区间 $(-R,R)$ 称为收敛区间， 再有幂级数判断 $x=\pm R$ 处的敛散性决定收敛域是 $-R-R$ 的开区间还是闭区间  
+ 收敛半径的解  
    + $\displaystyle\lim_{n\rightarrow\infty}|\frac{a_{n+1}}{a_n}|=\rho$  
    + $R=\begin{cases}  
\frac{1}{\rho},&\rho\neq0\\
+\infty,&\rho=0\\
0,&\rho=+\infty
\end{cases}$

函数展开成幂级数

+ $e^x,\sin x,\cos x$ 采用泰勒展开 $f(x)=\displaystyle\sum^{\infty}_{n=0}\frac{f^{[n]}(x_0)(x-x_0)^n}{n!}$ 通常 $x_0=0$  
+  $\frac{1}{1-x}=\displaystyle\sum^{\infty}_{n=0}x^n$  
+ $\ln(1+x)$ 采用 $(*)$ 来做代换并积分得到   
+ $(1+x)^a$ 采用广义的二项式定理（用二项式定理来记忆）  

#### 傅里叶级数

+ $f(x)=\frac{a_0}{2}+\displaystyle\sum^{\infty}_{n=1}(a_n\cos \frac{n\pi x}{l}+b_n\sin \frac{n\pi x}{l})$
+ $\begin{cases}
a_n=\frac{2}{l}\displaystyle\int^l_{0}f(x)\cos \frac{n\pi x}{l}dx &(n=0,1,2,...)\\
b_n=\frac{2}{l}\displaystyle\int^l_0f(x)\sin \frac{n\pi x}{l}dx &(n=1,2,...)
\end{cases}$

狄利克雷定理

+ 如果 $f(x)$ 是以 $T=2l$ 为周期的周期函数，而且 $f(x)$ 在 $[-l,l]$ 上逐段光滑，那么 $f(x)$ 的傅里叶级数在任意点 $x$ 处都收敛，并且收敛于左右极限的平均值  

延拓  

+ 奇延拓  
    + 奇延拓是指将 $[0,l]$ 上的函数延拓为奇函数，再进行傅里叶展开，求得的是原函数的正弦级数  
    + $f(x)=\displaystyle\sum^{\infty}_{n=1}b_n\sin \frac{n\pi x}{l}$  
    + $b_n=\frac{2}{l}\displaystyle\int^l_0f(x)\sin \frac{n\pi x}{l}dx$  

+ 偶延拓
    + 偶延拓是指将 $[0,l]$ 上的函数延拓为偶函数，再进行傅里叶展开，求得的是原函数的余弦级数  
    + $f(x)=\frac{a_0}{2}+\displaystyle\sum^{\infty}_{n=1}a_n\cos \frac{n\pi x}{l}$  
		+ $a_n=\frac{2}{l}\displaystyle\int^l_{0}f(x)\cos \frac{n\pi x}{l}dx$  