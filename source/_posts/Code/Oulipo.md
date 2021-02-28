---
title:Oulipo
date:2018-08-28 13:46:32
tags:
---

# Oulipo

## POJ 3461

<!--more-->

题目来源: [_POJ_](http://poj.org/problem?id=3461)

## 分析

一道裸的KMP，没有什么好说的。

## 代码

```C++
#include <cstdio>
#include <cstring>

#define MAXN 1000100

char a[MAXN],b[MAXN];
int f[MAXN];
int n,m;
int cnt;

void getFail()
{
    f[0] = 0;
    //f[1] = 0;
    for (int i = 1; i<m; i++)
    {    
        int j = f[i-1];
        while (j && b[i]!=b[j])    j = f[j-1];
        f[i] = b[i]==b[j]?j+1:0;
    }

    return;
}

void find()
{
    int j = 0;
    for (int i = 0; i<n; i++)
    {
        while (a[i]!=b[j] && j) j = f[j-1];
        if (a[i]==b[j])    j++;
        if (j==m)
            cnt ++;
    }
}

int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        cnt = 0;
        
        scanf("%s",b);
        scanf("%s",a);

        n = strlen(a);

        m = strlen(b);

        getFail();

        find();

        printf("%d\n",cnt);
    }
}
```
