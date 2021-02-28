---
title: "Smallest Minimum Cut"
date: 2018-08-28 14:55:32
tags: 
---

# Smallest Minimum Cut

## hdu 6214

<!--more-->

题目来源: [_hdu_](acm.hdu.edu.cn/showproblem.php?pid=6214)

## 分析

题目要求求出边数最小的最小割。很明显，我们在正常求最小割时根本无法得知最小割的边数。所以我们应该想办法把它记录下来。

我们可以把这个信息加入到所有边的`capacity`中。因为边共有`m`个，所以我们的最小割最大为`m`。那么我们可以令$capacity = capacity \times (m+1) + 1$。此时我们算出的最小割，便为$原来的最小割\times (m+1) + 边数$。所以，我们直接$mod (m+1)$就好了。

## 代码

```C++
#include <iostream>
#include <queue>
#include <cstdio>

#define MAXN 1010
#define INF 0x3f3f3f3f

using namespace std;

struct Node;
struct Edge;
int n,m;

struct Node
{
    Edge *firstEdge, *currentEdge;
    int level;

    Node()
    {
        firstEdge = NULL;
    }

}node[MAXN];

struct Edge
{
    Node *from, *to;
    int capacity, flow;
    Edge *next, *reverseEdge;

    Edge(Node *from, Node *to, int capacity):from(from),to(to),capacity(capacity),flow(0),next(from->firstEdge)   {}

    ~Edge()
    {
        delete next;
    }
};

struct Dinic
{
    bool makeLevelGraph(Node *s, Node *t, int n)
    {
        for (int i = 1; i<=n; i++)
        {
            node[i].level = 0;
            node[i].currentEdge = node[i].firstEdge;
        }
        queue<Node *> q;
        q.push(s);
        s->level = 1;

        while (!q.empty())
        {
            Node *v = q.front();
            q.pop();

            for (Edge *e = v->firstEdge; e; e = e->next)
                if (e->flow<e->capacity && e->to->level==0)
                {
                    e->to->level = v->level + 1;
                    if (e->to==t)
                        return true;
                    else q.push(e->to);
                }
        }

        return false;
    }

    int findPath(Node *s, Node *t, int limit = INF)
    {
        if (s==t)
            return limit;

        for (Edge *&e = s->currentEdge; e; e = e->next)
            if (e->to->level==s->level+1 && e->flow < e->capacity)
            {
                int flow = findPath(e->to, t, min(limit, e->capacity - e->flow));
                if (flow>0)
                {
                    e->flow += flow;
                    e->reverseEdge->flow -= flow;
                    return flow;
                }
            }

        return 0;
    }

    int operator()(int s, int t, int n)
    {
        int ans = 0;
        while (makeLevelGraph(&node[s], &node[t], n))
        {
            int flow;
            while ((flow = findPath(&node[s], &node[t]))>0 )
                ans += flow;
        }
        return ans;
    }

}dinic;

int main()
{
    ios::sync_with_stdio(false);

    int T;
    scanf("%d",&T);
    while (T--)
    {
        int s,t;
        scanf("%d%d%d%d",&n,&m,&s,&t);

        for (int i = 1; i<=n; i++)
        {
            delete node[i].firstEdge;
            node[i] = Node();
        }

        for (int i = 1; i<=m; i++)
        {
            int x,y,z;
            scanf("%d%d%d",&x,&y,&z);
            node[x].firstEdge = new Edge(&node[x], &node[y], z*(1+m)+1);
            node[y].firstEdge = new Edge(&node[y], &node[x], 0);

            node[x].firstEdge->reverseEdge = node[y].firstEdge;
            node[y].firstEdge->reverseEdge = node[x].firstEdge;
        }

        int ans = dinic(s, t, n);

        cout << ans%(1+m) << endl;
    }
}
```