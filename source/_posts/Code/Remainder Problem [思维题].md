---
title: "Remainder Problem [思维题]"
date: 2019-08-25 13:45:38
tags: 
---

# Remainder Problem [思维题]

## CF Edu 71 F

<!--more-->

题目来源：[_Codeforces_](https://codeforces.com/contest/1207/problem/F)

## 分析

题目给了长度为$5 \times 10^5$的全$0$数组，然后给出了两种操作：

1. `1 x y`: 令$a_x$加$y$；
2. `2 x y`: 求下标$i$满足$i \equiv y (\mod x)$的$a_i$的和。

假如我们直接维护一个$a_i$数组，那么如果我们暴力进行操作$2$的话，时间复杂度显然是$O\left(\frac{x}{x} \right)$的。当$x^2>N$时，该操作是$O(n^{\frac{1}{2}})$的。但是，当$x$较小时呢？我们可以直接维护一个$ans[x][y]$数组，在每次进行操作$1$时，对所有影响的数组进行更新即可。因为$x^2 \leq N$，所以插入操作也是$O(n^{\frac{1}{2}})$的。所以，我们最后得到了一个$O(q \sqrt{n})$的算法。

而实际上，由于大部分$x$都是不等于$\sqrt(n)$的，所以实际的时间要比$O(q \sqrt{n})$要小，所以可以通过该题。

## 代码

```C++
#include <iostream>
#include <algorithm>

#define MAXN 500000
#define K 750

using namespace std;

int a[MAXN + 1];
long long ans[K+1][K];

int main()
{
    int q;
    cin >> q;

    for (int i = 1; i<=q; i++)
    {
        int op, x, y;
        cin >> op;
        cin >> x >> y;

        if (op==1)
        {
            a[x] += y;
            for (int j = 1; j<=K; j++)
                ans[j][x % j] += y;
        }else
        {
            if (x>K)
            {
                long long tmp = 0;
                for (int j = y; j<=MAXN; j+=x)
                    tmp += a[j];
                cout << tmp << endl;
            }else
            {
                cout << ans[x][y] << endl;
            }
            
        }
    }
}
```
