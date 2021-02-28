---
title:Equivalent Sets
date:2018-08-28 13:48:11
tags:
---

# Equivalent Sets

## hdu 3836

<!--more-->

题目来源: [_hdu_](acm.hdu.edu.cn/showproblem.php?pid=3836
)

## 分析

题目给出了几个集合，并且给出了几组它们之间的关系，要求至少需要在测定几次它们之间的关系(小于关系)，能够验证出它们是否相等。同时，题目给出可以通过$A < B\ \&\ B < A $的方式来验证它们是否相等。

题目要求测定次数最小，那么什么情况下测量的次数会最小呢？或者说有哪些测量会是不必要的呢？我们假设两个集合之间的小于关系是一条有向边，那么当几个集合成环时，它们一定相等。而此时的边数也一定已经是最小了。

但是整个图最后一定要组成一个环吗?很明显，几个相交的环也能推出其中所有点的相等关系，因为等于关系是可以传递的。那么到底组成几个环最好呢？这该怎么算呢？

我们不妨想一下环的性质是什么呢？所有点的入度和出度都不为$0$。那么我们只要去掉为$0$的点便能成环。理论上，我们最好将入度为$0$的点和出度为$0$的点连在一起，但是有时候它们数目不一样，所以我们需要再将多出来的连接到任意一个点上即可。

不过这样成环后图一定联通吗？假设我们能分别用两条边生成两个不连通的环，那么可以证明我们用这两条边也能生成一整个环，所以一定存在最后的图联通的方案。但是若初始的图中就有一个环，那么就比较麻烦了。此时我们需要用Tarjan来求强连通分量，然后缩点，把其看成一个点即可。

因此，最后的答案是$ max(\sum_1^n in_i, \sum_1^n out_i) $，$in_i$和$out_i$记录的是每个强连通分量的入度和出度。

## 代码

```C++
#include <iostream>
#include <stack>
#include <algorithm>
#include <cstring>

#define MAXN 20010

using namespace std;

struct Edge;

struct Node
{
    Edge *edge;
    int dfn, low, color;
    bool flag;

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

    ~Edge()
    {
        delete next;
    }

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

int in[MAXN],out[MAXN];

int main()
{
    int n,m;
    while (cin >> n >> m)
    {
        memset(out,0,sizeof(out));
        memset(in,0,sizeof(in));
        for (int i = 1; i<=n; i++)
        {
            delete node[i].edge;
            node[i] = Node();
        }
        cnt = 0;

        for (int i = 1; i<=m; i++)
        {
            int x,y;
            cin >> x >> y;
            node[x].edge = new Edge(&node[x],&node[y]);
        }

        for (int i = 1; i<=n; i++)
            if (node[i].dfn==0)
                Tarjan(&node[i]);

        for (int i = 1; i<=n; i++)
        {
            for (Edge *e = node[i].edge; e; e = e->next)
                if (node[i].color!=e->to->color)
                {
                    out[node[i].color] ++;
                    in[e->to->color] ++;
                }
        }

        int ans[2];
        ans[0] = ans[1] = 0;
        
        for (int i = 1; i<=cnt; i++)
        {
            if (!in[i])
                ans[0]++;
            if (!out[i])
                ans[1]++;
        }
        if (cnt==1)
            cout << 0 << endl;
        else cout << max(ans[0],ans[1]) << endl;
    }
}
```