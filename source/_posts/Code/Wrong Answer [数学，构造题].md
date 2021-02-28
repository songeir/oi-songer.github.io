---
title:Wrong Answer [数学，构造题]
date:2019-02-25 15:34:37
tags:
---

# Wrong Answer [数学，构造题]

## CF Contest 542 E

<!--more-->

题目来源：[_codeforces_](https://codeforces.com/contest/1130/problem/E)

## 分析

这题算是一个十分有趣的题目，题目给出了一个代码，目标是求最大的$(r-l+1)*\sum_{i=l}^r a_i$，但是代码是错的。题目给出一个$k$，要求构造一组数据，该代码与正确答案的差恰好为$k$。

由于这题是构造题，那么我们尽可以向特殊情况去考虑。我采用了一种$0, -1, a_3, ..., a_n$的结构，这里$a_3$到$a_n$都大于$0$。那么实际上此时我们可以确定正确答案一定为$n \sum_{i=1}^n a_i$，并且题目给出的代码算出的一定是$(n-2) \sum_{i=3}^n a_i$。此时，我们就可以给出一个$k$的等式：

$$ k = n \sum_{i=1}^n a_i - (n-2) \sum_{i=3}^n a_i $$

$$ k = n \times (a_1 + a_2) + n \sum_{i=3}^n a_i - (n - 2) \sum_{i=3}^n a_i $$

$$ k = n \times (a_1 + a_2) + 2 \sum_{i=3}^n a_i $$

$$ k = 2 \sum_{i=3}^n a_i - n $$

又因为$a_i \leq 1e6$，所以：

$$ \frac{k + n}{2} = \sum_{i=3}^n a_i $$

$$ \frac{k+n}{2 \times (n -2)} = a_i $$

$$ \frac{k+2}{2 \times (n-2)} + \frac{1}{2} = a_i \leq 1e6 $$

所以，我们只需要随便找到一个能够满足上述不等式的$n$，然后再带回去算出$\sum_{i=3}^n a_i$，然后将它们分到$n-2$个位置即可。

此外，我们还需要注意奇偶的问题。由于$k+n$一定是$2$的倍数，所以我们要根据$k$的奇偶性来确定$n$的奇偶性。

## 代码

```C++
#include <iostream>
#include <algorithm>

using namespace std;

int ans[2010];

int main()
{
    int k;
    cin >> k;

    int n = 3;
    ans[1] = 0;
    ans[2] = -1;

    if (k % 2 == 1)
    {
        for (; (k+2) / (n-2) > 1e6; n++);

        int t = ( k + n ) / 2;
        for (int i = 3; i<=n; i++)
        {
            ans[i] = t / (n - i + 1);
            t -= ans[i];
        }
    
    }else
    {

        for (; (k+2) / (n-2) > 1e6; n++);
        if (n%2==1)
            n++;

        int t = ( k + n ) / 2;
        for (int i = 3; i<=n; i++)
        {
            ans[i] = t / (n - i + 1);
            t -= ans[i];
        }
    }

    cout << n << endl;
    for (int i = 1; i<=n; i++)
        cout << ans[i] << " ";

}
```