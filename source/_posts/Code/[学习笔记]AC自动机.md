---
title: "[学习笔记]AC自动机"
date: 2018-12-04 19:08:28
tags: 
---

# [学习笔记]AC自动机

> 这么长时间，总该学点新东西。打算新开这么一个"系列"，放一些新学的算法和数据结构。毕竟大学已经一年了，却没有在算法上继续扩宽自己的知识面，比赛时明显能感到自己知识广度的不足。

<!--more-->

## 介绍

**AC自动机**，全称是**Aho-Corasick automaton**，于1975年产生于贝尔实验室，是著名的多模式匹配算法。其主要是**Trie (字典树)** 和**KMP**算法的结合，能够找出在一个母串中多个子串的出现次数。

与KMP算法相同，其对时间的加速主要取决于失配函数。但是由于我们要实现多模式匹配，所以这里的匹配函数要针对一个Trie 树构建而非一个数组。由于每次匹配失败后我们不会重新匹配，而是根据失配函数进行跳跃，所以可以在极端情况下节省大量的时间。

## 流程及原理

AC自动机的实现流程可以分为几步：Trie树的构建；失配函数的生成；进行匹配。与KMP算法一样，失配函数的生成是其中最核心也是最困难的部分。

### Trie树的构建

首先，我们假设我们有一个母串`"ourshers"`,然后我们需要匹配子串`"our","ours","he"，
"him","she","hers"`在其中出现的总次数。因为很明显，这几个子串并没有一个公共的首字母，而我们需要将所有的串放入到一个树中，所以我们要将root节点设为空，然后在root节点的线面连接每一个单词的首字母作为子节点。最后我们生成的Trie树应该如下图所示：

![Trie树](http://ovi2jbxue.bkt.clouddn.com/InBlogAC%E8%87%AA%E5%8A%A8%E6%9C%BA-1.png)

其中，用正方形圈起来的是单词的结尾。

### 失配函数的生成

在实现AC自动机的失配函数之前，可以先回顾一下KMP算法的失配函数。假如失配函数是`f[]`,字符数组`a[]`是我们想要生成失配函数的母串，那么代码如下：

```C++
for (int i= 0; i<m; i++)
{
	int j = f[i];
    while (j && a[i]!=a[j])
    	j = f[j];
    f[i+1] = a[i]==a[j]? j+1 : 0;
}
```

我们通过不断地将当前点根据失配函数向前回溯，找到可以相同的点，来构造出下一个点的失配函数。注意，这里的失配函数满足的是$a[i-1]==a[f[i]-1]$,即失配函数会从无法匹配的字符直接跳向需要进行下一步匹配的字符。

那么，现在我们便来考虑AC自动机的失配函数。其思想和KMP类似，只不过这次我们需要用BFS来实现。在这里，我们将构建一个结构体，包含`word(char),fail(node*),son(node*[]),next(Node*),isWrod(bool)`三个成员变量(`word`主要用来debug，实际不一定用到)。

代码如下：
```C++
queue<Node*> q;
root->fail = NULL;
while(!q.empty())
{
	Node* v = q.front();
    q.pop();
	
    for (int i = 0; i<26; i++)
	{
    	Node *&c = v->c[i];
        
    	if (!c)    continue;
        
    	Node *u = v->fail; 
    	while ( u!=root && !u->c[i] )
        	u = u->fail;
            
    	c->fail = v!=root && u->c[i]? u->c[i] : root;
    	c->next = c->fail-isWord ? c->fail : c->fail->next;
        
    	q.push(c);
	}
}

```

这样的话，我们就能够得到失配函数`fail`。注意，这里的fail满足的条件是`t->word==t->fail->word`。`isWord`记录当前是否为词尾。而`next`的作用是记录最近的为词尾的当前节点的失配节点。

在完成了处理之后，我们便能够得到一个如下图的情况：

![Fail-Trie](http://ovi2jbxue.bkt.clouddn.com/InBlogAC%E8%87%AA%E5%8A%A8%E6%9C%BA-2.png)

### 模式匹配

匹配时整体思路与构建失配函数类似。我们假设母串为`s`(string类型)。所以代码如下：

```C++
Node *v = root;
for (int i = 0; i<s.length(); i++)
{
	char ch = s[i];
	while ( v!=root && !v->c[ch-‘a’])
    	v = v->fail;
	v = v->c[ch-‘a’]? V->c[ch-‘a’] : root;

	Node* t;
	if (v->isWord)
        t = v;
    else t = v->next;
        while (t)
        {
            ans ++;
            t = t->next;
        }
}

```

我们首先找到当前节点是否可以继续走下去。若是不可以，则回溯`fail`指针，找到第一个可以匹配的点。然后我们再判断该点是否为词尾，并且通过`next`指针判断其是否为其他单词的词尾。

这样，我们便完成了匹配部分。此时AC自动机的大部分功能便已经实现了。

## 例题

> 先列在这里，日后再写

### Luogu 3808

题目来源: [Luogu](https://www.luogu.org/problemnew/show/P3808)

```C++
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

struct Node
{
	char word;		//record the word
	int cnt;		//record if this word is the end of some word, and how many is it
	Node *fail;
	Node *next;
	Node *son[26];

	Node(char word=' '):word(word)
	{
		fail = NULL;
		next = NULL;
		cnt = 0;

		for (int i = 0; i<26; i++)
			son[i] = NULL;
	}
};

struct Trie
{
	Node *root;

	Trie(vector<string> s){
		root = new Node();

		for (int i = 0; i<s.size(); i++)
			build(s[i]);
	}

	void build(const string &s)
	{
		int i = 0;
		Node *p = root;

		while (i!=s.length())
		{
			if (p->son[s[i]-'a']==NULL)
				p->son[s[i]-'a'] = new Node(s[i]);

			p = p->son[s[i]-'a'];
			i++;
		}

		p->cnt ++;

		return;
	}

	void makeFail()
	{
		queue<Node*> q;
		q.push(root);
		while (!q.empty())
		{
			Node *v = q.front();
			q.pop();

			for (int i = 0; i<26; i++)
			{
				Node *&c = v->son[i];

				if (!c)	continue;

				Node *u = v->fail;
				while ( u && !u->son[i] )
					u = u->fail;

				c->fail = (v!=root && u->son[i])? u->son[i] : root;
				c->next = c->fail->cnt ? c->fail : c->fail->next;

				q.push(c);
			}

		}

		return;
	}

	int pair(string m)
	{	
		int ans = 0;

		Node *v = root;
		for (int i = 0; i<m.length(); i++)
		{
			const char &ch = m[i];

			while ( v!=root && !v->son[ch-'a'] )
				v = v->fail;

			v = v->son[ch-'a']? v->son[ch-'a'] : root;

			Node *t = v;
			while (t)
			{
				//	cout <<"* " << i << " " << t << " " << t->word << " " << t->cnt << endl;
				ans += t->cnt;
				t->cnt = 0;
				t = t->next;
			}
		}

		return ans;
	}

};

int n;
vector<string> s;
string m;

int main()
{
	cin >> n;
	for (int i = 0; i<n; i++)
	{
		string t;
		cin >> t;
		s.push_back(t);
	}
	cin >> m;

	Trie* t = new Trie(s);

	t->makeFail();

	int ans = t->pair(m);

	cout << ans;
}
```

### Luogu 3796

题目来源: [Luogu](https://www.luogu.org/problemnew/show/P3796)

```C++
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int ans[200];

struct Node
{
	char word;		//record the word
	int cnt;		//record if this word is the end of some word, and how many is it
	Node *fail;
	Node *next;
	Node *son[26];

	vector<int> words; 		//record whose end this node is.

	Node(Node *p,char word=' '):fail(p),word(word)
	{
		next = NULL;
		cnt = 0;

		for (int i = 0; i<26; i++)
			son[i] = NULL;
	}

	~Node()
	{
		for (int i = 0; i<26; i++)
			if (son[i])
				delete son[i];
	}
};

struct Trie
{
	Node *root;

	Trie(vector<string> s){
		root = new Node(NULL);
		root->fail = root;

		for (int i = 0; i<s.size(); i++)
			build(s[i],i);
	}

	~Trie()
	{
		delete root;
	}

	void build(const string &s,const int &x)
	{
		int i = 0;
		Node *p = root;

		while (i!=s.length())
		{
			if (p->son[s[i]-'a']==NULL)
				p->son[s[i]-'a'] = new Node(root,s[i]);

			p = p->son[s[i]-'a'];
			i++;
		}

		p->cnt ++;
		p->words.push_back(x);

		return;
	}

	void makeFail()
	{
		queue<Node*> q;
		q.push(root);
		while (!q.empty())
		{
			Node *v = q.front();
			q.pop();

			for (int i = 0; i<26; i++)
			{
				Node *&c = v->son[i];

				if (!c)	continue;

				Node *u = v->fail;
				while ( u!=root && !u->son[i] )
				{
					u = u->fail;
				}

				c->fail = (v!=root && u->son[i])? u->son[i] : root;
				c->next = c->fail->cnt ? c->fail : c->fail->next;

				q.push(c);

			}
		}

		return;
	}

	void pair(string m)
	{
		Node *v = root;
		for (int i = 0; i<m.length(); i++)
		{
			const char &ch = m[i];

			while ( v!=root && !v->son[ch-'a'] )
				v = v->fail;

			v = v->son[ch-'a']? v->son[ch-'a'] : root;

			Node *t = v;
			while (t)
			{
				if (t->cnt)
				{
					for (int i = 0; i<t->words.size(); i++)
						ans[t->words[i]] ++ ;
				}
				t = t->next;
			}
		}

		return;
	}

};

int n;
vector<string> s;
string m;

int main()
{
	while (cin >> n && n)
	{
		memset(ans,0,sizeof(ans));
		s.clear();

		for (int i = 0; i<n; i++)
		{
			string t;
			cin >> t;
			s.push_back(t);
		}
		cin >> m;
	
		Trie* t = new Trie(s);

		t->makeFail();

		t->pair(m);

		int maxn = 0;
		for (int i = 0; i<n; i++)
			maxn = max(maxn,ans[i]);

		cout << maxn << endl;

		for (int i = 0; i<n; i++)
			if (maxn==ans[i])
				cout << s[i] << endl;

		delete t;
	}

	return 0;
}
```