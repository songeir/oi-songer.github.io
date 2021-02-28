---
title: "Wannafly Camp Day 4"
tags: 
---

# Wannafly Camp Day 4

> 今天为DP专题。

<!--more-->

## 课上内容

### 烧桥计划

#### $O(n^3)$



#### $O(n^2)$

#### $O(n^{\frac{3}{2}})$

因为$ 1000 \leq a_i \leq 2000$


## 习题及讲解

题目来源：[_comet OJ_](https://www.zhixincode.com/contest/20/problems)

### A Cactus Draw

将所有的环放在同一层即可。然后处理出每个子树的宽度。

### B Diameter

这道题是一个DP。使用$dp[n]$记录$n$个点的有根树。我们先不考虑根的标号，考虑除了根以外标号最小的节点所在的子树大小为$k$，则：

$$ dp[n] = n \times \sum \frac{ dp[k] \cdot dp[n-k]}{n-k} \times C_{n-2}^{n-k-1} $$

那么，若我们使用$dp[i][j][k]$表示$i$个点的子树，最大深度为$j$，直径为$k$的方案数，则方程如下，时间复杂度为$O(n^6)$:

$$ 
\begin{align}
&dp[n][\max (p_1, p_3 + 1)][\max(p_2, p_4, p_1 + p_3 + 1)] \\ \\ =\ &n \times \sum \frac{dp[k][p_1][p_2] \cdot dp[n-k][p_3][p_4]}{n-k} \times C_{n-2}^{n-k-1} 
\end{align}$$

因为每个树都有唯一的中心，如果直径是偶数，那么中心是一个点，否则为一条边。若中心是边，那么两个子树的深度相同，否则要求最大的深度至少出现了两次。

此时，我们用$f[i][j]$表示$i$个点，深度至多为$j$的方案数；
用$g[i][j]$表示$i$个点，深度恰好为$j$的方案数。因此：

$$ f[n][i] = n \times \sum \frac{f[n-k][i]}{(n-k)} \times f[k][i-1] \times C_{n-2}^{k-1} $$

$$ g[n][i] = f[n][i] - f[n][i-1] $$

如果直径是$2j+1$,那么答案为$\sum g[k][j] \cdot g[n-k][j] \cdot C_{n-1}{k-1} $;

如果直径是$2j$，那么答案为$g[n][i] - \sum g[k][j-1] \cdot f[n-k][j-1] \cdot C_n^k$。

### C Division

对于每一个数字，求出每步操作的贡献，然后取区间最大的$k$个数字，可以通过主席树解决。不过空间不足，所以我们需要把所有的数字分到$2^k$到$2^{k+1}$分别做。时间复杂度$O(n \log n^2 + q \log n)$，空间为$O(n \log n)$。

### D Doppelblock

暴力，先搜索$X$的位置，然后再搜索数字，同时注意剪枝即可。

### E Fast Kronecker Transform

一个卷积，通过FFT加速。

### F Kropki

也是一道DP。未理解。

### G Least Common Multiple

未理解。

### H Nested Tree

虚树+树链剖分。

### I Sorting

因为$\leq x$的数字内部或者$\geq x$的数字内部的相对顺序是不会变的。那么我们便可以将所有$\leq x$的当成$0$，$\geq x$的当成$1$。这时候题目的`2`,`3`操作便变成了对$01$序列的操作。这个可以通过区间求和和区间赋值实现。

最后，当我们想要进行$1$操作时，因为$0$，$1$的相对顺序是不会变的，所以我们可以通过其位置通过前缀和直接相减得到当前的区间和。

### J Special Judge

给定$n$个点，$m$条边，判断有多少对相交的边。计算几何的基础题，不过特殊情况的判断较为复杂。
