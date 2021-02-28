---
title:where
date:2018-03-08 10:22:15
tags:
---

# where,let,case

<!--more-->
参考书籍: [_Learn you a haskell_](http://learnyouahaskell.com/)

## where

### 用法

在编程时，我们希望避免重复计算同一个值，但我们也都知道，在Haskell中并不存在变量，那我们一般怎么存储呢？`where`便是我们常用的关键字。比如，我们现在实现一个计算语数英三科分数之和并判断等级的函数:
```Haskell
judge :: Int -> String
judge chinese math english
    | score<180 = "You got a D, foolish!"
    | score<225 = "You got a C!"
    | score<255 = "You got a B,not bad!"
    | score<=300 = "Congratulation, you got an A!"
    | otherwise = "Error score!"
	where score = chinese + math + english
```
也就是说，我们可以将`where`关键字放在哨位后面，并在后面提前将算出来的数赋值给另一个常量，这样便可以避免重复计算了。另外，`where`后可以写多个表达式，只需让它们在同一列就好了，如下:
```Haskell
judge :: Int -> String
judge chinese math english
    | score<bad = "You got a D, foolish!"
    | score<fine = "You got a C!"
    | score<good = "You got a B,not bad!"
    | score<=great = "Congratulation, you got an A!"
    | otherwise = "Error score!"
	where score = chinese + math + english
    	  great = 300
          good = 255
          fine = 225
          bad = 180
```

### 作用域

函数的`where`部分中定义的名字只对本函数可见，因此不需担心其污染其他函数的命名空间。但是，在模式匹配时`where`部分中定义的名字只在当前模式中可用，在函数的其他模式中不可用。

### where中的模式匹配

在`where`中，我们也可以使用模式匹配来绑定，如之前的内容:
```Haskell
......
	...
	where score = chinese + math + english
    	  (great, good, fine, bad) = (300, 255, 225, 180)
```
再比如，我们实现一个简单的函数，来告诉我们名字的首字母:
```Haskell
initials :: String -> String -> String
initials firstname lastname = [f] ++ "." ++ [l] ++ "."
	where (f:_) = firstname
    	  (l:_) = lastname
```

### where中的函数

在`where`部分中，我们也可以定义函数，譬如我们定义一个函数，它可以取一个由三科成绩的元组组成的列表，并返回总分:
```
judge :: [(Int,Int,Int)] -> [Int]
judge xs = [ add a b c | (a,b,c) <- xs]
	where add a b c = a + b + c
```

## let

### 用法
`let`和`where`很相似。`where`允许我们在函数底部绑定变量，而`let`则允许在任何地方定义局部变量。其用法为`let <bindings> in <expressions>`，`let`中绑定的名字仅对`in`中可见。例如:
```Haskell
average :: Int -> Int -> Int -> Int
average x y z =
	let sum = x + y + z
    in	sum/3
```
其看上去与`where`差不多，但是`let`本身是一个表达式，意味着其有返回值，因此它可以实现以下操作:
```Haskell
ghci> 4 * (let a = 9 in a + 1) + 2
42
```
以下是几个常见用法:
```Haskell
---在局部作用域中定义函数
ghci> [let square x = x * x in (square 5, square 3, square 2)]
[(25, 9, 4)]
---当一行需要绑定多个名字是，用;进行分开
ghci> [let a = 100; b = 200; c = 300 in a*b*c, let foo="Hey "; bar = "there!" in foo ++ bar)
(6000000, "Hey there!")
---结合模式匹配从元组中取出数值
ghci> (let (a, b, c) = (1, 2, 3) in a + b + c) * 100
600
```

### 列表推导式中的let

还是之前计算总成绩的函数，使用`let`写法如下:
```Haskell
judge :: [(Int, Int, Int)] -> [Int]
judge xs = [ sum | (a, b, c) <- xs, let sum = a + b + c]
```

### ghci中的let

直接在ghci中定义函数和常量是，let的in部分可以省略。如果省略，名字的定义将会在整个绘画过程中可见。

## case

### 用法

Haskell中的`case`与其他语言中的类似，能够取一个变量，根据不同的值选择代码块执行。在Haskell中，这与模式匹配类似，实际上，模式匹配本质上便是`case`的语法糖。例如，以下两段代码是完全等价的:
```Haskell
head' :: [a] -> a
head' [] = error "No head for empty lists!"
head' (x:_) = x
---
head' :: [a] -> a
head' xs = case xs of [] -> error "No head for empty lists"
					  (x:_) -> x
```
`case`表达式的结构如下:
```Haskell
case expression of pattern -> result
				   pattern -> result
                   pattern -> result
                   ...
```
此外,`case`的使用十分灵活，可以在任何地方使用。比如，可以在表达式中套用它，来执行模式匹配，其与直接使用模式匹配是等价的。
```Haskell
describeList :: [a] -> String
describeList ls = "The list is " ++ case ls of [] -> "empty."
											   [x] -> "a singleton list."
                                               xs -> "a longer list."
                                               
---

describeList :: [a] -> String
describeList ls = "The list is " ++ what ls
	where what [] = "empty."
    	  what [x] = "a singleton list."
          what xs = "a longer list."
```