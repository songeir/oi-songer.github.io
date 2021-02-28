---
title:Efficient Tracking
date:2018-08-28 13:44:49
tags:
---

# Efficient Tracking

## CF Gym 101804E

> 这已经是一周前做的题目了，果然我真是能鸽善鹉。。。。

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/gym/101804/problem/E)

## 分析

这题是很常规的一道题目，其实总体而言就是求最大生成树。不过在求完之后还需要再搜索一遍，然后以节点1为根节点建树即可。

## 代码

```C++
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

struct Edge
{
	int from,to,val;

	Edge(int from=0,int to=0,int val=0):from(from),to(to),val(val)	{}

	const bool operator < (const Edge &tmp)const{
		return val > tmp.val;
	}
}e[1000100];

struct Node
{
	vector<int> e;
}node[1010];

int fa[1010];
int anc[1010];

int find(int x)
{
	return x==fa[x]? x : fa[x] = find(fa[x]);
}

int dfs(int x)
{
	for (int i = 0; i<node[x].e.size(); i++)
		if (anc[node[x].e[i]]==0)
		{
			anc[node[x].e[i]] = x;
			dfs(node[x].e[i]);
		}
}

int main()
{
	int n;
	cin >> n;

	for (int i = 1; i<=n; i++)
		fa[i] = i;

	int num = 0;
	for (int i = 2; i<=n; i++)
		for (int j = 1; j<i; j++)
		{
			int x;
			cin >> x;
			e[++num] = Edge(i,j,x);
		}

	sort(e+1,e+1+num);

	long long ans = 0;
	int cnt = 1;
	for (int i = 1; i<=num; i++)
	{
		int fx = find(e[i].from);
		int fy = find(e[i].to);

		if (fx!=fy)
		{
			fa[fx] = fy;

			node[e[i].from].e.push_back(e[i].to);
			node[e[i].to].e.push_back(e[i].from);
			ans += e[i].val;

			cnt ++;
		}

		if (cnt==n)
			break;
	}

	dfs(1);

	cout << ans << endl;
	for (int i = 2; i<=n; i++)
		cout << anc[i] << endl;
}
```