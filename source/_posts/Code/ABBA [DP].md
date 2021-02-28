---
title:ABBA [DP]
date:2019-08-24 12:40:45
tags:
---

# ABBA [DP]

## 2019牛客多校 第一场 E

<!--more-->

题目来源：[_Nowcoder_](https://ac.nowcoder.com/acm/contest/881/E)

## 分析

我们可以把这个题目看作一个已经拥有$n$个`AB`和$m$个`BA`，把它放入一个数组的过程。那么，题目即为要求有多少种放法。

这个题目的主要限制在于`AB`中的`A`一定先于`B`放入，`BA`同理。那么，我们可以发现，已放置的`A`和`B`的放置顺序对答案没有影响。即，只有“是否已放置”有影响，“放置在哪里”没有影响。那么，很明显，这道题便是一个DP了。我们使用`dp[i][j]`记录答案，其中`i`是放置了多少个`A`，`j`是放置对了多少个`B`。那么，很明显，我们需要满足以下两个条件：

1. $i \leq n + j$;
2. $j \leq m + i$.

在以上两个条件下进行状态转移即可。

## 代码

```C++
#include <iostream>
#include <algorithm>

#define MAXN 1010
#define MOD 1000000007

using namespace std;

long long dp[2 * MAXN][2 * MAXN];

int main()
{
    int n, m;
    
    while (cin >> n >> m)
    {
        for (int i = 0; i<=n+m; i++)
            for (int j = 0; j<=n+m; j++)
                dp[i][j] = 0;

        dp[0][0] = 1;
        for (int i = 0; i<=n + m; i++)
            for (int j = 0; j<=m + n; j++)
            {
                if (i < n + j)
                    dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD;
                if (j < m + i)
                    dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % MOD;

                // cout << i << " " << j << " " << dp[i][j] << endl;
            }   

        cout << dp[n+m][n+m] << endl;
    }
}
```