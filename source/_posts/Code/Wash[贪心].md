---
title: "Wash[贪心]"
date: 2018-08-04 11:13:13
tags: 
---

# Wash[贪心]

# hdu 6000

> | 集训时的一道题，做的时候靠蒙找到了最优情况，实际上是可以严格的证明的。

<!--more-->

## 题解

较为复杂的贪心算法，其难度也主要是集中在选择其贪心策略的问题上，或者说是对贪心策略正确性的证明上。所以我们集中来看这道题的贪心策略。

题目给出了一个`w[]`数组和一个`d[]`数组，要求其中各取`L`个数，然后令其$ max( w_i + d_j )$。所以我们的目标是找到一种组合情况，使得$w_i+d_j$的最大值最小。

首先，对于从`w[]`和`d[]`数组中取出的`L`个数，我们肯定是要取出最小的`L`个。然后，我们可以粗略的看出，当我们的`w[]`越小时，我们取的`d[]`越大越好。因此，我们可以对`w[]`从小到大排序，`d[]`从大到小排序，然后每个各自相加即可。

我们可以较为严格的证明一下: 假设我们已经按照如上顺序放好。那么，我们对于$ \forall i,j (i < j)$, 其一定满足$ w_i \leq w_j , d_i \geq d_j $，所以当我们调换顺序时，这两个数中的最大值一定会大于等于原来的最大值。并且这两个数的调换不会对其他数造成影响，所以我们明显不能调换，原来的顺序即使最佳情况。

此外，还需要注意的一点: 对于此题，由于洗衣机和干洗机都可以重复使用，所以我们刚开始需要从中取出的`L`个数并不仅仅是排序后取前`L`个，而是需要考虑一个机子使用多次的情况，所以这里最好用优先队列，一个个的取出，然后再将下一次能够使用的时间放入。

## 代码

```C++
#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

struct Node
{
	long long x,base;

	Node(long long x,long long base):x(x),base(base)	{}

	const bool operator < (const Node &tmp) const{
		return x > tmp.x;
	}
};

long long t1[1000100],t2[1000100];
priority_queue<Node> q1,q2;

int main()
{
	int T;
	scanf("%d",&T);

	for (int cas = 1; cas<=T; cas++)
	{
		q1 = priority_queue<Node>();
		q2 = priority_queue<Node>();

		int l,n,m;
		scanf("%d%d%d",&l,&n,&m);

		for (int i = 1; i<=n; i++)
		{
			long long x;
			scanf("%lld",&x);

			q1.push(Node(x,x));
		}

		for (int i = 1; i<=m; i++)
		{
			long long x;
			scanf("%lld",&x);

			q2.push(Node(x,x));
		}

		for (int i = 1; i<=l; i++)
		{
			Node t = q1.top();
			q1.pop();

			t1[i] = t.x;
			t.x += t.base;

			q1.push(t);
		}

		for (int i = 1; i<=l; i++)
		{
			Node t = q2.top();
			q2.pop();

			t2[i] = t.x;
			t.x += t.base;

			q2.push(t);
		}

		long long ans = 0;
		for (int i = 1; i<=l; i++)
			ans = max(ans, t1[i] + t2[l-i+1]);

		printf("Case #%d: %lld\n",cas,ans);
	}
}
```