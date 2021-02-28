---
title: "Haskell基础10"
date: 2018-07-11 20:36:34
tags: 
---

# Haskell基础10

# 模块

> | 这一部分的话，按照书上的进度，应该是包括模块的使用方法、常用模块的介绍和模块的构建。这里我们先跳过常用模块的介绍，先来讲一下怎么调用模块和构造模块。

<!--more-->

参考书籍: [_Learn you a Haskell_](http://learnyouahaskell.com/)

# 导入模块

在Haskell中，导入模块的语法是`import ModuleName`,必须放置在所有的函数定义之前。我们以`Date.List`这个模块为例，假设我们要导入该模块并使用模块中的一个函数来定义一个新的函数:

```Haskell
import Data.List

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub
```

其中,`nub`是一个包含在`Data.List`模块中的函数，它能去除一个列表中的重复元素。就这样，我们快速的写出了一个计算列表中不重复元素个数的函数。

在使用GHCi时，我们一个可以导入模块只要使用如下语法即可:
```Haskell
ghci> :m + Data.List
```

并且我们可以一次性导入多个:

```Haskell
ghci> :m + Data.List Data.Map Data.Set
```

我们亦可以单独导入模块中的某几个函数，写法如下:

```Haskell
import Data.List (nub, sort)
```

我们也可以特别的指出不导入哪个函数:

```Haskell
import Data.List hiding (nub)
```

此外，为了防止函数重名，Haskell提供了两种解决方案。一种是使用`qualified`关键字进行导入，这样导入模块中的函数必须加上模块名的前缀才能调用，如下:

```Haskell
import qualified Data.Map

mapFilter = Data.Map.filter
```

而当我们认为原模块名太长不方便使用时，我们也可以使用别名的方法，如下:

```Haskell
import qualified Data.Map as M

mapFilter = M.filter
```
# 构造模块

在Haskell中，模块要遵循一个特定的结构，大致如下:

```Haskell
module [ModuleName]
{	[FunctionName1]
,	[FunctionName2]
,	......
} where

\\ function definitions here
```

其中，我们可以在一个模块的`where`语句后面导入其他模块。我们也可以定义名字不包含在大括号中的函数，但是这些函数只能在当前文件中被调用，而无法被导入该模块的代码调用。

在模块完成后，保存为正常代码的`.hs`格式，名字必须与模块名相同，然后再同一目录下进行调用便可以了。而当模块名中包含`.`时，比如名字为`Songer.Haskell`,该模块则应该处于`.\Songer\`目录下的`Haskell.hs`中。