---
title: "Tree Constructing"
date: 2018-07-05 15:41:58
tags: 
---

# Tree Constructing

## CF 494 E

> | 这次是div3的题目，本身没有涉及到什么复杂的算法，可以说就是一道模拟题。不过细节还是很多的，需要注意。比赛时因为漏掉了一个细节结果比赛后被hack了，否则这次div3能排到一百多名(〒▽〒)。。。。

<!--more-->

## 题解

题目要求给定顶点数`n`,直径`d`,和最大度数`k`，是否有这样的数存在。存在的话输出这棵树的所有边。

首先，这里的`n`和`d`都是必须正好满足的，而`k`则是要求树最大度数小于等于`k`即可。所以，在这里，我们应该先从`d`入手。

很明显，我们可以首先尝试构建一个最长边，它总共包含`d+1`个点。所以，若$ n \le d $，就可以直接输出`"NO"`。

而当我们构建最长边时，若$d+1==1$，则必须满足$k\ge0$；若$ d+1==2$，则必须满足$k\ge1$;若$d+1\ge3$,则必须满足$ k \ge 2 $。所以若以上条件不满，我们也可以输出`"NO"`。

在最长边构建完成之后，我们便可以开始构建其他的边了。很明显，其他的边都是由最长边上的点为根节点延伸出来的，也就是说，其他的边集构成了一个根节点为最长边上的点的若干个子树。所以说，我们在最长边上一直生成子树，就能够形成一个满足最终条件的树。

当然，也存在不满足条件的情况。若我们已经构建了所有满足情况的子树之后，结点数还是小于`n`的话，说明无法构建，此时应该输出`"NO"`。

还有，我们该如何生成一个符合条件的子树呢？我们可以使用一个递归的建树函数，分别传入该点的序号，该点剩余的度数和该点向下还能够建树的深度。这样的话当深度为`0`是直接返回，从而使我们生成的子树不会令最长边变长。

## 代码

```C++

#include <iostream>

using namespace std;

int n,d,k;
int cur;

int ans[400100][2];
int num = 0;

void build(int x,int t,int kk)
{
	if (t==0)
		return;

	if (cur>n)
		return;

	for (int i = 0; i<kk; i++)
	{
		ans[num][0] = x;
		ans[num][1] = cur;
		cur ++;
		num ++;

		if (cur > n)
			return;

		build(cur-1,t-1,k-1);

		if (cur > n)
			return;
	}
}

int main()
{

	cin >> n >> d >> k;
	d++;

	if (n < d || (d>2 && k==1) )
	{
		cout << "NO";
		return 0;
	}
	for (int i = 1; i<d; i++)
	{
		ans[num][0] = i;
		ans[num][1] = i+1;
		num++;
	}
	cur = d+1;

	for (int i = 1; i<=d; i++)
		build(i,min(i-1,d-i),k-2);

	//cout << "! " << num << endl;
	if (num!=n-1)
		cout << "NO" << endl;
	else{
		cout << "YES" << endl;
		for (int i = 0; i<num; i++)
			cout << ans[i][0] << " " << ans[i][1] << endl;
	}
}

```
