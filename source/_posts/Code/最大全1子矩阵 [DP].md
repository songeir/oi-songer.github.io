---
title: "最大全1子矩阵 [DP]"
date: 2019-08-26 15:26:26
tags: 
---

# 最大全1子矩阵 [DP]

## POJ 3494

<!--more-->

题目来源：[_POJ_](http://poj.org/problem?id=3494)

## 分析

这也算是一个十分经典的DP题了。给定一个01矩阵，要求求出最大的全1子矩阵。

首先，我们可以通过$O(n^2)$的预处理算出$h[i][j]$，代表的是$i,j$坐标的点
向上的连续`1`的数目。

然后，我们采用“悬线法”来计算答案。假如$l_i$是最靠左的令$h[x] \geq h[i], (l_i \leq x \leq i)$,$r_i$同理。那么$(r_i - l_i + 1) \times 1$就是高度为$h_i$且$i,j$在底边上的最大矩形。

那么，问题就在于如何求$l_i$和$r_i$了。如果我们暴力地去求，那么整个算法地时间复杂度就是$O(n^3)$，明显太慢。在这里，我们就要用DP的方法来实现了。

我们令所有的$j<i$,$l_j$都已经算出，那么，当$h_j < h_i$时，那么，我们可以保证$h_{l_j} < h_i$。然后，我们可以继续比较$h_{h_j - 1}$和$h_i$。这样，我们可以快速地算出$l_i$，$r_i$。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <cstdio>

#define MAXN 2010

using namespace std;

int a[MAXN][MAXN];
int h[MAXN][MAXN];
int l[MAXN], r[MAXN];

int getint()
{
    char c = getchar();

    while (c<'0' || c>'9')
        c = getchar();

    int ret = 0;
    while (c>='0' && c<='9')
        ret = ret * 10 + c - '0', c = getchar();

    return ret;
}

int main()
{
    // ios::sync_with_stdio(false);

    int n, m;
    while (~scanf("%d%d", &n, &m))
    {
        for (int i = 1; i<=n; i++)
            for (int j = 1; j<=m; j++)
                a[i][j] = getint();
                // scanf("%d",&a[i][j]);
                // cin >> a[i][j];

        for (int i = 1; i<=n; i++)
            for (int j = 1; j<=m; j++)
                if (a[i][j]==1)
                    h[i][j] = h[i-1][j] + 1;
                else
                    h[i][j] = 0;

        int ans = 0;
        for (int i = 1; i<=n; i++)
        {
            for (int j = 1; j<=m; j++)
            {
                l[j] = j;

                while ( l[j]>1 && h[i][ l[j] - 1 ] >= h[i][j])
                    l[j] = l[ l[j] - 1];

            }
            for (int j = m; j>=1; j--)
            {
                r[j] = j;

                while ( r[j]<m && h[i][ r[j] + 1 ] >= h[i][j])
                    r[j] = r[ r[j] + 1];

                ans = max(ans, (r[j] - l[j] + 1) * h[i][j] );
            }
        }

        printf("%d\n", ans);
        // cout << ans << endl;
    }
}
```