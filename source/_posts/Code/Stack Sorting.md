---
title: "Stack Sorting"
date: 2018-02-03 18:01:32
tags: 
---

# Stack Sorting

> 写出来一个玄学的做法。。。。

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/contest/911/problem/E)

### 证明

题目要求的是令一个数组stack-sortable,也就是说这个数组可以通过一个栈中转从而变成非严格递增的有序数列。

那么我们就看一看一下这样的数组需要满足什么样的条件：

对于某一个数，因为当它在栈中被取出时所有比它小的数一定已经被取出了，所以所有比它小的数在栈中一定在它上面或者已在它进栈前出栈。并且所有比它大的数只能在它下面或者未被取出。

所以，对于某一个数`x`，所有比她小的数必须满足下面两种情况之一：

1. 在它的左面；
2. 在它的右面并且从这个数到`x`之间的所有数都比`x`小。

若我们用区间来表示，那么一个stack-sortalbe的数列中对于每一个`x`都满足以下形式(每个项的位置不能改变)：
$$ x + [1,x-1] + [x+1,n] $$

那么，由于题目中已经给出了`k`个数，所以我们可以推断这`k`个数是否满足条件。

### 实现

我们要维护一个式子，其中包含数字与区间。初始时该式子中无数字，只有一个区间$ [1,n] $。

然后我们每读入一个数，就判断这个数是否在第一个区间中，是的话对区间进行处理，不是的话则这个数列不是一个stack-sortable的数列。

对区间处理时，假设插入了`x`,区间为`[l,r]`，那么若$x \neq l\ \&\ x \neq r$,就把区间分为`[l,x-1]`和`[x+1,r]`。否则直接更改区间为`[l,r-1]`或`[l+1,r]`即可。

最后生成整个数列时，只要将这些区间从前到后对于每个区间中的数从大到小输出即可。

### 代码
```C++
#include <cstdio>

int a[200100];

struct Point
{
	int l,r;
	Point* next;

	Point(int l=0,int r=0,Point* next=NULL):l(l),r(r),next(next)	{}
};

struct S
{
	int a[200100];
	Point* b;

	bool Insert(int x)
	{
		if (x < b->l || x> b->r)
			return false;

		if (x==b->l && x==b->r)
		{
			Point*p = b;
			b = b-> next;
			delete p;
		}else if (x==b->r)
		{
			b->r = x-1;
		}else if (x==b->l)
		{
			b->l = x+1;
		}else{
			Point* c = new Point(x+1,b->r,b->next);
			b->r = x-1;
			b->next = c;
		}
		a[++a[0]] = x;

		return true;
	}

	void Make()
	{
		while (b!=NULL)
		{
			for (int i = b->r; i>= b->l; i--)
				a[++a[0]] = i;
			Point* p = b;
			b = b->next;
			delete p;
		}

		return;
	}
}St;

int main()
{
	int n,k;
	scanf("%d%d",&n,&k);

	St.b = new Point(1,n,NULL);
	St.a[0] = 0;

	for (int i = 1; i<=k; i++)
	{
		scanf("%d",&a[i]);
		if (!St.Insert(a[i]))
		{
			printf("-1");
			return 0;
		}
	}

	St.Make();

	for (int i = 1; i<=St.a[0]; i++)
		printf("%d ",St.a[i]);
}
```