---
title:Haskell基础9
date:2018-07-11 20:07:12
tags:
---

# Haskell基础9

# 扫描，\$ 和函数组合

<!--more-->

参考书籍: [_Learn you a Haskell_](http://learnyouahaskell.com/)

# 扫描

扫描，即指`scanl`和`scanr`函数。其与`foldl`和`foldr`类似，但是会将整个操作过程返回的所有值记录在一个列表中。比如：

```Haskell
ghci> scanl (+) 0 [3,5,2,1]
[0,3,8,10,11]
ghci> scanr (+) 0 [3,5,2,1]
[11,8,3,1,0]
ghci> scanl1 (\acc x -> if x>acc then x else acc) [3,4,5,3,7,9,2,1]
[3,4,5,5,7,9,9,9]
ghci> scanl (flip (:)) [3,2,1]
[[],[3],[2,3],[1,2,3]]
```
其中，`scanl`中最后的结果为列表的最后一个元素，`scanr`中为第一个元素。它可以用来跟踪折叠的执行过程。

# \$

`$`函数，也被称为**函数应用符(function application operator)**。他的定义如下：

```Haskell
($) :: (a -> b) -> a -> b
f $ x = f x
```

看上去这个符号似乎没有任何意义。但是实际上因为`$`拥有最低的优先级，并且它是右结合的(一般的函数是左结合的)，所以可以起到替代括号的作用。像下面的几种写法就是等价的:

```Haskell
sqrt (3 + 5)
sqrt $ 3 + 5

sum ( filter (> 10) (map (*2) [2..10] ))
sum $ filter (> 10) $ map (*2) [2..10]

```

`$`是右结合的，所以`f $ g $ x`和`f $ ( g $ x )`等价。因此，我们可以省去很多在最后的括号。

除了减少括号外，`$`还能够将函数应用转为函数，这就允许我们映射一个函数应用到一组函数组成的列表:

```Haskell
ghci> map ($ 3) [(4+), (10*), (^2)]
[7.0, 30.0, 9.0]
```

# 函数组合

## 定义

在数学中，**函数组合(function composition)**是这样定义的:$ (f \cdot g) (x) = f (g (x)) $。而在Haskell中的函数组合也与之类似，其符号为`.`。定义为：
```Haskell
(.) :: (b -> c) -> (a -> b) -> a -> c
f . g = \x -> f ( g x )
```

在进行函数组合时，我们要确保函数`g`的返回值与`f`的参数类型相同。其使用很简单，我们可以用其将几个函数生成一个新函数:

```
map (\x -> 3*x+1)
等价于
map ((+1) . (*3))
```


## 带有多个参数的函数组合

对于带有多个参数的函数，当我们想要使用函数组合时，我们可以通过部分应用来时所有函数只剩下一个参数，然后再使用。如下面的几个式子便是等价的:

```Haskell
sum (replicate 5 (max 6.7 8.9))
(sum . replicate 5) (max 6.7 8.9)
sum . replicate 5 $ max 6.7 8.9
```

## Point-Free 风格

函数组合的另一用途便是定义**Point-Free风格**，也称为Pointless风格。通过去掉函数定义中重复的变量，让代码更加简洁和易读。比如下面的代码:

```Haskell
sum' xs = foldl (+) 0 xs
改为
sum' = foldl (+) 0

fn x = ceiling (negate (tan (cos (max 50 x))))
改为
fn = ceiling . negate . tan . cos . max 50
```