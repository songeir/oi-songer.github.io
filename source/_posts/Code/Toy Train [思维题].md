---
title: "Toy Train [思维题]"
date: 2019-02-27 09:16:33
tags: 
---

# Toy Train [思维题]

## CF Contest 542 D

<!--more-->

## 分析

题目要求对于$n$个不同的起点，分别给出将所有糖果送完花费的最小时间。

我们可以先假设起点已经固定。由于我们每次可以携带多个糖果，并且可以卸下多个糖果，所以我们可以发现对于不同的$j$，将最初位于节点$j$的糖果送完所花费的时间相互之间互不干扰。

那么对于第$j$个节点，将这个节点的所有糖果送完所需要花费的时间是多少呢？我们假设起点为$i$。那么，我们第一次到达$j$所花费的时间就是$(j - i + n) \mod n$。然后我们假设节点$j$共有$k$个糖果，那么我们可以发现我们至少需要经过$j$节点$k$次才能拿到所有糖果。所以拿到所有糖果至少需要$(j - i + n) \mod n + (k - 1) *n$次移动。

此外，我们可以发现在下一次到达$j$点前，我们一定可以将上次从$j$点拿走的糖果送出去，所以，我们最后只剩下一个糖果没有送到位置。由于我们想令答案最小，所以只需要令最后送的位置最近即可。

那么，对于起点$i$,位置$j$的$k$个糖果$a_1 - a_k$（$k$必须不为$0$），所需花费的时间为:

$$ t[j] = (j - i + n) \mod n + (k - 1) * n + min( (a_i - j + n) \mod n) $$

那么，对于起点$i$，所花费的最小时间即为$min(t[j])$。 

## 代码

```C++
#include <iostream>
#include <algorithm>

#define MAXN 5010
#define INF 0x3f3f3f3f

using namespace std;

int cnt[MAXN], nearest[MAXN];

int main()
{
    int n, m;
    cin >> n >> m;

    for (int i = 1; i<=n; i++)
        nearest[i] = INF;

    for (int i =1; i<=m; i++)
    {
        int x, y;
        cin >> x >> y;
        cnt[x] ++;
        nearest[x] = min(nearest[x], (y + n - x) % n );
    }

    for (int i = 1; i<=n; i++)
    {
        int ans = 0;
        for (int j = 1; j<=n; j++)
            if (cnt[j])
                ans = max(ans, (cnt[j] - 1) * n + nearest[j] + (j - i + n) % n );

        cout << ans << " ";
    }
}
```