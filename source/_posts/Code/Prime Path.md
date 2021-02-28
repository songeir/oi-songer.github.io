---
title:Prime Path
date:2018-06-13 19:34:50
tags:
---

# Prime Path

# POJ 3126

> | 这道题也可以算是到水题吧。搜索加上求素数，这里用的是线性筛。

<!--more-->

题目来源: [vjudge](https://vjudge.net/contest/231087#problem/F) | [POJ](http://poj.org/problem?id=3126)

## 分析

题目要求很简单，给定一个起点和终点，要求用最短的步数到达。每改变一个数算作一步，并且在改变后要求仍然为素数。所以先算出所有素数，然后进行暴力BFS即可。

## 代码

```C++
#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

bool prime[10100];
int dist[10100];
int n;

void Prime()
{
	for (int i = 1; i<=10000; i++)
		prime[i] = true;

	prime[1] = false;
	prime[2] = prime[3] = true;
	for (int i = 2; i<=100; i++)
		if (prime[i])
		{
			int j = i*i;
			while (j<=10000)
			{
				prime[j] = false;
				j += i;
			}
		}
	return;
}

queue<int> q;
int main()
{
	Prime();

	cin >> n;
	for (int k = 1; k<=n; k++)
	{
		memset(dist,0,sizeof(dist));

		int x,y;
		cin >> x >> y;
		
		q = queue<int>();
		dist[x] = 1;
		q.push(x);
		while (!q.empty())
		{
			int v = q.front();	q.pop();
			//printf("!%d %d\n",v,dist[v]);

			if (v==y)
				break;

			int t = 1;
			for (int i = 0; i<4; i++)
			{
				for (int j = 0; j<=9; j++)
				{
					int z;
					if (t==1)
						z = v/(t*10)*(t*10) + t*j;
					else z = v/(t*10)*(t*10) + t*j + v%t;
					
					if (dist[z]==0 && prime[z] && z>=1000)
					{
						dist[z] = dist[v] + 1;
						q.push(z);
					}
				}

				t *= 10;
			}
		}
	
		cout << dist[y]-1 << endl;
	}
}
```
