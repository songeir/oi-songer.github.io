---
title:[学习笔记]Splay平衡树
date:2018-12-04 19:11:37
tags:
---

# [学习笔记]Splay平衡树

> 这个代码拖得也是够久了。。一个月之前Treap写炸了之后就写了份Splay的代码，但总是毛病众多，结果直到今天才算是调出来。

<!--more-->

## 算法介绍

**伸展树(Splay Tree)**，也叫**分裂树**，是一种能自我平衡的二叉查找树，它能在均摊$O(\log n)$的时间内完成基于伸展树的插入、查找、修改和删除操作。Splay的格局，是和别处不同的(雾。Splay的目的并不是维持树的平衡，而是将上次访问的数放在最近的地方，方便下次访问。经过数学论证，可以得出其均摊时间复杂度仍为$O(\log n)$。

首先，因为Splay仍然是一棵平衡树，所以很显然会用常见的`rotate()`——旋转操作。翻转操作一般分为左旋转和右旋转，其作用是在满足二叉查找树的性质的前提下，将某个节点于其父节点进行“位置的交换”，具体效果分别如下:

![旋转操作](http://ovi2jbxue.bkt.clouddn.com/InBlog/Splay%E5%B9%B3%E8%A1%A1%E6%A0%91-1.png)

因此，Splay树中最为核心的便是`Splay()`——伸展操作。其作用是将一个节点上移到根节点，方便下次进行访问。`Splay()`具体进行的操作需要根据情况而定，可分为以下三类：

> 假设我们操作的是`node`节点。此外，我们定义一个`relation()`函数，返回该节点是其父亲的左儿子还是右儿子。

1. node节点的父亲节点就是根节点: `rotate(node);`； ![splay操作1](http://ovi2jbxue.bkt.clouddn.com/InBlog/Splay%E5%B9%B3%E8%A1%A1%E6%A0%91-2.png)
1. `node->relation() == node->fa->relation()`: `rotate(x->fa); rotate(x);`; ![splay操作2](http://ovi2jbxue.bkt.clouddn.com/InBlog/Splay%E5%B9%B3%E8%A1%A1%E6%A0%91-3.png)
1. `node->realtion() != node->fa->relation()`:  `roate(x); rotate(x)`； ![splay操作3](http://ovi2jbxue.bkt.clouddn.com/InBlog/Splay%E5%B9%B3%E8%A1%A1%E6%A0%91-4.png)

这便是Splay中比较基础的两个操作，其他具体用到的函数一般都会调用到这两个函数。其它具体函数的原理会在下面讨论。

## 实现细节

代码参考: [_Menci_](https://oi.men.ci/splay-template/)

### 节点(Node)

这是Node结构体的定义，提供了所需的属性和基本的函数:

```C++
struct Node
{
    //value为数值，size表示子树大小，cnt表示当前节点的数有多少个
    int value;
    int size, cnt;

    Node *fa, *son[2];

    //如果是左儿子就是0(L)，否则是1(R)
    bool relation()
    {
        return this == this->fa->son[R];
    }

    Node(const int &val = 0, Node *f = NULL)
        :value(val), size(1), cnt(1), fa(f)
    {
        son[L] = son[R] = NULL;
    }

    ~Node()
    {
        if (son[L])
            delete son[L];
        if (son[R])
            delete son[R];
    }
};
```

### 旋转(rotate)

旋转操作的基本原理已于上处讲过，不再赘述。这里的旋转将左旋和右旋结合在了一起。

```C++
//旋转操作
void rotate(Node *x)
{
    Node *old = x->fa;
    int flag = x->relation();

    // 将x的父节点指向x的祖父节点
    if (old->fa)
        old->fa->son[ old->relation() ] = x;
    x->fa = old->fa;

    //将x的某个儿子指向x的父亲
    if (x->son[ flag ^ 1 ])
        x->son[ flag ^ 1 ]->fa = old;
    old->son[ flag ] = x->son[ flag ^ 1 ];

    //将x的父亲指向x
    old->fa = x;
    x->son[ flag ^ 1 ] = old;

    //更新信息
    update(old);
    update(x);

    if (x->fa==NULL)
        root = x;
        
    return;
}
```

### 伸展(splay)

Splay操作也如上文所说，不再赘述。

```C++
//splay操作
Node *splay(Node *x, Node *target = NULL)
{
    if (!x)
        return x;

    while (x->fa != target)
    {
        if (x->fa->fa == target)
            rotate(x);
        else if (x->fa->relation() == x->relation() )
        {
            rotate(x->fa);
            rotate(x);
        }else
        {
            rotate(x);
            rotate(x);
        }
    }

    return x;
}
```

### 更新(update)

`update()`函数负责对节点的`size`进行更新。实现也很简单:

```C++
void update(Node *x)
{
    if (!x)
        return;

    x->size = x->cnt;
    if (x->son[L])
        x->size += x->son[L]->size;
    if (x->son[R])
        x->size += x->son[R]->size;
        
    return;
}
```

### 查找(find)

查找也是一个基础操作，按照常规的二叉查找树的搜索方法即可:

```C++
//查找某个数
Node *find(const int &value)
{
    Node *x = root;

    while (x && x->value!=value)
    {

        if (value < x->value)
            x = x->son[L];
        else
            x = x->son[R];
    }

    if (!x)
        return NULL;

    splay(x);

    return x;
}
```

### 插入(insert)

插入是平衡树中很基本的操作。在Splay中，我们在插入前首先需要考虑该数值在树内是否存在。如果存在，我们只需要让`cnt++`即可；但若是不存在，我们便需要先查找到适合插入的位置，然后新建节点插入，最后在伸展才可以。

```C++
//插入操作
Node *insert(const int &value)
{
    if (root==NULL)
    {
        root = new Node(value, NULL);
        return root;
    }

    //先查找在平衡树中是否存在
    Node *x = find(value);
    if (x)
    {
        x->cnt ++;
        x->size ++;

        return x;
    }

    //target为当前点，parent为上一次的点，mark标记target是parent的左儿子还是右儿子
    Node *target = root, *parent = NULL;
    bool mark;

    //找到需要插入的位置
    while (target)
    {
        parent = target;
        parent->size ++;

        if (value < parent->value)
            target = parent->son[mark = L];
        else 
            target = parent->son[mark = R];
    }

    //新建Node, 如果parent不是NULL的话，对parent的儿子指针进行更改
    target = new Node(value, parent);
    if (parent)
        parent->son[ mark ] = target;

    splay(target);

    return target;
}
```

### 删除(erase)

删除操作和插入操作也类似，我们需要考虑删除的数是否只存在一个。若是存在多个，我们只需要让`cnt--`即可。但是若是存在一个，我们便需要通过一个较为复杂的方法对节点进行删除。

首先，很明显，我们不能直接对一个节点进行删除，这样的话可能会破坏树的结构。那么，我们的思路便是令我们想要删除的节点`node`不存在子节点，然后再删除。对此，我们有一个较为简单的方案：先将`node`的前趋节点移到根节点，再将`node`的后继节点移到根节点的右儿子的位置。此时，步骤如下，可以看出`node`节点变成了其后继的儿子，且其没有任何儿子，所以我们可以直接进行删除。

![](![删除操作](http://ovi2jbxue.bkt.clouddn.com/InBlog/Splay%E5%B9%B3%E8%A1%A1%E6%A0%91-5.png)

代码如下:

```C++
//节点的删除操作(只删除一个)
void erase(Node *x)
{
    if (x->cnt > 1)
    {
        splay(x);
        x->cnt --;
        x->size --;

        return;
    }

    Node *pre = pred(x);
    Node *suc = succ(x);

    splay(pre);
    splay(suc, pre);

    delete x;
    if (x->fa)
        x->fa->son[ x->relation() ] = NULL;
    
    if (x==root)
        root = NULL;

    update(suc);
    update(pre);

    return;
}
```

对数的删除操作只需要对上个函数进行调用就好了:

```C++
//某个数的删除操作(只删除一个)
void erase(const int &value)
{
    erase(find(value));

    return;
}
```

### 前趋(pred)

因为我们每个节存储的是当前数值的所有数，而不是一个数，所以求前趋就非常简单了。在大多数情况下，一个数的前趋就是这个点的前趋。我们只需要求其左儿子，然后若存在右儿子，一直向下求即可:

```C++
Node *pred(Node *x)
{
    Node *pre = x->son[L];

    if (!pre)
        return NULL;
    
    while (pre->son[R])
        pre = pre->son[R];
    
    return pre;
}
```

当然，可能会存在一个节点没有左儿子的情况，这种情况下，一个节点的前趋一般为其父亲。不过，由于我们在这里一般调用的是`pred(int):int`，而在这个函数里(具体来说，是在其中调用的`find()`函数里)，我们对该节点进行了一次`splay()`，所以其一定为根节点，所以不需要考虑这种情况。

在`pred(int):int`中，我们还需要多考虑一种情况：当想要查询的数值不存在时。这是我们需要手动插入一个节点，然后查询，最后再将这个节点删除。

```C++
//查询某个数的前趋
const int &pred(const int &value)
{
    Node *x = find(value);

    if (x)
        return pred(x)->value;
    else
    {
        x = insert(value);
        const int &ans = pred(x)->value;
        erase(x);

        return ans;
    }
}
```

### 后继(succ)

后继和前趋类似，分为节点查询和数查询两个函数:

```C++
//查询某个节点的后继
Node *succ(Node *x)
{
    Node *suc = x->son[R];

    if (!suc)
        return NULL;
    
    while (suc->son[L])
        suc = suc->son[L];

    return suc;
}
```

```C++
//查询某个数的后继
const int &succ(const int &value)
{

    Node *x = find(value);

    if (x)
        return succ(x)->value;
    else
    {
        x = insert(value);
        const int &ans = succ(x)->value;
        erase(x);

        return ans;
    }
}
```

### 查询数的排名(rank)

查询排名也分为了两个函数，一个是查询节点排名，一个查询数的排名。对于节点，和前趋和后继一样，因为在`rank(int)`中伸展过，我们还是只考虑当前节点已被移到根节点的情况，较为简单，所以函数如下:

```C++
//查询某个点的排名
int rank(Node *x)
{
    return (x->son[L]==NULL) ? 0: x->son[L]->size;
}
```

对于数，我们也还是需要考虑当前数不存在的情况:

```C++
//查询某个数的排名
int rank(const int &value)
{
    Node *x = find(value);

    if (x)
        return rank(x);
    else
    {
        x = insert(value);
        int ans = rank(x);
        erase(x);

        return ans;
    }
}
```

### 查询特定排名的节点或数(select)

`select(int)`函数主要依赖`rank(int)`来运作。这里需要注意，因为在查询过程中我们没有进行`Splay()`,所以说`rank(Node*)`代表的并不是该节点的排名，而是其左子树的大小。所以我们在向右子树搜索的时候需要将当前节点和左子树的大小减去，然后搜索。

```C++
//选择第k大的数
Node *select(int k)
{
    Node *x = root;
    while ( !( rank(x)+1 <= k && (rank(x) + x->cnt >=k) ) )
    {
        
        if (k < rank(x) + 1)
            x = x->son[L];
        else
        {
            k -= rank(x) + x->cnt;
            x = x->son[R];
        }
    }

    splay(x);

    return x;
}
```


## 例题

### Luogu 3369

题目来源: [_Luogu_](https://www.luogu.org/problemnew/show/P3369)

非常裸的一道平衡树，涉及了很多基本的操作。

```C++
#include <iostream>

#define L 0
#define R 1

using namespace std;    

struct Node
{
    //value为数值，size表示子树大小，cnt表示当前节点的数有多少个
    int value;
    int size, cnt;

    Node *fa, *son[2];

    //如果是左儿子就是0(L)，否则是1(R)
    bool relation()
    {
        return this == this->fa->son[R];
    }

    Node(const int &val = 0, Node *f = NULL)
        :value(val), size(1), cnt(1), fa(f)
    {
        son[L] = son[R] = NULL;
    }

    ~Node()
    {
        if (son[L])
            delete son[L];
        if (son[R])
            delete son[R];
    }
};

struct Splay
{
    Node *root;

    Splay()
    {
        root = NULL;
    }

    ~Splay()
    {
        delete root;
    }

    //更新节点的size
    void update(Node *x)
    {
        if (!x)
            return;

        x->size = x->cnt;
        if (x->son[L])
            x->size += x->son[L]->size;
        if (x->son[R])
            x->size += x->son[R]->size;

        return;
    }

    //旋转操作
    void rotate(Node *x)
    {
        Node *old = x->fa;
        int flag = x->relation();
    
        // 将x的父节点指向x的祖父节点
        if (old->fa)
            old->fa->son[ old->relation() ] = x;
        x->fa = old->fa;

        //将x的某个儿子指向x的父亲
        if (x->son[ flag ^ 1 ])
            x->son[ flag ^ 1 ]->fa = old;
        old->son[ flag ] = x->son[ flag ^ 1 ];

        //将x的父亲指向x
        old->fa = x;
        x->son[ flag ^ 1 ] = old;

        //更新信息
        update(old);
        update(x);

        if (x->fa==NULL)
            root = x;

        return;
    }

    //splay操作
    Node *splay(Node *x, Node *target = NULL)
    {
        if (!x)
            return x;

        while (x->fa != target)
        {
            if (x->fa->fa == target)
                rotate(x);
            else if (x->fa->relation() == x->relation() )
            {
                rotate(x->fa);
                rotate(x);
            }else
            {
                rotate(x);
                rotate(x);
            }
        }

        return x;
    }

    //查询某个节点的前趋
    Node *pred(Node *x)
    {
        Node *pre = x->son[L];

        if (!pre)
            return NULL;

        while (pre->son[R])
            pre = pre->son[R];

        return pre;
    }

    //查询某个节点的后继
    Node *succ(Node *x)
    {
        Node *suc = x->son[R];

        if (!suc)
            return NULL;
        
        while (suc->son[L])
            suc = suc->son[L];

        return suc;
    }

    //查询某个点的排名
    int rank(Node *x)
    {
        return (x->son[L]==NULL) ? 0: x->son[L]->size;
    }

    //查找某个数
    Node *find(const int &value)
    {
        Node *x = root;

        while (x && x->value!=value)
        {

            if (value < x->value)
                x = x->son[L];
            else
                x = x->son[R];
        }

        if (!x)
            return NULL;

        splay(x);

        return x;
    }

    //插入操作
    Node *insert(const int &value)
    {
        if (root==NULL)
        {
            root = new Node(value, NULL);
            return root;
        }

        //先查找在平衡树中是否存在
        Node *x = find(value);
        if (x)
        {
            x->cnt ++;
            x->size ++;

            return x;
        }

        //target为当前点，parent为上一次的点，mark标记target是parent的左儿子还是右儿子
        Node *target = root, *parent = NULL;
        bool mark;

        //找到需要插入的位置
        while (target)
        {
            parent = target;
            parent->size ++;

            if (value < parent->value)
                target = parent->son[mark = L];
            else target = parent->son[mark = R];
        }

        //新建Node, 如果parent不是NULL的话，对parent的儿子指针进行更改
        target = new Node(value, parent);
        if (parent)
            parent->son[ mark ] = target;

        splay(target);

        return target;
    }

    //节点的删除操作(只删除一个)
    void erase(Node *x)
    {
        if (x->cnt > 1)
        {
            splay(x);
            x->cnt --;
            x->size --;

            return;
        }

        Node *pre = pred(x);
        Node *suc = succ(x);

        splay(pre);
        splay(suc, pre);

        delete x;
        if (x->fa)
            x->fa->son[ x->relation() ] = NULL;
        
        if (x==root)
            root = NULL;

        update(suc);
        update(pre);

        return;
    }

    //某个数的删除操作(只删除一个)
    void erase(const int &value)
    {
        erase(find(value));

        return;
    }

    //查询某个数的排名
    int rank(const int &value)
    {
        Node *x = find(value);

        if (x)
            return rank(x);
        else
        {
            x = insert(value);
            int ans = rank(x);
            erase(x);

            return ans;
        }
    }

    //选择第k大的数
    Node *select(int k)
    {
        //k++;

        Node *x = root;
        while ( !( rank(x)+1 <= k && (rank(x) + x->cnt >=k) ) )
        {
            
            if (k < rank(x) + 1)
                x = x->son[L];
            else
            {
                k -= rank(x) + x->cnt;
                x = x->son[R];
            }
        }

        splay(x);

        return x;
    }

    //查询某个数的前趋
    const int &pred(const int &value)
    {
        Node *x = find(value);

        if (x)
            return pred(x)->value;
        else
        {
            x = insert(value);
            const int &ans = pred(x)->value;
            erase(x);

            return ans;
        }
    }

    //查询某个数的后继
    const int &succ(const int &value)
    {

        Node *x = find(value);

        if (x)
            return succ(x)->value;
        else
        {
            x = insert(value);
            const int &ans = succ(x)->value;
            erase(x);

            return ans;
        }
    }

    //debug用
    void print(Node *x)
    {
        if (x)
        {
            cout << "(" << x->value << ", " << x->cnt << ")-[ ";
            print(x->son[L]);
            cout << ", ";
            print(x->son[R]);
            cout << "]";
        }
    }

}*splay;

int main()
{
    splay = new Splay();

    int n;
    cin >> n;

    for (int i = 1; i<=n; i++)
    {
        int opt;
        cin >> opt;

        int x;
        switch(opt)
        {
            case 1:
                cin >> x;
                splay->insert(x);
                break;
            case 2:
                cin >> x;
                splay->erase(x);
                break;
            case 3:
                cin >> x;
                cout << splay->rank(x)+1 << endl;
                break;
            case 4:
                cin >> x;
                cout << splay->select(x)->value << endl;
                break;
            case 5:
                cin >> x;
                cout << splay->pred(x) << endl;
                break;
            case 6:
                cin >> x;
                cout << splay->succ(x) << endl;
                break;
            default:
                cout << "Error: No such operation!" << endl;
        }
        //splay->print(splay->root);
        //cout << endl;
    }
}

```

### Luogu 3391

题目来源: [_Luogu_](https://www.luogu.org/problemnew/show/P3391)