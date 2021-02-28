---
title:热浪 [Dijkstra]
date:2018-08-24 14:26:29
tags:
---

# 热浪 [Dijkstra]

## Code[VS] 1557

> 整理板子时发现这个博客里竟然没有Dijkstra的板子。

<!--more-->

题目来源: [_Code[VS]_](http://codevs.cn/problem/1557/)

## 分析

简单的带有heap的Dijkstra。

## 代码

```C++
#include <iostream>
#include <queue>

#define INF 0x3f3f3f3f
#define MAXN 3000

using namespace std;

struct Node
{
    struct Edge *edge;
    int dist;
    int id;

    Node()
    {
        edge = NULL;
        dist = INF;
    }

    const bool operator <(const Node &tmp) const
    {
        return this->dist < tmp.dist;
    }

}node[MAXN];

struct Edge
{
    Node *from, *to;
    Edge *next;
    
    int val;

    Edge(Node *from, Node *to, int val):
        from(from), to(to), next(from->edge), val(val)  {}
};

int dist[MAXN];

priority_queue<Node> q;
void Dijkstra(Node st)
{
    dist[st.id] = 0;
    st.dist = 0;

    q.push(st);
    while (!q.empty())
    {
        Node tmp = q.top();
        q.pop();

        if (dist[tmp.id]!=tmp.dist)
            continue;
        
        for (Edge *e = tmp.edge; e; e = e->next)
        {
            if ( dist[e->to->id] > tmp.dist + e->val)
            {
                Node to = *e->to;
                dist[to.id] = tmp.dist + e->val;
                to.dist = dist[to.id];

                q.push( to );
            }
        }
    }
}

int main()
{
    int t, c, ts, te;
    cin >> t >> c >> ts >> te;

    for (int i = 1; i<=t; i++)
    {
        dist[i] = INF;
        node[i].id = i;
    }
    for (int i = 0; i<c; i++)
    {
        int x, y, z;
        cin >> x >> y >> z;

        node[x].edge = new Edge(&node[x], &node[y], z);
        node[y].edge = new Edge(&node[y], &node[x], z);
    }

    Dijkstra(node[ts]);

    cout << dist[ node[te].id ];
}
```