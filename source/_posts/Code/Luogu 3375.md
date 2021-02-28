---
title: "Luogu 3375"
date: 2018-03-03 17:12:58
tags: 
---

# Luogu 3375

> KMP算法，准确的说是KM算法，遥想很久以前写过一次，后来就再也没有动过了。现在差不多也已经忘记怎么写了，重新学习以下。

> 例题是Luogu上的一道模板题，以前做过一次，只得了70分。这次又做了一遍，结果我已经无力吐槽了。用`gets()`读入字符串0分，自己用`getchar()`手写读入是70分，用`scanf()`读入是100分。。。。。纠结了我一整个下午的问题就这么解决了○|￣|_

<!--more-->

题目来源:[_Luogu_](https://www.luogu.org/problemnew/show/P3375)

考虑字符串`a`(长度$n$),`b`(长度$m$),$m<=n$,传统的字符串匹配算法的时间复杂度是$O(mn)$的(极端情况下),而Kmp的时间复杂度是$O(m+n)$。其关键在于其前缀数组。

我们在使用传统的字符串匹配算法时，极端情况下之所以很慢，是因为我们可能会将两个字符串中的每一个字符都比较一遍。但是在很多情况下，我们知道了字符串`b`后，当我们与字符串`a`匹配失败后，我们可以显然的到向右移动一位甚至好几位之后还是无法匹配的。KMP算法就是通过预处理，算出在当前匹配失败后，`b`向右移动多少位才有可能匹配，从而节省时间。

这样，我们可以通过一个数组`f[i]`来记录右移后第几个字符能够到达`i`的位置。在匹配过程中，代码如下：
```C++
int j = 0;
for (int i = 0; i<n; i++)
{
    while (j && a[i]!=b[j])	
    	j = f[j];
    if (a[i]==b[j])	
    	j++;
    if (j==m)
    {
    	printf("%d",i-m+1);
    	break;   
    }
}
```

而整个算法中，最为神(xuan)奇(xue)的就是失配函数`f[]`的构造，其实也就是一个`b`数组对自己进行匹配的过程:
```C++
for (int i = 0; i<m; i++)
{
	int j = f[i];
    while (j && b[i]!=b[j])
    	j = f[j];
    f[i+1] = b[i]==b[j]?1:0;
}
```

> 注意：上面我们求的`f[i]`满足的条件为$b[f[i]-1] == b[i-1]$而非$b[f[i]] == b[i]$，而下列代码中的`f[i]`由于题目要求，满足的条件为$b[f[i]-1] == b[i]$.

代码:
```C++
#include <cstdio>
#include <cstring>

#define MAXN 1000100

char a[MAXN],b[MAXN];
int f[MAXN];
int n,m;
/*
void GetString(char* s,int& n)
{
	char c = getchar();
	while ((c<'A'||c>'Z') && (c<'a'||c>'z'))
		c = getchar();
	n = 0;
	while ((c>='A'&&c<='Z')||(c>='a'&&c<='z'))
	{
		s[n++] = c;
		c = getchar();
	}

	return;
}
*/
void getFail()
{
	f[0] = 0;
	//f[1] = 0;
	for (int i = 1; i<m; i++)
	{	
		int j = f[i-1];
		while (j && b[i]!=b[j])	j = f[j-1];
		f[i] = b[i]==b[j]?j+1:0;
	}

	return;
}

void find()
{
	int j = 0;
	for (int i = 0; i<n; i++)
	{
		while (a[i]!=b[j] && j) j = f[j-1];
		if (a[i]==b[j])	j++;
		if (j==m)
			printf("%d\n",i-m+2);
	}
}

int main()
{
	//GetString(a,n);
	//GetString(b,m);

	scanf("%s",a);
	scanf("%s",b);

	//gets(a);
	n = strlen(a);
	//gets(b);
	m = strlen(b);

	getFail();

	find();

	for (int i = 0; i<m; i++)
		printf("%d ",f[i]);
}
```