---
title:Equivalent Prefixes [笛卡尔树]
date:2019-08-23 22:01:11
tags:
---

# Equivalent Prefixes [笛卡尔树]

## 2019牛客多校 第一场 A

<!--more-->

题目来源：[_Nowcoder_](https://ac.nowcoder.com/acm/contest/881/A)

## 分析

题目给定了`a[]`,`b[]`，要求找出最大的$p \leq n$满足$[a_1, a_2, ... , a_p]$和$[b_1, b_2, ... ,b_p]$是“相等”的。相等在这个题目中的定义为：对于长度都为`n`的序列`u[]`和`v[]`，任意的$1 \leq 1 \leq l \leq r \leq n$都能使$RMQ(u, l, r) = RMQ(v, l, r)$。$RMQ()$即为区间最小值的下标。

我们先来研究如何判断两个序列是“相等”的。很明显，由于对于任意的$l$和$r$，$RMQ(l,r)$都相同，那么这两个序列中每个数的相对顺序都是一样的。其实，这也就代表着，这两个序列构造出的[_笛卡尔树_](http://songer.xyz/index.php/archives/382/)的结构是相同的。

但是，答案要求的是“最小的满足条件的$p$”。如果我们每次都对笛卡尔树的结构做一次比较的话，由于每次要比较所有的点，所以时间为$O(n^2)$，肯定超时了。那么，还有什么能够让我们确定这两个笛卡尔树相同呢？笛卡尔树构造中的单调栈。单调栈能够唯一地反映当前插入的点的位置，只要每次的单调栈相同，那么生成的笛卡尔树一定相同。而且实际上，由于单调栈的长度变化能唯一的反映出插入点位置的变化，所以只需要每次比较单调栈的长度即可。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <stack>

#define L 0
#define R 1
#define MAXN 100100

using namespace std;

struct Node
{
    int val;
    Node *fa;
    Node *son[2];

    Node(int val = 0)
    {
        this->val = val;
        fa = NULL;
        son[L] = NULL;
        son[R] = NULL;
    }
};

struct CartesianTree
{
    stack<Node *> s;
    Node *root;

    CartesianTree()
    {
        root = NULL;
        s = stack<Node *>();
    }

    void insert(int a)
    {
        Node *next = new Node(a);
        Node *last = NULL;

        while (!s.empty())
        {
            if (s.top()->val < next->val)
            {
                Node *tmp = s.top();
                if (tmp->son[R])
                    tmp->son[R]->fa = next;
                next->son[L] = tmp->son[R];
                tmp->son[R] = next;
                next->fa = tmp;
                break;
            }
            last = s.top();
            s.pop();
        }

        if (s.empty() && last)
        {
            next->son[L] = last;
            last->fa = next;

            if (last==root)
                root = next;
        }
        if (root==NULL)
            root = next;

        s.push(next);
    }
};

int a[MAXN], b[MAXN];

int main()
{
    ios::sync_with_stdio(false);

    int n;

    while (cin>>n)
    {
        for (int i = 0; i<n; i++)
            cin >> a[i];
        for (int i = 0; i<n; i++)
            cin >> b[i];

        CartesianTree x, y;

        int i;
        for (i = 0; i<n; i++)
        {
            x.insert(a[i]);
            y.insert(b[i]);

            if (x.s.size() != y.s.size())
                break;
        }

        cout << i << endl;
    }
}
```
