---
title: "H"
date: 2018-08-28 10:26:35
tags: 
---

# H-index

## Kick Start 2019 H

> 最近有好久没有做过算法题了，而且博客更是很久没有更新过了。最近Google的Kick Start快要开始了。趁这个机会，刷一刷Kick Start的题，重新找一下做算法题时的思路。

<!--more-->

题目来源：[_Kick Start_](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a274e)

## 分析

虽说这题是2019 H的第一题，然而我还是没能想到正确的做法用一个优先队列即可。题目给出了$10^5$的数据范围，虽说给了整整$50$s,但是$O(n^2)$的算法实际上还是不现实，所以我们仍要实现一个$O(n log n)$的算法。

简单地分析题目，首先可以得到一个较为显然的结论： **对于同一组数据的$n$个解，其一定是单调不下降的。** 因此，若我们维护一个值$ans$作为完成第$i$个paper时的解。那么，当$i++$时，我们我们需要做的便是将$ans++$，然后验证是否合法。若合法，则继续$ans++$，直到不合法为止。由于实际上每个$ans$只会加一次，因此不论验证步骤，该算法目前是$O(n)$的。也就是说，我们需要实现一个$O(log n)$的验证操作。

我们又可以发现，当写完第$i$个paper后，这$i$个paper中所有的citation小于$ans$的论文都对答案没有影响。也就是说，它们是“可抛弃的”。若当前确认$ans$合法，并且去验证$ans+1$是否合法，我们即可以将所有小于$ans + 1$的值抛弃，此时剩下的paper便是所有citation大于等于$ans + 1$的，若此时数目大于$ans + 1$，则说明$ans + 1$合法。实现时只需要使用一个优先队列（小根堆），然后维护当前大于等于$ans$的所有的数。若$ans$增加了，则将所有小于$ans$的值删掉，然后验证$ans$是否合法即可。最后由于所有的数只会入队和出队一次，且查询次数也为$O(n)$，所以最后该算法的时间复杂度为$O(n log n)$。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <queue>

#define MAXN 100100

using namespace std;

priority_queue<int, vector<int>, greater<int> > q;

int main()
{
    int T;
    cin >> T;

    for (int cas = 1; cas <= T; cas ++)
    {
        q = priority_queue<int, vector<int>, greater<int> >();

        int n;
        cin >> n;

        cout << "Case #" << cas << ":";

        int ans = 0;
        for (int i = 1; i<=n; i++)
        {
            int x;
            cin >> x;

            q.push(x);

            while (true)
            {
                while (q.size() && q.top() < (ans + 1))
                    q.pop();

                // cout << "! " << ans << " " << q.size() << endl;

                if (q.size() > ans)
                    ans ++;
                else
                    break;
            }

            cout << " " << ans;
        }

        cout << endl;
    }
}
```