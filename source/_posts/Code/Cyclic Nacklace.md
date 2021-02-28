---
title: "Cyclic Nacklace"
date: 2018-08-28 13:46:20
tags: 
---

# Cyclic Nacklace

## hdu 3746

<!--more-->

题目来源: [_hdu_](acm.hdu.edu.cn/showproblem.php?pid=3746)

## 分析

题目给出了一个字符串`s`，要求求出我们最少需补充多少个字符，使得这个字符串内存在循环节(循环节可以总共只有`1`个,即`s`自己)。

首先，我们可以证明，此时的循环节一定是`s`的最小循环节。对于最小循环节`t1`，我们假设最后需要补`x`个。假设我们存在另一个循环节`t2`，使得最后需要补的字符个数为`y`，且`y<x`。因为此时这两个循环节肯定不是互相包含的，那么他们肯定存在一个不等于`t1`和`t2`的公共循环节，此时这个循环节就会是最小循环节，与前提条件不符，说明不存在这样的循环节`t2`。

那么，现在的问题便转化为了求`s`的最小循环节。这里需要一个较为巧妙地方法。我们知道，再求KMP的`fail[]`数组时，我们能够求出其自匹配的最长长度，而此时除了最后几个没有凑够一个循环节的点和第一个循环节内的点，而此时`i-fail[i]`的最大值变为循环节的长度。此外，我们可以发现，我们只需要j计算每个循环节最后一个点的`i-fail[i]`即可。所以最后只需不停执行如下语句即可:
```C++
for (int i = s.length(); i>0; i = f[i])
	ans = max(ans, i-f[i]);
```

## 代码

```C++
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s;
int f[100100];

void getFail()
{
    f[0] = 0;

    for (int i = 1; i<s.length(); i++)
    {
        int j = f[i];
        while (j && s[i]!=s[j])
            j = f[j];
        f[i+1] = s[i]==s[j]? j+1 : 0;
    }
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        cin >> s;
        getFail();

        int ans = 1;
        for (int i = s.length(); i>0;)
        {
            int j = f[i];
            ans = max(ans, i-j);
            i = j;
        }

        if (ans==s.length())
            cout << ans << endl;
        else
            cout << (ans - s.length()%ans)%ans << endl;
    }
}

```