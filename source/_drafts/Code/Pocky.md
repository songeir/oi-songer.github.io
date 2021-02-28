---
title:Pocky
tags:
---

# Pocky

# hdu 5984

> 作为一个从头到尾没看出规律，推积分又没推出来的人，我在比赛时是绝望的。。。。

<!--more-->

## 证明

这完全是一个数学题，不过按照惯例，题解还是要写的。题目给出了一根长度为$L$的pocky，要求每次随机分割，取走前半部分，问平均多少次能够使长度小于等于$d$。

$$ 
\begin{align}
p_1 & =\frac{d}{L}	\\ 
p_2 & = \int_d^L \frac{d}{x} dx && = d \ln \frac{d}{L}	&\\
p_3 & = \int_d^L ( \int_d^x \frac{d}{y} dy )dx && = d \cdot \int_d^L \ln \frac{d}{x} dx && = 
\end{align}
$$

## 代码