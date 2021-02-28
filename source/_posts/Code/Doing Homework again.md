---
title:Doing Homework again
date:2018-08-05 22:28:08
tags:
---

# Doing Homework again

# hdu 1789

<!--more-->

题目来源: [_HDU_](http://acm.hdu.edu.cn/showproblem.php?pid=1789)

## 分析

这道题是一道很简单的模拟题(大概)，其难点主要在于是否能够发现正确的模拟策略。而模拟本身十分简单。

题目要求怎么安排做作业才能使最后的惩罚最小。对于这道题，我们加入从前向后模拟的话，我们发现我们需要考虑两个因素:deadline和惩罚。我们既想要尽早地完成deadline较进的作业，又想要在无法避免的情况下优先完成惩罚较大的作业。此时我们会发现，想要根据这两个因素找到最合适的方案及其困难。

因此，我们便需要换一种思维了。首先，很明显，一项作业只需在deadline前完成即可，时间前后并不影响。那么，我们为什么不考虑从后向前跑呢？在从后向前跑时，我们会维护一个时间戳，表明当前的时间，然后将deadline在当前时间之后的作业加入堆中。而在这个堆中，我们只需要考虑惩罚大小这一个属性即可。而时间戳则会从后向前依次移动，并在每个时间点完成一项作业，即从大根堆中取出一个元素。

很明显，在这种算法下，我们在当前时间完成的每项作业都是目前最重要的，并且不需要考虑时间因素，因为我们是从后向前运行，所以只要还有时间，就一定能完成当前作业，否则会剩下惩罚最小的作业。

## 代码

```C++
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

struct Node
{
    int val,time;

    const bool operator < (const Node& tmp)const{
        return time > tmp.time || (time==tmp.time && val > tmp.val);
    }

}node[1010];

priority_queue<int> q;

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        q = priority_queue<int> ();

        int n;
        cin >> n;

        for (int i = 1; i<=n; i++)
            cin >> node[i].time;
        for (int i = 1; i<=n; i++)
            cin >> node[i].val;

        sort(node+1,node+1+n);

        int t = node[1].time;
        for (int i = 1; i<=n; i++)
        {
            q.push(node[i].val);

            while (!q.empty())
                if (t >= node[i].time && t>0)
                {
                    t--;
                    q.pop();
                }else break;

            t = node[i].time - 1;
        }
        while (t!=0)
        {
            if (q.empty())
                break;

            q.pop();
            t--;
        }

        long long ans = 0;
        while (!q.empty())
        {
            ans += q.top();
            q.pop();
        }

        cout << ans << endl;
    }
}
```