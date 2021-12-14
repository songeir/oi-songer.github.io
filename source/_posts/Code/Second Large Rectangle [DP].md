---
title: "Second Large Rectangle [DP]"
date: 2019-08-26 21:31:05
tags: [test]
categories: [code]
---

# Second Large Rectangle [DP]

## 2019牛客 第二场 H

<!--more-->

题目来源：[_Nowcoder_](https://ac.nowcoder.com/acm/contest/882/H)

## 分析

题目要求“次大全1子矩阵”。其实我们将最大全1子矩阵的代码略加改动便可得到答案。

由于我们之前算的是最大子矩阵，所以在代码里，我们每次根据$i, j$和$h_{i,j}$算出$l_{i,j}$,$r_{i,j}$时，都只用到了$h_{i,j} \times (r_{i,j} - l_{i,j} + 1)$这么一种情况去更新答案。也就是说，我们只考虑了最大的情况。那么，这次，我们只需要将$(h_{i,j} - 1) \times (r_{i,j} - l_{i,j} + 1)$和$h_{i,j} \times (r_{i,j} - l_{i,j})$考虑进去就行了。此时我们只需维护最大值和次大值两个值即可。

但是，还有一种特殊情况。当同一行几个相邻点$h_{i,j}$相同时，同一答案可能被计算多次。在计算最大子矩阵时不需要在乎此问题，但在这里就需要考虑了。我们可以发现，当几个点在同一行时，它们的$l_{i,j}$和$r_{i,j}$在一起能共同决定整个矩形。也就是说，我们只要将$(l_{i,j},r_{i,j})$扔到`set`里即可。当然，`set`只需判断在同一行的情况。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <set>

#define MAXN 1010

using namespace std;

int a[MAXN][MAXN];
int h[MAXN][MAXN];
int l[MAXN], r[MAXN];

set<pair<int, int>> s;

int main()
{
    int n, m;
    while (~scanf("%d%d", &n, &m))
    {
        for (int i = 1; i<=n; i++)
        {
            getchar();
            for (int j = 1; j<=m; j++)
                a[i][j] = getchar() - '0';
        }

        for (int i = 1; i<=n; i++)
            for (int j = 1; j<=m; j++)
                if (a[i][j]==1)
                    h[i][j] = h[i-1][j] + 1;
                else
                    h[i][j] = 0;

        int ans = 0, maxn = 0;
        for (int i = 1; i<=n; i++)
        {
            s.clear();

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

                // cout << l[j] << " " << r[j] << " " << h[i][j] << endl;

                if (s.find(pair<int, int>(l[j], r[j])) == s.end())
                {
                    s.insert(pair<int, int>(l[j], r[j]));

                    int m = (r[j] - l[j] + 1) * h[i][j];

                    if (m > maxn)
                    {
                        ans = maxn;
                        maxn = m;

                        if (m - h[i][j] > ans)
                            ans = m - h[i][j];
                        if (m - (r[j] - l[j] + 1) > ans)
                            ans = m - (r[j] - l[j] + 1);

                    }else if (m > ans)
                        ans = m;
                }

            }
        }

        printf("%d\n", ans);
        // cout << ans << endl;
    }
}
```
