---
title: "[学习笔记]Dinic算法"
tags: 
---

# [学习笔记]Dinic算法(最大费用流)

> PS: 更新于2019-9-16。在代码中添加了之前误删除的currentEdge变量，能够大幅度加快代码速度。

<!--more-->

## 算法介绍

其实不仅仅是Dinic算法，所有的最大费用流算法的思想都是类似的。其主要思想都是不停的寻找增广路，然后进行增广直至不可行为止。假设我们有一个如下的图，那么算法思路如下:(图中边上的"$x$/$y$"格式中，$x$指的是残量，$y$指的是以流过的流量)

1. 对于一个图，我们首先尝试寻找图中是否有增广路:
![图1](http://ovi2jbxue.bkt.clouddn.com/InblogDinic%E7%AE%97%E6%B3%95-1.png)
2. 增加增广路的流量，增加的值为该条路中最小的残量，生成新的残量网络；
![图2](http://ovi2jbxue.bkt.clouddn.com/InblogDinic%E7%AE%97%E6%B3%95-2.png)
3. 重复1~2操作；
4. 最终图形如下；
![图3](http://ovi2jbxue.bkt.clouddn.com/InblogDinic%E7%AE%97%E6%B3%95-3.png)

这里有一个比较形象的动图:

![图4](http://ovi2jbxue.bkt.clouddn.com/InblogDinic%E7%AE%97%E6%B3%95-4.gif)

## 实现细节

代码参考于: [_Menci_](https://oi.men.ci/dinic-notes/)

要实现Dinic算法，我们要分为几个部分: `Node`和`Edge`结构体，`makeLevelGraph()`和`findPath()`函数和主函数。

### Node

`Node`结构体内需包含三个变量: 指向第一条边的指针`firstEdge`，指向“当前”边的指针`currentEdge`(用于优化代码速度)和存放`level`的变量。

```C++
struct Node
{
    Edge *currentEdge, *firstEdge;
    int level;

    Node()
    {
        firstEdge = NULL;
    }

}node[MAXN];
```

### Edge

`Edge`中的成员变量则比较多，一对分别指向起点和终点的`Node *`类型的指针，分别记录初始值和流量的`capacity`和`flow`变量，还有分别指向下一条边和反向边的`Edge *`类型的`next`和`reverseEdge`指针。其中，比较巧妙地一点是反向边的建立。建立反向边使得我们可以"反悔"，即通过反向的通过改变来实现反悔的功能。

```C++
struct Edge
{
    Node *from, *to;
    int capacity, flow;
    Edge *next, *reverseEdge;

    Edge(Node *from, Node *to, int capacity):from(from),to(to),capacity(capacity),flow(0),next(from->edge)   {}

    ~Edge()
    {
        delete next;
    }
};
```

### makeLevelGraph()

`makeLevelGraph()`函数的作用是检查图中是否还有增广路存在，然后生成各个点的`level`值，其本身其实就是一个朴素的bfs。代码也很简单，如下:

```C++
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
            if (e->flow!=e->capacity && e->to->level==0)
            {
                e->to->level = v->level + 1;
                if (e->to == t)
                    return true;
                else
                    q.push(e->to);
            }
    }

    return false;
}
```

### findPath()

`findPath()`则是一个寻找增广路的过程，在这里使用的是dfs，并在dfs的过程中传递和更行此条增广路的最大流的值。

```C++
int findPath(Node *s, Node *t, int limit = INF)
{
    if (s==t)
        return limit;

    for (Edge *&e = s->currentEdge; e; e = e->next)
        if (e->to->level==s->level+1)
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
```

### 主函数

这部分就是一个不断判断判断能否增广然后进行增广的过程。

```C++
int ans = 0;
while (makeLevelGraph(&node[s], &node[t], n))
{
    int flow;
    while ((flow = findPath(&node[s], &node[t]))>0 )
        ans += flow;
}
```

## 例题

题目来源: [_POJ_](http://poj.org/problem?id=1273)

```C++
#include <iostream>
#include <queue>

#define MAXN 210
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
                if (e->flow!=e->capacity && e->to->level==0)
                {
                    e->to->level = v->level + 1;
                    q.push(e->to);
                }
        }

        return t->level!=0;
    }

    int findPath(Node *s, Node *t, int limit = INF)
    {
        if (s==t)
            return limit;

        for (Edge *&e = s->currentEdge; e; e = e->next)
            if (e->to->level==s->level+1)
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
            {
                ans += flow;
                // cout << "? " << flow << endl;
            }
            //cout << "! " << ans << endl;
        }
        return ans;
    }

}dinic;

int main()
{
    while (cin >> m >> n)
    {
        for (int i = 1; i<=n; i++)
        {
            delete node[i].firstEdge;
            node[i] = Node();
        }

        for (int i = 1; i<=m; i++)
        {
            int x,y,z;
            cin >> x >> y >> z;
            node[x].firstEdge = new Edge(&node[x], &node[y], z);
            node[y].firstEdge = new Edge(&node[y], &node[x], 0);

            node[x].firstEdge->reverseEdge = node[y].firstEdge;
            node[y].firstEdge->reverseEdge = node[x].firstEdge;
        }

        int ans = dinic(1, n, n);

        cout << ans << endl;
    }
}
```
