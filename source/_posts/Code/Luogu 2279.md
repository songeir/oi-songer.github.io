---
title: "Luogu 2279"
date: 2019-02-10 20:12:15
tags: 
---

# Luogu 2279

> 本来Luogu给的标签是动态规划的，结果我动态规划好长时间都没有做出来。看了一下题解，发现都是贪心。。。。贪心的写法还是比较简单的。

<!--more-->

题目来源: [_Luogu_](https://www.luogu.org/problemnew/show/P2279)

## 题解

我们可以先对每个根节点分析：当我们把一个消防局放在根节点上时，它能够覆盖他的父节点、他的兄弟和他的祖父节点。而当我们把该消防局放在根节点的祖父节点上时，我们可以发现消防局同样可以覆盖这些节点，并且还能覆盖其他的节点。也就是说，这个题目是有局部最优解的，而且很明显的，因为该节点并不会影响其他节点的位置，所以没有后效性。因此我们可以使用贪心算法。

## 代码
```C++
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

int fa[1010];
int son[1010][1010];
bool flag[1010];

struct Point{
	int x,depth;
	
	Point(int x,int depth):x(x),depth(depth)	{}

	const bool operator <(const Point& tmp)const{
		return depth<tmp.depth;
	}
};

priority_queue<Point> q;

void dfs(int x,int depth)
{
	q.push(Point(x,depth));
	for (int i = 1; i<=son[x][0]; i++)
		dfs(son[x][i],depth+1);
	return;
}

void fill(int x,int dis)
{
	flag[x] = false;
	if (dis==0)
		return;

	if (x!=1)
		fill(fa[x],dis-1);
	for (int i = 1; i<=son[x][0]; i++)
		fill(son[x][i],dis-1);
	return;
}

int main()
{
	memset(flag,true,sizeof(flag));
	int n;
	scanf("%d",&n);

	for (int i = 2; i<=n; i++)
	{
		scanf("%d",&fa[i]);
		son[ fa[i] ][ ++ son[ fa[i] ][0] ] = i;
	}

	dfs(1,1);

	int ans = 0;
	while (!q.empty())
	{
		Point p = q.top(); q.pop();
		if (flag[p.x])
		{
			ans++;
			fill(fa[fa[p.x]],2);
		}
	}

	printf("%d",ans);
}
```