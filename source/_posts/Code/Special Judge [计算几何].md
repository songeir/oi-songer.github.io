---
title: "Special Judge [计算几何]"
date: 2019-02-26 10:19:28
tags: 
---

# Special Judge [计算几何]

## Wannafly Day4 J

<!--more-->

题目来源：[_comet OJ_](https://zhixincode.com/contest/22/problem/J?problem_id=315)

## 分析

一道计算几何的模板题，难点在于特殊情况的判断很复杂，很容易想漏。我们需要分别对端点对端点，端点对线段，线段对线段，平行，重合并相交，重合但是线段不相交，重合并包含这几种情况分别进行判断。

## 代码

```C++
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;

const double eps=1e-8;
const double PI=acos(-1.0);
int sgn(double x)
{
    if(fabs(x)<eps) return 0;
    if(x<0) return -1;
    else return 1;
}
struct Point
{
    double x,y;
    int mark;

    Point(){}
    Point(double _x,double _y)
    {
        x=_x;
        y=_y;
    }
    bool operator == (const Point &b)const
    {
        return sgn(x-b.x)==0&&sgn(y-b.y)==0;
    }
    Point operator - (const Point &b)const
    {
        return Point(x-b.x,y-b.y);
    }
    double operator ^ (const Point &b)const
    {
        return x*b.y-y*b.x;
    }
    double operator * (const Point &b)const
    {
        return x*b.x+y*b.y;
    }
};
struct Line
{
    Point s,e;
    Line(){}
    Line(Point _s,Point _e)
    {
        s=_s;
        e=_e;
    }
};

bool inter(Line l1,Line l2)
{
    return
    max(l1.s.x,l1.e.x)>=min(l2.s.x,l2.e.x)&&
    max(l2.s.x,l2.e.x)>=min(l1.s.x,l1.e.x)&&
    max(l1.s.y,l1.e.y)>=min(l2.s.y,l2.e.y)&&
    max(l2.s.y,l2.e.y)>=min(l1.s.y,l1.e.y)&&
    sgn((l2.s-l1.e)^(l1.s-l1.e))*sgn((l2.e-l1.e)^(l1.s-l1.e))<=0&&
    sgn((l1.s-l2.e)^(l2.s-l2.e))*sgn((l1.e-l2.e)^(l2.s-l2.e))<=0;
}

bool cmp(Point p,Point q)
{
    if(p.x==q.x) return p.y<q.y;
    return p.x<q.x;
}
Point a[1010];
int u[2010],v[2010];
int ans,n,m;
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++)
        scanf("%d%d",&u[i],&v[i]);
    for(int i=1;i<=n;i++)
    {
        scanf("%lf%lf",&a[i].x,&a[i].y);
    }
    for(int i=1;i<=m;i++)
    {
        for(int j=i+1;j<=m;j++)
        {
            Line l1(a[u[i]],a[v[i]]),l2(a[u[j]],a[v[j]]);
            if(sgn((l1.e-l1.s)^(l2.e-l2.s))==0)
            {
                if(inter(l1,l2))
                {
                    Point b[5];
                    b[1]=a[u[i]];
                    b[1].mark = i;
                    b[2]=a[u[j]];
                    b[2].mark = j;
                    b[3]=a[v[i]];
                    b[3].mark = i;
                    b[4]=a[v[j]];
                    b[4].mark = j;
                    sort(b+1,b+1+4,cmp);

                    if (b[1].mark!=b[2].mark && !(b[2].x == b[3].x && b[2].y == b[3].y))
                        ans ++;

                }
            }
            else
            {
                if(inter(l1,l2)) ans++;
                if(u[i]==u[j]||v[i]==u[j]||u[i]==v[j]||v[i]==v[j]) ans--;
            }
        }
    }
    printf("%d\n",ans);
    return 0;
}
```