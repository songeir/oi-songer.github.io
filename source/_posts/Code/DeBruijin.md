---
title:DeBruijin
date:2018-08-28 13:46:54
tags:
---

# DeBruijin

## hdu 2894

<!--more-->

题目来源: [_hdu_](http://acm.hdu.edu.cn/showproblem.php?pid=2894)

## 分析

题目要求，给出一个长度为$k ( 2 \leq k \leq 11) $，我们需要生成一个`0`,`1`组成的最长环形字符串，使得其中任意`k`个连续的子串互不相等。题目要求输出该字符串长度与字符串本身。

我们在求字符串之前，可以先看一下它的长度有什么规律。我们可以证出长度$ m = 2^k $。因为长度为`k`的`01`字符串一共存在$2^k$中情况，而$m=2^k$时它也有$2^k$个子串，所以我们只需要让每一个子串各不相同就好了。

然后我们只需要较为暴力的求出该串即可。我这里使用的时深搜的方法。因为每个字串的下一个相邻的子串只有两种情况，我们搜索一下，看哪一种最后能够将所以子串生成出来即可。

## 代码

```C++
#include <iostream>
#include <cmath>
#include <iomanip>
#include <cstring>

using namespace std;

int dist[100100];
int n,k;

bool dfs(int x)
{
    if (dist[x]==n)
        return true;
    
    for (int i = 0; i<2; i++)
        if (dist[(x*2+i)%n]==0)
        {
            dist[(x*2+i)%n] = dist[x] + 1;
            if (dfs((x*2+i)%n))
                return true;
            dist[(x*2+i)%n] = 0;
        }

    return false;
}

int trans(int x)
{
    int t = n/2;
    return x/t;
}

int main()
{
    while (cin >> k)
    {
        n = pow(2,k);
        cout << pow(2,k) << " ";

        dist[0] = 1;
        memset(dist,0,sizeof(dist));
        
        dfs(0);

        int t = 0;
        cout << trans(t);
        for (int i = 1; i<n; i++)
            for (int j = 0; j<2; j++)
                if (dist[(t*2+j)%n]==dist[t]+1)
                {
                    t = t*2 + j;
                    t %= n;
                    cout << trans(t);
                }
        cout << endl;
    }
}
```