---
title: "Be Positive"
date: 2019-02-25 14:52:20
tags: 
---

# Be Positive 

## CF Contest 542 A

<!--more-->

题目来源：[_codeforces_](https://codeforces.com/problemset/problem/1130/A)

## 分析

这题一看其实就是一个水题。我们只需要分别判断正负数的个数即可。正数数量$>= \frac{n}{2}$就输出`1`，负数数量$>= \frac{n}{2}$就输出`-1`，否则输出`0`。

## 代码

```C++
#include <iostream>

using namespace std;

int cnt[2];

int main()
{
    int n;
    cin >> n;
    
    cnt[0] = cnt[1] = 0;
    for (int i = 1; i<=n; i++)
    {
        int x;
        cin >> x;
        if (x>0)
            cnt[0] ++;
        else if (x<0)
            cnt[1] ++;
    }

    if (cnt[0] >= (n + 1) / 2)
        cout << 1 << endl;
    else if (cnt[1] >= (n + 1) / 2)
        cout << -1 << endl;
    else cout << 0 << endl;
}
```