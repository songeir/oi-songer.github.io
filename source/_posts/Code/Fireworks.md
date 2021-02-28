---
title:Fireworks
date:2018-06-13 19:35:09
tags:
---

# Fireworks

# POJ 1426

> | 最近一个多月没有更新过博客了。。。虽然上个月做题的题量还不算太少，但是都没有写博客。最近这两周考试有比较多，而我又比较懒，所以一直耽搁下来了。今天可能会把一千做过的题目整理一下，多发几个博客。题目难度可能不一，因为最近做的难题不是很多。

<!--more-->

题目来源： [vjudge](https://vjudge.net/contest/231087#problem/E) | [POJ](http://poj.org/problem?id=1426)

## 分析

这个题目其实可以算是个水题了，要求输入一个数，然后算出其最小的只包含0和1的倍数。其实就是一个暴力搜索的题目，只要搜索的时候只搜索包含0，1的数的情况便可。

## 代码

```C++
#include <cstdio>
#include <algorithm>
#include <iostream>

unsigned long long ans;

unsigned long long find(unsigned long long x,int n,int depth)
{
	if (depth>19)
		return 0;

	if (x%n==0)
	{
		//if (x<10000000)
		//	std::cout << "!" << x << " " << x%n << std::endl; 
		return x;
	}

	unsigned long long ans1 = find(x*10,n,depth+1);
	if (ans1)
		return ans1;
	unsigned long long ans2 = find(x*10+1,n,depth+1);
	if (ans2)
		return ans2;
	return 0;
}

int main()
{
	int n;
	scanf("%d",&n);
	while (n!=0)
	{		
		std::cout << find(1,n,0) << std::endl;

		scanf("%d",&n);
	}
}
```


