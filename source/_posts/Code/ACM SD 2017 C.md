---
title: "ACM SD 2017 C"
date: 2018-06-13 19:35:09
tags: 
---

# ACM SD 2017 C

> 好像是除了签到题外最水的一题 ，做题时思路还算是清晰，但是第一次做时想错了。

<!--more-->

题目来源: [sdibt](http://acm.sdibt.edu.cn/JudgeOnline/problem.php?id=3265)

## 分析

题目给出了`n`个点，然后每秒钟每个点会分裂为两个点，分别移动到其左边和右边。即对于第`t`秒时存在一个点的位置为`x`，那么在`t+1`秒时便存在两个由其分裂出来的点在`x-1,x+1`。由此，我们可以得出对于一个点衍生出的所有的点的位置分布图，大致如下：
```
					1
                  1 0 1
                1 0 2 0 1
              1 0 3 0 3 0 1
            1 0 4 0 6 0 4 0 1
            	 ......
```

由此，我们可以看出其存在的规律--将其中的`0`全部去掉之后，其分布便为一个杨辉三角，即下图：
```
					1
                   1 1
                  1 2 1
                 1 3 3 1
                1 4 6 4 1
                 ......
```

而题目要求给出了`n`个点的初始位置和各自的数量之后，能够计算得出在`T`秒之后在位置`w`处的点的总数。

因此，我们可以对于每一个初始的点与`w`之间进行判断，得出由此点衍生出的图中`w`是否为`0`，若不为`0`则将根据坐标，将其化为一个求组合数的问题。

## 结论

$$ Ans = \sum_{i=1}^n cnt(i) $$


$$ cnt(i) = \left\{
\begin{aligned}
&0  &,  abs(w-x) > T	\\
&0  &,  odd(w-x-T)		\\
&C(n,m) &,even(w-x-T)  
\end{aligned}
\right.$$
$$ (n=T,m=abs(w-x+t)/2) $$

## 代码
```C++
#include <cstdio>

#define MOD 1000000007

long long a[100001];

struct FireWork
{
	int num,x;

	FireWork(int x=0,int num=1):x(x),num(num)	{}
}fire[100100];

long long abs(long long x)
{
	return x>0?x:-x;
}

void exgcd(long long a,long long b,long long &x,long long &y){
    if (b==0){
        x=1,y=0;
        return;
    }
    exgcd(b,a%b,y,x);
    y-=a/b*x;
}

long long getInverse(long long x,long long y){
    long long res,tmp;
    exgcd(x,y,res,tmp);
    return (res+y)%y;
}

long long C(long long n,long long m,long long p){//C(n,m)%p 
    
    long long tmp1=getInverse(a[m],p);
    tmp1=a[n]*tmp1%p;
    long long tmp2=getInverse(a[n-m],p);
    return tmp1*tmp2%p;
}

long long cnt(int x,int w,int t)
{
	long long dis = abs(x-w);

	if (dis > t)
		return 0;
	if ( (t-dis)%2 == 1)
		return 0;

	dis = dis/2;
	dis += (t+1)/2;
	dis = t - dis;

	//printf("!%lld %d %lld\n",dis,t,C(dis,t,MOD));

	return C(t,dis,MOD);
}

int main()
{
	int n,t,w;

	a[0] = 1;
	for (int i = 1; i<=100000; i++)
		a[i] = a[i-1]*i % MOD;

	while (scanf("%d%d%d",&n,&t,&w)!=EOF)
	{
		for (int i = 0; i<n; i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			fire[i] = FireWork(x,y);
		}

		long long ans = 0;
		for (int i = 0; i<n; i++)
			{
				ans += fire[i].num*cnt(fire[i].x,w,t);
				ans %= MOD;
			}

		printf("%lld\n",ans%MOD);

	}
}
```