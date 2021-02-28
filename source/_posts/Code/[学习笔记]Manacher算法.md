---
title: "[学习笔记]Manacher算法"
date: 2018-12-04 19:10:38
tags: 
---

# [学习笔记]Manacher算法

## 最长回文子串

> 昨天加上今天一直在调树链剖分，然而不知为何就是一直在RE，暂时先放弃了。。。否则这几天我就不用干别的了(￣▽￣)"。

<!--more-->

## 介绍

**Manacher算法**是一个处理最长回文子串的算法，运用了巧妙地方法，将时间优化为了$O(n)$。

## 原理及流程

对于一个字符串`s`，我们用`p[]`来存储以每个点为中心的最长回文字串的右半部分的长度。

假设我们从左向右枚举处理，那么当我们处理到第$i$个时，所有的$p_j, (j<i)$明显已知。同时，我们假设我们此前记录了一个变量`maxid`，其数值为$j+p[j]$最大的$j$。那么，便会如下图所示，存在一个$j$关于$maxid$与$i$对称，因为$maxid$为中心的这个范围都是回文串，所以$p_i$便为$p_j$。

![图1](http://ovi2jbxue.bkt.clouddn.com/InblogManacher%E7%AE%97%E6%B3%95-1.png)

当然，存在另一种情况，便是$i+p_j \geq maxid + p_{maxid} $，如下图所示。此时的$p_i$只能先赋值为$maxid - i$。但是由于$maxid + p_{maxid}$向右时位置的，所以我们还需要继续向下比较，增加$p_i$，然后验证是否成立，找到最大值，顺便更新一下$maxid$。

![图2](http://ovi2jbxue.bkt.clouddn.com/InblogManacher%E7%AE%97%E6%B3%95-2.png)

我们可以看到，在第一种情况中，查找$p_i$时一个$O(1)$的操作，而在第二种情况中，查找$P_i$则需要多一个枚举，不过这个枚举明显就是对$maxid + p_maxid$的枚举，总的而言是个$O(n)$的，所以这个算法就是一个$O(n)$的算法。

不过算法到这里还有一个问题，我们一般会用$i-k$与$i+k$来判断是否是回文，但是这样判断不了偶数长度的回文，对于这个问题，manacher算法有一个巧妙地解决方法:在每个字符的中间插入一些字符。这些字符必须是相等的。此外，为了避免判断越界，我们还可以在字符串头与尾加入两个不一样的字符。如下所示:
```plain
原串:     a b c c d e f f e g
处理后: $#a#b#c#c#d#e#f#f#e#g#!
```
此时，我们还能发现一个奇特的性质，所有点的$p_i$便是其真正回文串的长度。到此，manacher算法便完成了。其核心代码如下:

```C++
int maxid = 0, id = 0;
for (int i = 0; i<str.length(); i++)
{
	if ( i < maxid )
    	p[i] = min( p[id*2 - i], maxid-i);
    else
    	p[i] = 0;
      
    while ( str[ i+p[i]+1 ]==str[ i-p[i]-1 ] )
    	p[i] ++;
    if (i+p[i]>maxid)
    {
    	maxid = i+p[i];
        id = i;
    }
}
```

## 例题及代码

题目来源: [_hdu_](http://acm.hdu.edu.cn/showproblem.php?pid=3068)

```C++
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int p[250000];

int main()
{
    string s;
    while (cin >> s)
    {
        memset(p,0,sizeof(p));

        string str;
        str.append(1, '$');
        str.append(1, '#');
        for (int i = 0; i<s.length(); i++)
        {
            str.append(1, s[i]);
            str.append(1, '#');
        }
        str.append(1, '!');

        int maxid = 0, id = 0;
        for (int i = 0; i<str.length(); i++)
        {
            if ( i < maxid )
                p[i] = min( p[id*2 - i], maxid-i);
            else
                p[i] = 0;
        
            while ( str[ i+p[i]+1 ]==str[ i-p[i]-1 ] )
                p[i] ++;
            if (i+p[i]>maxid)
            {
                maxid = i+p[i];
                id = i;
            }
        }

        int ans = 0;
        for (int i = 0; i<str.length(); i++)
        {
            ans = max(ans, p[i]);
           // cout << str[i] << " " << p[i] << endl;
        }
        cout << ans << endl;
    }
}
```