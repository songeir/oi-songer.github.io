---
title:Maze
date:2018-08-28 13:35:06
tags:
---

# Maze

# Codeforces Problem 377A

> 这题也算是一道比较好些的题目，但是前提是能想出正确的解法。

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/problemset/problem/377/A)

## 分析

题目要求在给出的棋盘中加入$k$面墙，并且能够使得最后所有空白的块联通。如果我们从墙的角度出发，实际判断该从哪里放墙是十分复杂的。但是如果我们从空白的角度出发，我们会发现我们的目的只是确保空白块联通即可。所以我们可以先将所有的空白块设为`X`（墙），然后从其中某一点开始搜索，生成一个制定大小的联通块即可。

## 代码
```C++
#include <iostream>
#include <queue>

using namespace std;

char a[510][510];

struct Node{
	int x,y;
	Node(int x,int y):x(x),y(y)	{}
};

queue<Node> q;
const int xp[] = {0,0,-1,1};
const int yp[] = {1,-1,0,0};

void bfs(int x,int y,int cnt)
{
	if (cnt==0)
		return;

	q.push(Node(x,y));

	while (!q.empty())
	{
		Node t = q.front();
		q.pop();
		if (a[t.x][t.y]=='.')
			continue;

		a[t.x][t.y] = '.';

		//cout << "[ " << t.x << ", " << t.y << "] in " << cnt << endl;
		cnt --;
		if (cnt==0)
			break;

		for (int i = 0; i<4; i++)
			if (a[t.x+xp[i]][t.y+yp[i]]=='X')
				q.push(Node(t.x+xp[i],t.y+yp[i]));
	}
}

int main()
{
	int n,m,k;
	cin >> n >> m >> k;

	for (int i = 0; i<=n+1; i++)
		for (int j = 0; j<=m+1; j++)
			a[i][j] = '#';

	int cnt = n * m;
	for (int i = 1; i<=n; i++)
		for (int j = 1; j<=m; j++)
		{
			cin >> a[i][j];
			if (a[i][j]=='#')
				cnt --;
			else a[i][j] = 'X';
		}

	bool flag = false;
	for (int i = 1; i<=n; i++)
	{
		for (int j = 1; j<=m; j++)
			if (a[i][j]=='X')
			{
				bfs(i,j,cnt-k);
				flag  = true;
				break;
			}
		if (flag)
			break;
	}

	for (int i = 1; i<=n; i++)
	{
		for (int j = 1; j<=m; j++)
			cout << a[i][j];
		cout << endl;
	}
}
```