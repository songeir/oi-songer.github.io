---
title: "Antenna Placement"
date: 2018-08-28 13:47:21
tags: 
---

# Antenna Placement

## POJ 3020

<!--more-->

题目来源: [_POJ_](http://poj.org/problem?id=3020)

## 分析

题目给出一个$ n \times m $的由`*`和`o`组成的图，要求用一些宽度为`1`，长度为`2`的板子将所有的`*`覆盖。要求求出最少需要多少板子。

我们假设若两个`*`相邻，那么它们之间便有一条边。那么我们可以看到，对于任意一个点，与其相邻的任意两个点之间一定不存在边。所以由此构造出来的图满足二分图的性质。而这个问题明显的转化为了一个二分图的最小点覆盖问题。所以我们直接套用匈牙利算法即可。

## 代码

```C++
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char mp[50][20];
bool flag[50][20];
int belong[50][20][2];
int n,m;

bool inmp(int x,int y)
{
    return x>=0 && x<n && y>=0 && y<m;
}

const int xp[] = {0,0,-1,1};
const int yp[] = {1,-1,0,0};
bool find(int x, int y)
{
    for (int i = 0; i<4; i++)
        if (inmp(x+xp[i],y+yp[i]) && mp[x+xp[i]][y+yp[i]]=='*' && !flag[x+xp[i]][y+yp[i]])
        {
            flag[x+xp[i]][y+yp[i]] = true;
            if (belong[ x+xp[i] ][ y+yp[i] ][0]==-1 || find( belong[ x+xp[i] ][ y+yp[i] ][0], belong[ x+xp[i] ][ y+yp[i] ][1]) )
            {
                belong[ x+xp[i] ][ y+yp[i] ][0] = x;
                belong[ x+xp[i] ][ y+yp[i] ][1] = y;
                return true;
            }
        }
    return false;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        memset(belong,-1,sizeof(belong));

        cin >> n >> m;

        int num = 0;
        for (int i = 0; i<n; i++)
            for (int j = 0; j<m; j++)
            {
                cin >> mp[i][j];
                if (mp[i][j]=='*')
                    num++;
            }

        int cnt = 0;
        for (int i = 0; i<n; i++)
            for (int j = 0; j<m; j++)
                if (mp[i][j]=='*')
                {
                    memset(flag,false,sizeof(flag));
                    if (find(i,j))
                        cnt ++;
                }

        cout << num - cnt/2 << endl;
    }
}
```