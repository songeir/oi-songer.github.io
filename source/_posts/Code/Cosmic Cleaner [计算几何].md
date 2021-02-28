---
title:Cosmic Cleaner [计算几何]
date:2019-02-26 10:17:19
tags:
---

# Cosmic Cleaner [计算几何]

## Wannafly Day 1 H

题目来源：[_comet OJ_](https://zhixincode.com/contest/11/problem/H)

> 一道裸的三维计算几何题，也是当天当时唯一做出来的一道题。

<!--more-->

## 分析

这道题的题意十分好分析，其实就是求一个大球和$n$个小球的交的总和。对于球的交，我们可以先判断它们是否相交，若相交直接套用公式即可，否则要判断一下特殊情况。

## 题解

```C++

#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <cstring>

using namespace std;

const double PI = acos(-1.0);

struct Point
{
    double x, y, z;

    Point() {}

    Point(double x, double y, double z)
        :x(x), y(y), z(z) {}

    Point operator - (const Point &tmp) const
    {
        return Point(this->x - tmp.x, this->y - tmp.y, this->z - tmp.z);
    }

    Point operator + (const Point &tmp) const
    {
        return Point(this->x + tmp.x, this->y + tmp.y, this->z + tmp.z);
    }

    Point operator * (const double &k) const
    {
        return Point(this->x * k, this->y * k, this->z * k);
    }

    Point operator / (const double &k) const
    {
        return Point(this->x / k, this->y / k, this->z / k);
    }

    double operator * (const Point &tmp) const
    {
        return this->x * tmp.x + this->y * tmp.y + this->z * tmp.z;
    }
};

double dist(Point a, Point b)
{
    return sqrt( (a - b) * (a - b) );
}

struct Sphere
{
    Point center;
    double r;

    Sphere()    {};

    Sphere(Point center, double r)
        :center(center), r(r)   {}
}a[110];

double SphereInterV(Sphere a, Sphere b)
{
    double d = dist(a.center, b.center);
    double l1 = ( (a.r * a.r - b.r * b.r) / d + d) / 2.0;

    double l2 = d - l1;
    double x1 = a.r - l1, x2 = b.r - l2;

    double v1 = PI * x1 * x1 * (a.r - x1 / 3.0);
    double v2 = PI * x2 * x2 * (b.r - x2 / 3.0);

    double v = v1 + v2;
    return v;
}

int main()
{
    ios::sync_with_stdio(false);

    int T;
    cin >> T;

    for (int cas = 1; cas<=T; cas++)
    {
        memset(a, 0, sizeof(a));

        int n;
        cin >> n;

        for (int i = 1; i<=n; i++)
        {
            int x, y, z, r;
            cin >> x >> y >> z >> r;

            a[i] = Sphere(Point(x, y, z), r);
        }

        int x, y, z, r;
        cin >> x >> y >> z >> r;
        Sphere clear(Point(x, y, z), r);

        double ans = 0;
        for (int i = 1; i<=n; i++)
        {
            if ( dist(clear.center, a[i].center) + a[i].r <= clear.r)
                ans += 4.0 / 3 * PI * a[i].r * a[i].r * a[i].r;
            else if ( dist(clear.center, a[i].center) < a[i].r + clear.r)
                ans += SphereInterV(clear, a[i]);
        }

        cout << fixed;
        cout << "Case #" << cas << ": " << setprecision(20) << ans << endl;
    }
}
```