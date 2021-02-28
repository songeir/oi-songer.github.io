---
title: "Sorting"
date: 2018-02-03 18:01:32
tags: 
---

# Sorting

## hdu 6281

<!--more-->

题目来源: [_hdu_](http://acm.hdu.edu.cn/showproblem.php?pid=6281)

## 分析

题目本身是比较简单的，要求输出字典序最小的序列`P`，使其满足下面的式子:

$$ \frac{ a_{p_{i-1}} + b_{p_{i-1}} }{ a_{p_{i-1}} + b_{p_{i-1}} + c_{p_{i-1}} } \leq \frac{ a_{p_i} + b_{p_i} }{ a_{p_i} + b_{p_i} + c_{p_i} } $$

我们只需要按照上面的式子对`a,b,c`构成的结构体排序，就可以得到答案。不过这题的问题在于用浮点数会产生浮点误差，而用整数的话则会爆`long long`。所以我们需要化简一下式子:

$$ \begin{aligned} \frac{c_{p_{i-1}}}{a_{p_{i-1}} + b_{p_{i-1}} + c_{p_{i-1}}} & \geq \frac{c_{p_i}}{a_{p_i} + b_{p_i} + c_{p_i}} \\	\frac{c_{p_{i-1}}}{a_{p_{i-1}} + b_{p_{i-1}} } & \geq \frac{c_{p_i}}{a_{p_i} + b_{p_i}} \\	c_{p_{i-1}} \times ( a_{p_i} + b_{p_i} ) & \geq c_{p_i} \times ( a_{p_{i-1}} + b_{p_{i-1}} )	\end{aligned} $$

## 代码

```C++
#include <iostream>
#include <algorithm>

using namespace std;

struct Node
{
    long long val[2];
    int id;

    Node(int a,int b,int c,int id):id(id)
    {
        val[0] = (long long)c;
        val[1] = (long long)a+b;
    }

    Node()  {}

    const bool operator < (const Node &tmp)const{
        return (val[0]*tmp.val[1] > tmp.val[0]*val[1]) || (val[0]*tmp.val[1] == tmp.val[0] * val[1] && id < tmp.id);
    }
}node[1010];

int main()
{
    int n;
    while (~scanf("%d",&n))
    {
        for (int i = 1; i<=n; i++)
        {
            int x,y,z;
            cin >> x >> y >> z;

            node[i] = Node(x,y,z,i);
        }

        sort(node+1, node+1+n);

        for (int i = 1; i<n; i++)
            cout << node[i].id << " ";
        cout << node[n].id << endl;
    }
}
```