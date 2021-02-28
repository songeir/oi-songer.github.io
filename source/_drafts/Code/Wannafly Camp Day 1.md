---
title: "Wannafly Camp Day 1"
tags: 
---

# Wannafly Camp Day 1

> 。。。

<!--more-->

## 题目及分析

### A Erase Nodes

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/A?problem_id=134)

* 树上的版本： $(u,v)$产生贡献的概率为$\frac{1}{dist(u,v)+1}$
* 外向树上的版本：$(u,v)$产生贡献是至少有一条路径
* 不走环的部分：树分治+NTT
* 走环的版本：区间分支+NTT

### B Erase Numbers III

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/B?problem_id=135)



### C Fibonacci Strikes Back

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/C?problem_id=136)

与**模意义下的二次方程的解数**有关。

### D Honeycomb

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/D?problem_id=137)

### E Power of Function

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/E?problem_id=138)

我们发现，其实每个点在$k$固定时可以看为到点$1$的距离为$m$。然后我们可以用$k$进制来表示所有的数，我们可以发现一次移动，其实等价于将该$k$进制数右移一位（当且仅当最右一位为$0$），或者等价于将某个位置的数减一（当且仅当该位不为$0$）。然后我们便可以针对任意一个数计算出它对应的$m$。其等于每位和加位数减二。

### F Quicksort

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/F?problem_id=139)

使用DP来解决。使用$dp[x][y]$表示一个长度为$x$的数组经过$y$次快排后的逆序对数。那么:

$$ dp[x][y] = \frac{\sum dp[x-1][y-1] }{} $$(没看清)

此外，还有一个由概率推出的公式:

$$ dp[l][0] = \frac{l*(l-1)}{4} $$

### G Routes

### H Cosmic Cleaner

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/H?problem_id=141)

这题是一个朴素的计算几何题，主要是求两个球的交集。这个交集可以由两个相交的球的球缺来组成，用数学方法计算即可。

球缺的体积如下:

$$ \pi H^2 \left( R - \frac{H}{3} \right) $$

### I Square Subsequences

### J Square Substrings

### K Sticks

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/K?problem_id=144)

这题就是一道暴力搜索题，但是卡常较为严重，所以需要用各种方法来减小常数即可。

### L Pyramid

题目来源: [_comet OJ_](https://www.zhixincode.com/contest/9/problem/L?problem_id=145)

没听懂。。。