---
title:I
date:2018-03-14 22:43:23
tags:
---

# I'm Telling the Truth

## hdu 3729

<!--more-->

题目来源: [_hdu_](http://acm.hdu.edu.cn/showproblem.php?pid=3729)

## 分析

这题第一眼看上去或许不太像二分图匹配问题。但是我们仔细研究一下便可以发现，我们可以把学生和分数当作二分图的两个部分，因为分数小于$100000$，所以我们可以直接开一个数组存储它的`belong[]`。然后就二分图匹配，找到匹配的数量，便是我们要的"说真话的学生数量"。

## 代码

```C++
#include <iostream>
#include <cstring>

using namespace std;

bool flag[100100];
int l[100],r[100];
int belong[100100];
int ans[100];

bool find(int x)
{
    for (int i = l[x]; i<=r[x]; i++)
        if (!flag[i])
        {
            flag[i] = true;
            if (belong[i]==0 || find(belong[i]))
            {
                belong[i] = x;
                return true;
            }
        }
    return false;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        memset(belong,0,sizeof(belong));

        int n;
        cin >> n;
        for (int i = 1; i<=n; i++)
            cin >> l[i] >> r[i];

        int cnt = 0;
        for (int i = n; i>0; i--)
        {
            memset(flag,false,sizeof(flag));
            if (find(i))
                ans[++cnt] = i;
        }

        cout << cnt << endl;
        for (int i = cnt; i>1; i--)
            cout << ans[i] << " ";
        cout << ans[1] << endl;
    }
}
```