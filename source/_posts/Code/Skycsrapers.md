---
title:Skycsrapers
date:2019-03-20 21:09:21
tags:
---

# Skycsrapers

# CF 1137 A

> 这是我的第一场Div.1，结果打完之后又掉回Div.2了，结束了我短暂的Div.1生涯。。。

<!--more-->

题目来源：[_Codeforces_](https://codeforces.com/contest/1137/problem/A)

## 分析

题目给出了一个$n \times m$的地图`mp[][]`，假设其由`n`条横向道路和`m`条纵向道路组成，并且在每一个路口都有一个摩天大楼，高度为`mp[i][j]`。然后，我们希望在不更改同一行或同一列的大楼之间的高度关系的情况下，令高度最高的大楼的高度尽可能的小。

这其实就是一个Hash，我们对于每一行或者每一列都Hash映射到尽可能小的数即可。不过我们还要考虑一个点同时对行和列的影响。譬如一个点在行中算出其为`10`，但是在列中是最小的。所以我们需要令列中的所有数都按照正常Hash的情况再加`9`。所以实际上，我们可以记录，每个点在行中或者列中，小于等于它的数的Hash值的数目和大于等于的数目，即`smaller[i][j][]`和`bigger[i][j][]`。第三维通过`0,1`来记录行列，然后答案在`smaller[i][j][]`和`bigger[i][j][]`中取组合的最大值即可。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <string>

#define MAXN 1010

using namespace std;

struct A
{
    int i, j;
    int x;

    A(){}

    A(int x, int i, int j):x(x), i(i), j(j) {}

    const bool operator < (const A &tmp) const
    {
        return this->x < tmp.x;
    }

    const bool operator != (const A &tmp) const
    {
        return this->x != tmp.x;
    }

}a[MAXN];

int mp[MAXN][MAXN];
int smaller[MAXN][MAXN][2], bigger[MAXN][MAXN][2];

int main()
{
    ios::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;

    for (int i = 1; i<=n; i++)
        for (int j = 1; j<=m; j++)
            cin >> mp[i][j];

    for (int i = 1; i<=n; i++)
    {
        for (int j = 1; j<=m; j++)
            a[j] = A(mp[i][j], i, j);

        sort(a+1, a+1+m);

        int t = 1;
        smaller[ a[1].i ][ a[1].j ][0] = 1;
        for (int j = 2; j<=m; j++)
        {
            if (a[j]!=a[j-1])
                t++;

            smaller[ a[j].i ][ a[j].j ][0] = t;
        }

        for (int j = 1; j<=m; j++)
            bigger[ a[j].i ][ a[j].j ][0] = t - smaller[ a[j].i ][ a[j].j ][0];
    }

    for (int j = 1; j<=m; j++)
    {
        for (int i = 1; i<=n; i++)
            a[i] = A(mp[i][j], i, j);

        sort(a+1, a+1+n);

        int t = 1;
        smaller[ a[1].i ][ a[1].j ][1] = 1;
        for (int i = 2; i<=n; i++)
        {
            if (a[i]!=a[i-1])
                t++;

            smaller[ a[i].i ][ a[i].j ][1] = t;
        }

        for (int i = 1; i<=n; i++)
            bigger[ a[i].i ][ a[i].j ][1] = t - smaller[ a[i].i ][ a[i].j ][1];
    }

    for (int i = 1; i<=n; i++)
    {
        for (int j = 1; j<=m; j++)
        {
            int ans = max(smaller[i][j][0] + bigger[i][j][1], smaller[i][j][1] + bigger[i][j][0]);  
            ans = max(ans, smaller[i][j][0] + bigger[i][j][0]);
            ans = max(ans, smaller[i][j][1] + bigger[i][j][1]);

            cout << ans << " ";
        }
        cout << endl;
    }
}
```