---
title: "Haskell基础"
date: 2018-01-29 17:16:30
tags: 
---

# Haskell基础
# 函数，列表，元组
> 一些Haskell的基础语法
<!--more-->
---
## 函数定义
> * Haskell中函数不能大写字母开头

```Haskell
--函数名 :: 类型
add :: Int -> Int -> Int
doubleMe :: Int -> Int
```

## 类型
```Haskell
-- 普通类型
Int,Double,String,Char etc.
-- 函数类型
使用 -> 进行拼接
如若 add 函数需传入两个Int，输出一个Int，则其类型为
Int -> Int -> Int
-- 而当我们想要 add 函数可对任何类型进行操作操作，我们可以设置为
a -> a -> a
-- 其中a代表任意类型
-- 当我们只需对数字进行操作时，可以使用类型类进行限定，如
(Num a) => a -> a -> a
```

## 函数实现
> 通过**模式匹配**实现

```haskell
--计算平方的函数
doubleMe x = x * x

--计算平方和的函数
doubleUs x y = x * x + y * y

--将小于100的数乘2
doubleSmallNumber = if x>100
					then x
                    else 2 * x
```

## 列表
> 类似数组

1. 可以使用 `x:xs` 或 `x ++ xs`的方式来拼接列表

2. 列表支持嵌套

3. 可以通过 `!!` 函数访问列表

4. Haskell可以自动补全区间，诸如`[1..20]`或`['a'..'z']`

## 列表推导式

> 列表推导式写法类似于数学中的集合，如下：

```haskell
--1到20中的所有技术
[ x | x<-[1..20] , x 'mod' 2 /=0]

--x与y的所有乘积
[ x * y | x<-[1..20] , y<-[1..20] ]

--以上的函数一般写法
Multiply xs ys = [ x * y | x<-xs , y<-ys]
```

## 元组
> 类似结构体，可以结合不同类型的元素

> 元组中只有两个元素时被称为序对

```haskell
--使用括号进行组合
(a,b)
(a,"what",x)
--可以限定a的类型
add :: (Num a) => (a,a) -> a
add (a,b) = a + b
```
