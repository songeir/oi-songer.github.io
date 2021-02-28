---
title: "Luogu 2278"
date: 2019-02-10 20:12:25
tags: 
---

# Luogu 2278
> | 好久以前就做了一次，没有做出来。这次又做了一遍，感觉思路清晰了不少。

<!--more-->

题目来源: [_Luogu_](https://www.luogu.org/problemnew/show/P2278)

## 分析

由题目可得，我们当前应当运行的进程应该主要取决于进程的优先级，其次取决于进程进入的时间。由于我们只需要知道优先级最高的程序，所以这明显是个堆，所以我们应该使用优先队列来完成。

## 实现步骤

我们首先维护一个当前的时间，然后有一个优先队列。

对于每一次的输入，我们都需要对优先队列进行update，从而将当前时间到此次输入开始的时间这个时间范围中能够运行完毕的进程进行输出，然后在有限队列中插入该进程。

在输入完所有进程后，依次将优先队列中的进程取出，其中应记得更新时间。

## 代码
```C++
#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

struct Point
{
	int pid,st,last,rank;

	Point(int pid=0,int st=0,int last=0,int rank=0):pid(pid),st(st),last(last),rank(rank)	{}

	void Print(int t)			//进程运行完毕时的输出
	{
		printf("%d %d\n",pid,t);
	}

	const bool operator < (const Point& tmp)const{		//将rank高或者rank相等并且st早的进程排在前面
		return rank<tmp.rank || (rank==tmp.rank && st>tmp.st);
	}
};

priority_queue<Point> q;

int main()
{
	int a,b,c,d;
	int t = 0;
	while (scanf("%d%d%d%d",&a,&b,&c,&d)!=EOF)			//这里一定要写!=EOF,否则可能超时
	{
		while ((!q.empty()) && q.top().last + t <= b)
		{
			Point p = q.top();
			t += p.last;		//更改时间
			p.Print(t);			//输出
			q.pop();			//取出已经运行完毕的而进程
		}
		if (!q.empty())			//如果还有进程的话
		{						//该进程可以运行一定时间，但是不能运行完毕
			Point p = q.top();	q.pop();
			p.last -= b - t;
			q.push(p);
		}
		t = b;		//调整时间

		q.push(Point(a,b,c,d));
	}

	while (!q.empty())		//输出所有剩下的进程
	{
		Point p = q.top();
		t += p.last;
		p.Print(t);
		
		q.pop();
	}
}
```