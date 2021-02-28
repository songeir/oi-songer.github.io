---
title: "Zero Quantity Maximization"
date: 2019-03-20 20:30:50
tags: 
---

# Zero Quantity Maximization

# CF 1133 D

<!--more-->

题目来源：[_Codeforces_](https://codeforces.com/contest/1133/problem/D)

## 分析

题目给出两个数组`a[]`和`b[]`，要求对于满足$c_i = d \cdot a_i + b_i$的数组`c[]`，当`d`取何值时`c[]`中有尽可能多的`0`。

我们只需要假设所有的`c[i]`都为`0`，然后求出满足其关系的`d`，找到出现次数最多的`d`就可以了。

这题当时做的时候最早没有用`map<>`，而是使用了排序后手动计算的方法，结果莫名其妙的出现了许多的bug，换成`map<>`之后就好了。。。此外，这里其实可以不使用`Node`，而是直接用一个`pair<int, int>`即可，只需要记住用`gcd()`将分数化为最简形式即可。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <map>

#define MAXN 200100

using namespace std;

struct Node
{
    long long a, b;
    int k;

    void getK()
    {
        if (this->a * this->b<0)
            this->k = -1;
        else this->k = 1;
    }

    const bool operator < (const Node &tmp)const{
        return abs(this->b * tmp.a) * this->k < abs(tmp.b * this->a) * tmp.k;
    }

}node[MAXN];

map<Node, int> mp;

int main()
{
    ios::sync_with_stdio(false);

    int n;
    cin >> n;

    for (int i = 1; i<=n; i++)
        cin >> node[i].a;

    for (int i = 1; i<=n; i++)
    {
        cin >> node[i].b;
        node[i].getK();
    }

    int cnt = 0;
    for (int i = 1; i<=n; i++)
        if (node[i].a==0 && node[i].b==0)
        {
            cnt ++;
        }else if (node[i].a!=0)
        {
            mp[node[i]]++;
        }

    int ans = 0;
    map<Node, int>::iterator it;
    for (it = mp.begin(); it!=mp.end(); it++)
        ans = max(ans, it->second);

    cout << ans + cnt << endl;
}
```