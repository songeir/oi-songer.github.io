---
title: "Triangle Partition"
date: 2018-08-28 13:48:56
tags: 
---

# Triangle Partition

## hdu 6300

<!--more-->

题目来源: [_hdu_](acm.hdu.edu.cn/showproblem.php?pid=6300)

## 分析

题目给出了$3n$个点，要求用它们组成$n$个互不相交的三角形。并且题目保证了不存在共线的点。所以我们只需要按照$x$坐标排序，然后每三个组成一个三角形即可。

## 代码

```C++
#include <iostream>
#include <algorithm>

using namespace std;

struct Node
{
    int x,y,id;
    
    const bool operator <(const Node &tmp)const{
        return x < tmp.x ;
    }
}node[3010];

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int n;
        cin >> n;

        for (int i = 1; i<=3*n; i++)
        {
            cin >> node[i].x >> node[i].y;
            node[i].id = i;
        }

        sort(node+1, node+3*n+1);

        for (int i = 1; i<=n; i++)
        {
            cout << node[i*3-2].id << " " << node[i*3-1].id << " " << node[i*3].id << endl;
        }
    }
}
```