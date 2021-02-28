---
title: "Connect"
date: 2019-02-25 14:55:41
tags: 
---

# Connect

## CF Contest 542 C

<!--more-->

题目来源：[_codeforces_](https://codeforces.com/contest/1130/problem/C)

## 分析

这题还算是很裸的题目。我们首先通过BFS分别找到所有和起点和终点相连的点，然后将它们之间一一计算距离，取最小值即可。

## 代码

```C++
#include <iostream>
#include <cstring>
#include <queue>
#include <cstdio>

#define MAXN 55
#define INF 0x3f3f3f3f

using namespace std;

int n;
int a[MAXN*MAXN][2], b[MAXN*MAXN][2];
int an = 0, bn = 0;
char mp[MAXN][MAXN];
bool flag[MAXN][MAXN];

const int xp[] = {-1, 1, 0, 0};
const int yp[] = {0, 0, -1, 1};

bool in(int x,int y)
{
    return x>0 && x<=n && y>0 && y<=n;
}

queue< pair<int, int> > q;
void mk(int x, int y, int res[MAXN][2], int &cnt)
{
    memset(flag, false, sizeof(flag));
    while (!q.empty())
        q.pop();

    res[++cnt][0] = x;
    res[cnt][1] = y;

    flag[x][y] = true;
    q.push( pair<int, int>(x, y) );
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i<4; i++)
            if ( flag[x + xp[i]][y + yp[i]] == false && mp[x+xp[i]][y+yp[i]]=='0' && in(x+xp[i], y+yp[i]))
            {
                flag[x + xp[i]][y + yp[i]] = true;
                res[++cnt][0] = x + xp[i];
                res[cnt][1] = y + yp[i];
                q.push( pair<int ,int >(x + xp[i], y + yp[i]) );
            }
    }
}

int main()
{
    cin >> n;

    int sx, sy, ex, ey;
    cin >> sx >> sy;
    cin >> ex >> ey;

    for (int i = 1; i<=n; i++)
    {
        for (int j = 1; j<=n; j++)
            cin >> mp[i][j];
        getchar();
    }

    mk(sx, sy, a, an);
    mk(ex, ey, b, bn);

    int ans = INF;
    for (int i = 1; i<=an; i++)
        for (int j = 1; j<=bn; j++)
        {
            int xd = a[i][0] - b[j][0];
            int yd = a[i][1] - b[j][1];

            // cout << a[i][0] << " " << a[i][1] << endl;
            // cout << b[j][0] << " " << b[j][1] << endl;
            
            ans = min(ans, xd * xd + yd * yd);
        }

    cout << ans << endl;
}
```