---
title: "Two Cakes [思维题]"
date: 2019-03-01 09:18:53
tags: 
---

# Two Cakes [思维题]

## CF Contest 542 B

<!--more-->

题目来源：[_codeforces_](https://codeforces.com/contest/1130/problem/B)

## 分析

这道题其实和Wannafly Camp中的[_夺宝奇兵_](http://songer.xyz/index.php/archives/343/)有异曲同工之妙。我们有两个人，他们分别需要从`0`走到`n`，那么我们其实可以发现对于每次从第$i$个走到$i+1$个，谁在哪个位置完全没有影响，我们只需要考虑怎么走最近即可。

## 代码

```C++
#include <iostream>
#include <algorithm>

#define MAXN 100100

using namespace std;

int a[MAXN][2];

int main()
{
    int n;
    cin >> n;

    for (int i = 1; i<=2*n; i++)
    {
        int x;
        cin >> x;
        if (a[x][0]==0)
            a[x][0] = i;
        else a[x][1] = i;
    }

    long long ans = 0;
    ans += a[1][0] + a[1][1] - 2;
    for (int i = 1; i<n; i++)
    {
        int min1 = abs(a[i][0] - a[i+1][0]) + abs(a[i][1] - a[i+1][1]);
        int min2 = abs(a[i][0] - a[i+1][1]) + abs(a[i][1] - a[i+1][0]);

        ans += min(min1, min2);
    }

    cout << ans << endl;
}
```