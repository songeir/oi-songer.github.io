---
title:井字棋AI
date:2018-03-14 22:43:23
tags:
---

# 井字棋AI

> 这是C++大作业中的额外作业，本来没打算做的，结果实验室的纳新试题是做一个五子棋的AI，所以就抱着练练手的目的做了一下这题，结果还挺麻烦的。

<!--more-->

## 刚开始的想法

最初，看到要写这么一个AI，我就立刻涌现出了一个想法: 对棋盘中的每个点根据不同情况赋值，最后按照值的大小来选择该下在哪里，赋值规则如下:

> * 下完此步后立刻胜利	+ 8 分
> * 敌人若下此步则立刻胜利 + 7 分 
> * 中心 + 5 分
> * 四角 + 3 分
> * 四边 + 1 分
>
> 其他： 该棋子旁每多一个己方棋子，则 + 1 分

因为该策略可以说是凭直觉确定的，所以不出意外的，并不能确保AI能够胜利或者平局。比如，下面这种特殊情况:
```
X--      X--      X--      X-O      X-O      X-O      X-O
---  =>  -O-  =>  -O-  =>  -O-  =>  -O-  =>  -O-  =>  XO-  	
---      ---      --X      --X      X-X      XOX      XOX
```

不过对于大多数情况，这个简单的"AI"还是能够应付的，而且代码也较为简短，所以我这里AI的核心代码贴在下面(完整的):
```C++
void TicTacToe::makeAutoMove()                  //robot
{
    int value[3][3] = {{3,1,3},{1,5,1},{3,1,3}};            //set default value of each point
    const int xp[] = {0,0,1,-1};
    const int yp[] = {1,-1,0,0};

    int mx,my,max = 0;

    for (int i = 0; i<3; i++)
        for (int j = 0; j<3; j++)
        {
            for (int k = 0; k<4; k++)
                if (check(i+xp[k],j+yp[k]))
                    value[i][j]++;                  //if there are a out token nearby, value++

            char c = board[i][j];
            board[i][j] = 'X';                  //pretend this point is a 'X'
            if (getWinner() == 'X')             //check could 'X' win
                value[i][j] = 7;

            board[i][j] = 'O';                  //the same as above
            if (getWinner() == 'O')
                value[i][j] = 8;

            board[i][j] = c;                    //set it back

            if (board[i][j]!='-')               //if we couldn't place a token here
                value[i][j] = 0;        

            if (value[i][j] > max)
            {
                max = value[i][j];
                mx = i;
                my = j;
            }
        }

    makeMove(mx,my);                        //put an 'O'
}
```

## 深入分析

那么，我们该怎么写这个AI程序呢？很明显，井字棋作为一个博弈游戏，我们应该通过一个估价函数来决定下一步的策略。而这个估价函数得出的值不应像上面的算法一样直接由当前棋盘决定，而是由其后续状态决定。也就是说，其实对于这一题，我们应该用极大极小值的方法将后续状态的值传递给前一状态。

### 极大极小值

#### 介绍
关于极大极小值，我们在这里阐述一下。很明显，当我们(AI)执子时，AI一定要选择最好的策略，而对于玩家执子时，我们要假设他会选择(对我们而言)最差的策略。因此，当我们想要更新当前的棋盘的价值时，若下一步是AI来下，那么我们完全可以让当前的价值等于后续状态的价值中的最大值，玩家下时则相反，我们应取最小的值。

#### 弊端
不过，对于以上的方法，其实存在一定的弊端，这个程序中也没有解决:在价值传递时会遗失一部分数据。若玩家足够聪明，这遗失的数据并无影响。但是，若玩家可能犯错的话，遗失的数据可能会令AI失去胜利的机会而变成平局。举个例子，在AI选择时，在AI看来胜利概率高的棋局和概率低的棋局是等价的，因此可能不会选择相对更佳的那个。

### 优化

若是我们使用搜索的方法获取下一步策略的价值，每走一步都需要$O(3^9)$的时间，虽然不是特别多，但是其中有大量的重复计算，而很明显的，$3^9 < 20000 $，也就是说，我们可以用预处理的方法将各个状态的棋盘的价值存储起来，从而大幅加快速度(雾。。。。

> PS：这个优化其实并不是特别必要，只是当时估错时间了，认为它很重要。。。。

#### hash

首先，我们要使用一个简单的hash函数来将棋盘的状态转化为整数，这个非常简单，代码如下:
```C++
int TicTacToe::trans()          //using hash to trans the board to a value
{
    int ans = 0;
    for (int i = 0; i<3; i++)
        for (int j = 0; j<3; j++)
        {
            ans *= 3;
            if (board[i][j] == 'X')
                ans += 1;
            else if (board[i][j] == 'O')
                ans += 2;
        }
    return ans;
}
```

#### 预处理

我们要预处理出价值，但是每个状态的价值与其下一价值有关。因此，我们应该按照棋子从多到少枚举棋盘，然后计算价值。

首先，按照棋子从多到少枚举:
```C++
void TicTacToe::robotInit()
{
    for(int i = 0; i<9; i++)
    {
        printf("[*]finished %.2f%%\n", (double)(i+1)*100/9 );
        int nx = (10 - i) /2;
        int no = ( 9 - i) /2;
        dfs(0,0,nx,no,i);
    }
}
```

#### 生成棋盘

枚举棋子数时，我们使用`dfs()`函数来生成棋盘并更新价值。其传入的参数分别为`x`坐标,`y`坐标，可下的`X`棋子数量，可下的`O`棋子数量，空格数量。

我们分别枚举`X`,`O`和`-`(代表空)，然后判断是否可以下这种棋子，递归调用，直到棋盘满为止。其中，判断条件如下:
> $nx>0$: `X`可下
> 
> $no>0$: `O`可下
>
> $x+y+nx+no<9: `-`可下

> PS:这里的`x`与`y`都是$0~2$

到达最终状态时，判断当前棋盘是否能得出结局，若可以，直接按赢+100分，输-100分，平0分赋值，若不是，则采用最大最小值的方法依照其后续状态更改他的价值。

代码写的很乱，如下:
```C++

void TicTacToe::dfs(int x,int y,int nx,int no,int blank)        //get all the possible board, and get their value
{

    if (y>2)
    {
        x ++;
        y = 0;
    }

    if (x>2)
    {
        if (getWinner()!='-')
        {
            char m = getWinner();

            if (m == 'O')
                value[trans()] = 100;
            else if (m == 'X')
                value[trans()] = -100;
            else if (m == 'V')
                value[trans()] = 0;
            else if (m == '-')
                printf("Error!"); 
        }
        else
        {
            int v = trans();
            value[v] = INF;

            for (int i = 0; i<3; i++)
                for (int j = 0; j<3; j++)
                    if (board[i][j]=='-')
                    {

                        if (blank%2)
                            board[i][j] = 'X';
                        else board[i][j] = 'O';
                        
                        if (value[v] == INF)
                        {
                            value[v] = value[trans()];
                        }
                        else if (blank%2==1)
                            value[v] = std::min(value[trans()],value[v]);           //enemy will choose the step which has the lowest value
                        else value[v] = std::max(value[trans()],value[v]);          //AI will choose the step which has the highest value

                        board[i][j] = '-';
                    }
        }

        return;
    }

    if (nx>0)
    {
        board[x][y] = 'X';
        dfs(x,y+1,nx-1,no,blank);
    }
    if (no>0)
    {
        board[x][y] = 'O';
        dfs(x,y+1,nx,no-1,blank);
    }
    if ( x*3+y + nx + no < 9)
    {
        board[x][y] = '-';
        dfs(x,y+1,nx,no,blank);
    }

    return;
}
```
