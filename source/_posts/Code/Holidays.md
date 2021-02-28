---
title:Holidays
date:2018-08-28 13:45:12
tags:
---

# Holidays

## Codeforces Gym 101804H

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/gym/101804/problem/H)

## 分析

这题给出了一个图，给出`q`次询问，要求每次询问中分为从点1到某点的途经城市数小于某个值的最短路。我们只需要让原来存储距离的`dist[]`变为`dist[][]`即可，一维存放的是目的地，另一维存放的是走了多少个城市。然后，在`SPFA()`运行完时递推地传递一下值，令$dist_{i,j} = min( dist_{i,k} ) , k \in [1,j] $即可。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>

#define INF 0x3f3f3f3f

using namespace std;

struct Edge
{
	int from,to,val;

	Edge(int from,int to,int val):from(from),to(to),val(val)	{}
};

struct Node
{
	int x,cnt;
	Node(int x=0,int cnt=0):x(x),cnt(cnt)	{}
};

vector<Edge> node[1010];

int dist[1010][1010];
int n,m;

bool flag[1010][1010];
queue<Node> q;
void SPFA()
{
	memset(flag,false,sizeof(flag));
	memset(dist,INF,sizeof(dist));
	q.push(Node(1,0));

	dist[1][0] = 0;

	while (!q.empty())
	{
		Node v = q.front();
		q.pop();

		//cout << "! " << v.x << " " << v.cnt << endl;

		for (int i = 0; i<node[v.x].size(); i++)
		{
			if (dist[ node[v.x][i].to ][ v.cnt+1 ] > dist[v.x][v.cnt] + node[v.x][i].val)
			{
				dist[ node[v.x][i].to ][ v.cnt+1 ] = dist[v.x][v.cnt] + node[v.x][i].val;

				if (!flag[node[v.x][i].to][v.cnt+1] && v.cnt+1<=n)
				{
					flag[ node[v.x][i].to ][v.cnt+1] = true;
					q.push( Node(node[v.x][i].to, v.cnt + 1) );
				}
			}
		}
		flag[v.x][v.cnt] = false;
	}
}

int main()
{
	cin >> n >> m;

	for (int i = 0; i<m; i++)
	{
		int x,y,z;
		cin >> x >> y >> z;

		node[x].push_back(Edge(x,y,z));
		//node[y].push_back(Edge(y,x,z));
	}

	SPFA();

	int q;
	cin >> q;

	for (int i = 1; i<=n; i++)
	{
		for (int j = 1; j<=n; j++)
		{
			dist[i][j] = min(dist[i][j], dist[i][j-1]);
			//cout << dist[i][j] << " ";
		}
		//cout << endl;
	}

	while (q--)
	{
		int x,y;
		cin >> x >> y;
		y++;

		if (dist[x][y]!=INF)
			cout << "=] " << dist[x][y] << endl;
		else cout << "=[" << endl;
	}
}

```