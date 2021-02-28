---
title:CTS类型，枚举类型，控制语句
date:2018-02-03 18:01:20
tags:
---

# CTS类型，枚举类型，控制语句

> 由于已经~~(精通)~~学过了C++语言，所以会着重与C#与CPP的不同之处，不再从头整理。

<!--more-->

## 变量的定义
* 支持类型推断，使用`var`来定义变量；
* 变量在使用前必须初始化。

## CTS类型
由于C#并没有内置类型，所有的类型都内置于.NET Framework中，C#中的类型只是.NET类型(CTS类型)的示例。这一点和Haskell中的类型类比较相似。因此，我们可以实现以下操作:
```C#
string s = i.ToString();
```
CTS类型共有15种值类型，2中引用类型(string和object)。如下:

1.整型(8种)
 
|  名称 |    CTS类型    |   说明   |
|-------|--------------|----------|
| sbyte | System.SByte | 8位有符号 |
| short | System.Int16 | 16位有符号|
| int   | System.Int32 | 32位有符号|
| long  | System.Int64 | 64位有符号|
| byte  | System.Byte  | 8位无符号 |
| ushort| System.UInt16| 16位无符号|
| uint  | System.UInt32| 32位无符号|
| ulong | System.Uint64| 64位无符号|

一个整数默认为int类型，若要将其付给其他整个书类型，可以在后面加上'L'(long),'U'(uint),'UL'(ulong)。

2.浮点类型(2种)

|  名称  |    CTS类型     |   说明   |
|--------|---------------|----------|
| float  | System.Single | 32位单精度 |
| double | System.Double | 64位双精度|
3.decimal类型--高精度浮点类型

> CTS类型: System.Decinal

> 说明: 128位高精度

4.bool类型

> CTS类型: System.Boolean

5.字符类型

> CTS类型: System.Char

6.引用类型

|  名称  |    CTS类型     |      说明     |
|--------|---------------|---------------|
| string | System.String | Unicode字符串 |
| object | System.Object | 根类型，CTS中所有其他类型都有它派生|

## 控制语句

### switch
* 除非`case`后什么都不写，否则必须要写`break`语句。

### foreach
foreach循环可以迭代集合中的每一项。我们假定`Array`是一个整型数组，则可使用如下:
```C++
foreach (int temp in  Array)
{
	Console.WriteLine(temp);
}
```
注意，foreach不能改变集合中各项的值，即上面的`temp`不可更改。

## 枚举类型
> 虽然CPP也有枚举类型，但是我使(mei)用(yong)较(guo)少.

写法如下:
```C#
public enum TimeOfDay
{
	Morning = 0;
    Afternoon = 1;
    Evening = 2;
}
```
我们可以用形如`TimeOfDay.Morning`直接取出数值，然后和当前时间进行比较，从而判断时间。

在C#中，enum基于`System.Enum`基类，速度上没有损失，且支持一些已经写好的方法，如:
```C#
TimeOfDay time = TimeOfDay.Afternoon;
Console.WriteLine(time.ToString());
//按字符串输出

//从字符串中获取值
TimeOfDay time2 = (TimeOfDay) Enum.Parse(typeof(TimeOfDay),"afternoon",true);
Console.WriteLine((int)time2);
```