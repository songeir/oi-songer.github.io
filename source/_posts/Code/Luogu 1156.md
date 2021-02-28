---
title: "Luogu 1156"
date: 2018-03-03 17:08:56
tags: 
---

# Luogu 1156

> 这题还算是比较简单，看着便有些思路。感觉和背包问题比较像。

<!--more-->

题目来源: [_Luogu_](https://www.luogu.org/problemnew/show/P1156)

## 题解

由题目可得，我们想要到达的最终状态是高度为0，而这个过程中我们需要确保生命值大于0。也就是说，这道题目中存在的分支是吃掉垃圾(增加生命值)还是堆垃圾(增加高度)。而类比于背包问题，我们使用`dp[i][j]=k`来存储状态。其中`i`,`j`,`k`分别为高度，当前为第几个垃圾，生命值。

明显可以看出，在同一高度时生命值越高越好。所以，我们便可以大致得出以下的状态转移方程:

$ dp[i][j] = Max(\ dp[i][j] + f[j],\ dp[i-h[j]][j]) $

> 在这里，我们假设`t[j]`,`f[j]`,`h[j]`分别为垃圾的放入时间，所加生命值，高度。

注意，上述方程中分别代表吃垃圾和堆垃圾两种选择，而这两种选择必须是基于原本奶牛是存活的状态下才能执行，所以对于左右的两个式子，必须分别要求$dp[i][j] \geq t[j]$和$dp[i-h[j]][j] \geq t[j]$才能成立。

因为该方程与背包较为相似，所以我们也能发现该数组可以改为只包含高度的一位数组，最后在循环体内只要令高度的循环从高到低就好了。

## 代码
```C++
#include <cstdio>
#include <algorithm>
#include <cstring>

int dp[110];			//采用类似背包的优化方法，优化为一位数组

struct Garbage 			//存储有关垃圾的数据
{
	int t,f,h;

	const bool operator <(const Garbage& tmp)const{
		return t<tmp.t;			//按照t(时间)排序
	}
}garbage[110];

int main()
{
	memset(dp, 0, sizeof(0));
	int d,g;
	scanf("%d%d", &d, &g);

	for (int i=1; i<=g; i++)
		scanf("%d%d%d", &garbage[i].t, &garbage[i].f, &garbage[i].h);

	std::sort(garbage,garbage+1+g);

	dp[0] = 10;
	for (int i = 1; i<=g; i++)
	{
		for (int j = d; j>=0; j--)
		{
			if ( dp[j] >= garbage[i].t )		//首先如果本来能够到达该高度，则吃下该垃圾
				dp[j] += garbage[i].f;
			if ( j - garbage[i].h >= 0 && dp[ j - garbage[i].h ] >= garbage[i].t )		//比较吃垃圾与堆放垃圾谁剩余生命值最大
				dp[j] = std::max(dp[j], dp[ j - garbage[i].h ]);
		}
		
		if (dp[d]>0)			//如果到达了高度d，则立刻退出
		{
			printf("%d",garbage[i].t);
			return 0;
		}
	}

	//能够运行到这里说明奶牛出不来，然后直接模拟就好了
	int last = 10;
	for (int i = 1; i<=g; i++)
		if ( garbage[i].t <= last )
			last += garbage[i].f;

	printf("%d",last);
	return 0;
}
```