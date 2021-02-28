---
title: "Camp Schedule"
date: 2019-03-20 21:48:53
tags: 
---

# Camp Schedule

# CF 1137 B

<!--more-->

题目来源：[_Codeforces_](https://codeforces.com/contest/1137/problem/B)

## 分析

题目给出两个`01`串`s`和`t`，要求对`s`进行重新排列，令其含有尽可能多的`t`的子串。最简单的看，我们只需要令`s`被尽可能多的`t`的子串构成即可。

但实际上，如果`t`中存在部分前缀和部分后缀相同的情况的话就会非常麻烦。此外，还有可能`t`本身就是由数个重复串组成的。这时，我们可以用KMP中的`fail[]`数组来解决这个问题。

首先，我们需要先找出`t`中的循环节。注意，这时我们考虑的循环节，包括了`t`中的最后的后缀是循环节的一部分但并不是一个完整的循环节的情况（譬如，`ababa`的循环节即为`ab`，因为`a`也是`ab`的前缀，只是不是一个完整的循环节）。找出该循环节，我们其实可以用以下代码实现(参考于[_Cyclic Nacklace [KMP变型]_](http://songer.xyz/index.php/archives/235/))：

```C++
for (int i = t.length(); i>0; i = fail[i])
        x = max(x, i - fail[i]);
```

这样，我们其实只需要看`s`中有多少个`t`的循环节就好了。然后我们减去`t`本身有多少个循环节再加一即为答案。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <string>

#define MAXN 500100

using namespace std;

string s, t;

int fail[MAXN];

void getFail(string s)
{
    fail[0] = 0;

    for (int i = 1; i<s.length(); i++)
    {
        int j = fail[i];
        while (j && s[i]!=s[j])
            j = fail[j];
        fail[i+1] = s[i]==s[j]? j+1 : 0;
    }
}

int cnt[2];
int sum[2];
string str;

int main()
{
    cin >> s;
    cin >> t;

    getFail(t);

    str = "";
    int lent = t.length();
    int lens = s.length();
    int x = t.length();

    for (int i = t.length(); i>0; i = fail[i])
        x = max(x, i - fail[i]);

    for (int i = 0; i<lent; i++)
        cnt[ t[i] - '0' ] ++;

    for (int i = 0; i<lens; i++)
        sum[ s[i] - '0' ] ++;

    if (sum[0] >= cnt[0] && sum[1] >= cnt[1])
    {
        cout << t;
        sum[0] -= cnt[0];
        sum[1] -= cnt[1];

        cnt[0] = 0;
        cnt[1] = 0;

        for (int i = fail[lent]; i<lent; i++)
        {
            cnt[ t[i] - '0' ] ++;
            str += t[i];
        }

        while (sum[0] >= cnt[0] && sum[1] >= cnt[1])
        {
            cout << str;
            sum[0] -= cnt[0];
            sum[1] -= cnt[1];
        }

        while (sum[0]--)
            cout << 0;
        while (sum[1]--)
            cout << 1;

        cout << endl;
    }else 
        cout << s << endl;
}
```