---
title: "Codeforeces Edu 37 D"
date: 2018-02-18 17:06:05
tags: 
---

# Codeforeces Edu 37 D

> |这题真的是一点思路也没有，好不容易看懂了题解写完了，结果发现理解出了偏差（；´д｀）ゞ

<!--more-->

题目来源: [_Codeforces_](http://codeforces.com/contest/920/problem/D)

## 题解
### 思路
在计算怎么转移之前，我们需要先判断是否能够转移出水的体积为`V`的水桶。

那么，首先我们可以得出，对于$ sum = \sum^n_{i=1}{v[i]} $，若$sum<V$则不可能。

然后我们判断什么时候可以转移。我们可以发现当$ V\%k == 0$时，我们永远可以得到一个水的体积为`V`的水桶。

而当`V`不是`k`的整数倍时，`V`中$V\%k$这一部分肯定能够从其它桶凑出。只有此时能够得到一个体积为`V`的水桶。

然后我们便需要算出是否有几个水桶水量的和能够与`V`同余。这里我们需要用到简单的动态规划(但我还是把它忘了。。。)。使用`dp[i][j]`记录到第`i`个数是否能取到同余`k`为`j`的值。

最后只要输出移动方法就行了。因为改题目非固定答案，所以我们可以"套模板",即使用麻烦但是能够达成效果的方法进行移动。

我们可以使用一个`flag[i][j]`来记录在到达位置`i`且`%k==j`时是否取了`i`这个位置的数。

然后我们把所有取了的数移到一个位置`x`，没有取的移到一个位置`y`,再用`y`把`x`中的水加至体积为`V`便可以了。
### 结论

#### 判断

1. $sum < V$时: NO
2. $sum\%k==0$时: YES
3. $ \exists S$使得$\sum_{i\in S}{v[i]} \equiv V(\mod k)$: YES
4. Otherwise: NO

> ($S$为取出的数的下标的集合)
> 
> 第2中情况其实可以直接被第三种情况包括，只要初始从`dp[0][0] = true`开始即可。

#### DP
我们使用`dp[i][j]`来表示到第`i`个数时能否有取法`S`使得$\sum_{i\in S}{v[i]} \equiv V(\mod k)$。那么转移方程如下:
$$ dp[i][j] = dp[i-1][j]\ || \ dp[i-1][Mod(j-v[i],k)]$$

其中或运算符左边的是不取当前数值的情况，右边是取当前数值的情况。

> 这里使用自己写的`Mod()`函数是为了防止`CPP`的`%`算出负值。
> 
> 在`f[i][Mod(j-v[i],k)]`为`True`时`flag[i][j]`为`True`

#### 转移步骤

## 代码
```C++
#include <cstdio>
#include <cstring>

bool dp[5010][5010];
bool flag[5010][5010];
int v[5010];

int Mod(int a,int b)
{
	while (a<0)
		a += b;

	return a%b;
}

int main()
{
	memset(dp,false,sizeof(dp));
	memset(flag,false,sizeof(flag));

	int n,k,V,sum = 0;
	scanf("%d%d%d",&n,&k,&V);

	for (int i =1; i<=n; i++)
	{
		scanf("%d",&v[i]);
		sum += v[i];
	}

	if (sum<V)				//sum<V时输出NO
	{
		printf("NO\n");
		return 0;
	}

	dp[0][0] = true;			//初始值
	for (int i = 1; i<=n; i++)
		for (int j = 0; j<k; j++)
		{
			if (dp[i-1][j])				//当前数值不取的情况
				dp[i][j] = true;
			else if (dp[i-1][Mod(j-v[i],k)])		//取当前数值的情况
			{
				dp[i][j] = true;
				flag[i][j] = true;
			}
		}
	/*
	for (int i = 1; i<=n; i++)
	{
		for (int j = 0; j<k; j++)
			printf("%d ",dp[i][j]);
		printf("\n");
	}
	*/
	if (dp[n][V%k])
	{
		printf("YES\n");

		int t1=0,t2=0;	//分别代表取了的数和没取的数转移到的位置

		int j = V%k,i=n;
		while(i>0)
		{
			if (v[i]==0)
			{
				i--;
				continue;
			}
			if (flag[i][j])
			{
				j = Mod(j-v[i],k);
				if (!t1)
					t1 = i;
				else{
					printf("%d %d %d\n",(v[i]+k-1)/k,i,t1);
					v[t1] += v[i];
					v[i] = 0;
				}
			}else{
				if (!t2)
					t2 = i;
				else{
					printf("%d %d %d\n",(v[i]+k-1)/k,i,t2);
					v[t2] += v[i];
					v[i] = 0;
				}
			}
			i--;
		}

		if (V%k==0 && V!=0)
		{
			if (t2!=1)	t1=1;
			else t1 = 2;
			printf("%d %d %d\n",V/k,t2,t1);
		}
		else if (t1 && V!=v[t1])
		{
			if (!t2)
			{
				if (t1==1)	t2=2;
				else t2 = 1;
			}
			if (v[t1]<V)
				printf("%d %d %d\n",(V-v[t1])/k,t2,t1);
			else printf("%d %d %d\n",(v[t1]-V)/k,t1,t2);
		}

	}else printf("NO");
}
```