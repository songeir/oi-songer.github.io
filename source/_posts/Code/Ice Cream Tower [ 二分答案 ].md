---
title: "Ice Cream Tower [ 二分答案 ]"
date: 2018-12-06 20:34:46
tags: 
---

# Ice Cream Tower [ 二分答案 ]

## CF Gym 101194 D

<!--more-->

## 分析

这道题第一眼看上去感觉贪心可做，然而会发现存在不可行的情况。对于一个高度为`k`的Tower，其最大值肯定越小越好，其最小值肯定也越大越好。但是中间值却不一定，其是存在后效性的。所以贪心是不可行的。

既然贪心不可行，而有没有什么其他的好方法，便只能用二分了。二分的难点在于`check()`操作是否可行，答案是否单调。首先答案明显是单调的，所以问题不大。而`check()`操作是否可以实现呢？假设我们当前需要check`m`个Tower，那么我们完全可以假设这`m`个Tower是以最小的`m`为顶。我们可以发现，这完全是可行的。然后，所以往后的操作也是贪心的，即若是可以加入便可以直接加。那么，我们可以得到一个$O(n)$的`check()`操作。此问题得解。

此外，还要注意一个二分时常见的问题--答案是“靠左的”还是“靠右的”。若答案是靠左的，`mid`应取`(l+r)/2`，且`x<=a[mid]`时`r=mid`；若答案时靠右的，`mid`应取`(l+r)/2+1`，且`x>=a[mid]`时`l=mid`。

## 代码

```C++
#include <iostream>
#include <algorithm>

#define MAXN 300100

using namespace std;

long long a[MAXN];
long long b[MAXN];

bool check(int m, int n, int k)
{
    for (int i = 1; i<=m; i++)
        b[i] = a[i];

    int j = m+1;
    if (j == m * k + 1)
        return true;

    for (int i = m+1; i<=n; i++)
    {
        if ( a[i] >= b[ (j - 1) % m + 1 ] * 2 )
        {
            b[ (j - 1) % m + 1 ] = a[i];
            j++;
            
            if (j == m * k + 1)
                return true;
        }
    }

    return false;
}

int main()
{
    int T;
    cin >> T;

    for (int cas = 1; cas<=T; cas++)
    {
        int n, k;
        cin >> n >> k;

        for (int i = 1; i<=n; i++)
            cin >> a[i];

        sort(a+1, a+1+n);

        int l = 0, r = n;
        while (l!=r)
        {
            int mid = (l + r) / 2 + 1;
            if (check(mid, n, k))
                l = mid;
            else r = mid - 1;
        }

        cout << "Case #" << cas << ": " << l << endl;
    }
}
```