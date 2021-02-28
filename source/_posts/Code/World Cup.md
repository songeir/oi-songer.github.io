---
title: "World Cup"
date: 2018-12-06 20:23:18
tags: 
---

# World Cup

## CF Gym 101194 L

> 这其实就是2016年EC final的题目，发布在了CF上。这道题还是属于比较简单的一道。

<!--more-->

题目来源： [_Codeforces_](https://codeforces.com/gym/101194/attachments)

## 分析

给出了四个队伍，他们互相之间进行6场比赛。每次比赛中，获胜方加3分，失败方不加分。若平局的话则各加一分。要求对于给出的四个队伍的比赛后的分数，判断其是否合法。若合法，判断其是否可以通过该分数得出每场比赛的胜负（即得出的分数的比赛结果是否唯一）。

对于这道题，因为一个队伍只能打3场比赛，所以其最高分数就是9分。多余9分的情况接不可能。所以，我们能够用一个四位数来表示当前的状态，四个数字分别代表四个队伍的分数。这样的话，我们便可以通过一个预处理算出所有可行的情况，然后每组数据只需查询即可。

我们的预处理可以通过dfs来完成，通过枚举每场比赛的三个不同的结果，最后将当前状态的计数器加1。在查询时，若计数器为0，则说明`Wrong Scoreboard`；若计数器为1，则说明`Yes`；若计数器大于等于2，则是`No`。

## 代码

```C++
#include <iostream>
#include <algorithm>

using namespace std;

int mark[1000000];
int both[7][2] = { {0, 0}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4} };

int a[6];
void make(int cnt)
{
    //cout << a[1] << " " << a[2] << " " << a[3] << " " << a[4] << endl;
    if (cnt>6)
    {
        mark[ a[1] + a[2]*10 + a[3]*100 + a[4]*1000 ]++;
        
        //cout << a[1] + a[2]*10 + a[3]*100 + a[4]*1000 << endl;

        return;
    }

    a[ both[cnt][0] ] += 3;
    make(cnt+1);
    a[ both[cnt][0] ] -= 3;

    a[ both[cnt][0] ] += 1;
    a[ both[cnt][1] ] += 1;
    make(cnt+1);
    a[ both[cnt][0] ] -= 1;
    a[ both[cnt][1] ] -= 1;

    a[ both[cnt][1] ] += 3;
    make(cnt+1);
    a[ both[cnt][1] ] -= 3;

}

int main()
{
    int T;
    cin >> T;

    make(1);

    for (int cas = 1; cas<=T; cas++)
    {
        for (int i = 1; i<=4; i++)
        {
            cin >> a[i];
        }

        //sort(a+1, a+5);
        int sum = a[1] + a[2]*10 + a[3]*100 + a[4]*1000;
        //cout << sum << endl;

        cout << "Case #" << cas << ": ";
        if (mark[sum]==0)
            cout << "Wrong Scoreboard" << endl;
        else if (mark[sum]==1)
            cout << "Yes" << endl;
        else cout << "No" << endl;
    }
}
```