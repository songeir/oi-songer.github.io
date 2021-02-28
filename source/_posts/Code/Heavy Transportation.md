---
title: "Heavy Transportation"
date: 2018-08-28 13:45:51
tags: 
---

# Heavy Transportation

## POJ 1797

> 之前电脑的电源适配器坏了，送厂换新，花了几天。因此，这几天我一直在学(hua)习(shui)，博客一直没有更新。本来博客就拖了很久，这一下感觉根本补不上了。。。

<!--more-->

题目来源: [_POJ_](http://poj.org/problem?id=1797)

## 分析

题目给出了一个无向带权图，要求给出一条从`1`到`n`的最小的边权值最大的路。其实这就是一个最短路的简单变形，只需要更改一下判断条件即可，将原来的$dist_j > dist_i + val_{i,j} $换为$ ans_j < min( dist_i, val_{i,j} ) $即可。然后由于这个图较为稠密，所以要用Dijsktra.

## 代码

```C++
#include <cstdio>
#include <cstring>
#include <algorithm>

#define INF 0x3f3f3f3f

using namespace std;

int n,m;
int mp[1010][1010];
bool flag[1010];
int ans[1010];

int dijkstra()
{
    for (int i = 1;i<=n;i++)
    {
        ans[i]=mp[1][i];
        flag[i] = false;
    }
    ans[1]=0;

    for (int i = 1;i<=n;i++)
    {
        int minn = -1, v;
        for (int j = 1; j<=n; j++)
        {
            if (!flag[j] && ans[j] > minn)
            {
                minn = ans[j];
                v = j;
            }
        }
        flag[v] = true;
        for (int j = 1; j<=n; j++)
        {
            if (!flag[j] && ans[j] < min(ans[v],mp[v][j]))
                ans[j] = min(ans[v],mp[v][j]);
        }
    }
    return ans[n];
}

int main()
{
    int T;
    scanf("%d",&T);
   
    for (int cas = 1; cas<=T; cas++)
    {
        memset(mp,0,sizeof(mp));

        scanf("%d%d",&n,&m);

        for (int i = 1; i<=m; i++)
        {
            int x,y,z;
            scanf("%d%d%d",&x,&y,&z);
            mp[x][y] = mp[y][x] = z;
        }

        int an = dijkstra();

        printf("Scenario #%d:\n%d\n\n",cas,an);
    }
}
```
