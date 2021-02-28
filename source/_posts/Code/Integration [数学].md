---
title:Integration [数学]
date:2019-08-25 10:12:45
tags:
---

# Integration [数学]

## 2019牛客 第一场 B

<!--more-->

题目来源：[_Nowcoder_](https://ac.nowcoder.com/acm/contest/881/B)

## 分析

这道题就是一道纯粹的数学题。。题目要求计算如下公式：

$$ \frac{1}{\pi} \int_0^{\infty} \frac{1}{\prod_{i=1}^n (a_i^2 + x^2)} dx $$

首先，我们先假设一个变量：

$$ c_i = \frac{1}{\prod_{j \neq i}(a_j^2 - a_i^2)}$$

那么，其实第一个公式便可以进行如下的化简：

$$\begin{aligned}
&\ \frac{1}{\pi} \int_0^{+\infty} \frac{1}{\prod_{i=1}^n (a_i^2 + x^2)} dx \\
= &\ \frac{1}{\pi} \int_0^{+\infty} \sum \frac{c_i}{a_i^2 + x^2} dx (\text{此处由题解给出，我实在不会证}) \\
= &\ \frac{1}{\pi} \sum \int_0^{+\infty} \frac{c_i}{a_i^2 + x^2} dx \\
= &\ \frac{1}{\pi} \sum \left( \frac{c_i}{a_i} \times \left. \arctan(x/a_i) \right|_0^{+\infty} \right) \\
= &\ \frac{1}{\pi} \sum \frac{c_i}{2a_i} \pi  
\end{aligned}$$

### 实现细节

这道题主要由两个细节问题：

1. 不能频繁的进行取乘法逆元操作，否则会超时。应先乘在一起，然后再求逆元。
2. 注意$a_j^2 - a_i^2$可能为负数。

## 代码

```C++
#include <iostream>

#define MAXN 1010
#define MOD 1000000007

using namespace std;

long long pow(long long x, long long n, long long mod)
{
    long long ret = 1;
    long long t = x % mod;

    while (n)
    {
        if (n & 1)
            ret = ret * t % mod;

        n /= 2;
        t = t * t % mod;
    }

    return ret;
}

long long reverse(long long x, long long mod)
{
    return pow(x, mod - 2, mod);
}

long long a[MAXN];

int main()
{
    ios::sync_with_stdio(false);

    int n;
    while (cin >> n)
    {
        for (int i = 1; i<=n; i++)
            cin >> a[i];

        long long ans = 0;
        for (int i = 1; i<=n; i++)
        {
            long long tmp = 1;
            for (int j = 1; j<=n; j++)
                if (i!=j)
                {
                    long long m = a[j] * a[j] - a[i] * a[i];
                    m %= MOD;
                    if (m<0)
                        m += MOD;
                    tmp = tmp * m % MOD;
                }

            tmp = tmp * 2 * a[i] % MOD;

            ans = (ans + reverse(tmp, MOD)) % MOD;
        }

        cout << ans << endl;
    }
}
```
