---
title: "Checkposts"
date: 2018-08-28 13:48:44
tags: 
---

# Checkposts

## CF 427 C

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/problemset/problem/427/C)

## 分析

题目要求求出每个强连通分量中价值最小的点，并计数。只需要跑一边Tarjan，然后更新所有强连通分量中的最小值即可。

## 代码

```C++
#include <iostream>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cstdio>

#define MAXN 100100
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;

struct Edge;

struct Node
{
    Edge *edge;
    int dfn, low, color;
    bool flag;
    int val;

    Node()
    {
        flag = false;
        dfn = low = color = 0;
        edge = NULL;
    }
}node[MAXN];

struct Edge
{
    Node *from, *to;
    Edge *next;

    Edge(Node *from, Node *to):from(from),to(to),next(from->edge)   {}
};

int cnt = 0;

stack<Node *> s;
void Tarjan(Node *x)
{
    static int num = 0;
    x->low = x->dfn = ++num;
    x->flag = true;
    s.push(x);

    for (Edge *e = x->edge; e; e = e->next)
    {
        if (e->to->dfn==0)
        {
            Tarjan(e->to);
            x->low = min(x->low, e->to->low);
        }else if (e->to->flag)
            x->low = min(x->low, e->to->dfn);
    }

    if (x->dfn==x->low)
    {
        x->flag = false;
        x->color = ++cnt;

        while ( !s.empty() && s.top()!=x)
        {
            Node *v = s.top();
            v->color = cnt;
            v->flag= false;
            s.pop();
        }
        if (!s.empty())
            s.pop();
    }
}

int minCost[MAXN];
long long way[MAXN];

int main()
{
    int n,m;
    scanf("%d",&n);

    for (int i = 1; i<=n; i++)
        scanf("%d",&node[i].val);

    scanf("%d",&m);
    for (int i = 1; i<=m; i++)
    {
        int x,y;
        scanf("%d%d",&x,&y);

        node[x].edge = new Edge(&node[x],&node[y]);
    }

    for (int i = 1; i<=n; i++)
        if (node[i].dfn==0)
            Tarjan(&node[i]);

    memset(minCost,INF,sizeof(minCost));

    for (int i = 1; i<=n; i++)
    {
        if (node[i].val < minCost[ node[i].color ])
        {
            minCost[ node[i].color ] = node[i].val;
            way[ node[i].color ] = 1;
        }else if (node[i].val == minCost[ node[i].color ])
        {
            way[ node[i].color ] ++ ;
        }
    }

    long long ans[2];
    ans[0] = 0;
    ans[1] = 1;
    for (int i = 1; i<=cnt; i++)
    {
        ans[0] += minCost[i];
        ans[1] *= way[i];
        ans[1] %= MOD;
    }

    cout << ans[0] << " " << ans[1] << endl;
}
```

