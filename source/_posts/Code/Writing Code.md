---
title:Writing Code
date:2018-08-28 13:46:43
tags:
---

# Writing Code

## CF 544 C

> CF的题目编号与比赛编号挺乱的，以后为了统一，博客上一律使用题目编号。之前的都是比赛编号，我有时间(bu)可能会改一下。

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/problemset/problem/544/C)

## 分析

很明显，这是一个DP。我们可以发现影响方案数的状态有如下三个:
1. 取到哪几个人;
2. 完成的代码行数;
3. bug数量。

所以，我们可以使用一个三位数组来存储方案数。`f[][][]`，第一维存储取到了第几个人，第二维为代码行数，第三位为bug总数，那么状态转移方程如下:

$$ f[i][j][k] += f[i-1][j-1][k-a[i]] $$
$$ f[i][j][k] += f[i][j-1][k-a[i]] $$

而很明显，我们可以将这个三维数组优化为二维，去掉第一维，最后的方程如下:

$$ f[j][k] += f[j-1][k-a[i]] $$

## 代码

```C++
#include <iostream>

using namespace std;

long long f[510][510];
int a[510];

int main()
{
    int n,m,b;
    long long p;
    cin >> n >> m >> b >> p;

    for (int i = 1; i<=n; i++)
        cin >> a[i];

    f[0][0] = 1;
    for (int i = 1; i<=n; i++)
        for (int j = 1; j<=m; j++)
        {
            for (int k = b; k>=0; k--)
                if (k-a[i]>=0)
                {
                    f[j][k] += f[j-1][k-a[i]];
                    f[j][k] %= p;
                }
        }

    long long ans = 0;
    for (int i = 0; i<=b; i++)
    {
        ans += f[m][i];
        ans %= p;
    }
    cout << ans;
}
```