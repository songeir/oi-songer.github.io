---
title:map与filter函数
date:2018-06-13 19:35:15
tags:
---

#  map与filter函数

> 快两个月没有更Haskell了，最近也一直没有学。现在劳动节放假，趁有时间更一些。

<!--more-->

参考书籍: [_Learn you a Haskell_](http://learnyouahaskell.com/)

## map

`map`取一个函数和一个列表作为参数，它会将这个函数应用到这个列表中的每个元素，产生一个新的列表。下面为它的定义:
```Haskell
map :: (a -> b) -> [a] -> [b]
map _ [] = []
map f (x:xs) = f x : map f xs
```

以下为它的几个用法举例:
```Haskell
ghci> map (+3) [1,5,3,1,6]
[4,8,6,4,9]
ghci> map (++ "!") ("BIFF","BANG","POW"]
["BIFF!","BANG!","POW!"]
ghci> map (replicate 3) [3..6]
[[3,3,3],[4,4,4],[5,5,5],[6,6,6]]
ghci> map fst [(1,2),(3,5),(6,3),(2,6),(2,5)]
[1,3,6,2,2]
```

## filter
`filter`函数取一个谓词(preddicate)和一个列表，返回有列表中所有符合该条件的元素组成的列表(谓词指的是返回布尔值的函数)。其实现大致如下:
```Haskell
filter :: (a -> Bool) -> [a] -> [a]
filter _ [] = []
filter p (x:xs)
	| p x       = x : filter p xs
    | otherwise = filter p xs 
```

下面是一些相关的示例:
```Haskell
ghci> filter even [1..10]
[2,4,6,8,10]
ghci> let notNull x = not (null x) in filter notNull [[1,2,3],[],[3,4,5],[2,2],[],[],[]]
[[1,2,3],[3,4,5],[2,2]]
ghci> filter ('elem' ['a'..'z']) "u LaUgH aT mE BeCaUsE I aM diFfeRent"
"uagameasadifeent"
```

此外，我们还可以使用`filter`实现之前的快速排序:
```Haskell
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
	let smallerOrEqual = filter (<= x) xs
        larger = filter (> x) xs
    in quicksort smallerOrEqual ++ [x] ++ quicksort larger
```

## takeWhile

`takeWhile`函数取一个谓词和一个列表作为参数，然后从头开始遍历列表，然后一旦遇到不符合条件的元素，它就会停止执行，并返回结果列表。其实现大致如下:
```Haskell
takeWhile :: (a -> Bool) -> [a] -> [a]
takeWhile _ [] = []
takeWhile f (x:xs)
	| f x       = f x : takeWhile f xs
    | otherwise = []
```

其示例用法:
```Haskell
ghci> takeWhile (/=' ')"elephants know how to party"
"elephants"
ghci> sum (takeWhile (<10000) (filter odd (map (^2) [1..] )))
166650
```