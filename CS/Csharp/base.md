<!--
 * _______________#########_______________________ 
 * ______________############_____________________ 
 * ______________#############____________________ 
 * _____________##__###########___________________ 
 * ____________###__######_#####__________________ 
 * ____________###_#######___####_________________ 
 * ___________###__##########_####________________ 
 * __________####__###########_####_______________ 
 * ________#####___###########__#####_____________ 
 * _______######___###_########___#####___________ 
 * _______#####___###___########___######_________ 
 * ______######___###__###########___######_______ 
 * _____######___####_##############__######______ 
 * ____#######__#####################_#######_____ 
 * ____#######__##############################____ 
 * ___#######__######_#################_#######___ 
 * ___#######__######_######_#########___######___ 
 * ___#######____##__######___######_____######___ 
 * ___#######________######____#####_____#####____ 
 * ____######________#####_____#####_____####_____ 
 * _____#####________####______#####_____###______ 
 * ______#####______;###________###______#________ 
 * ________##_______####________####______________ 
 * 
 * @Author: 崩布猪
 * @Date: 2024-03-10 08:40:25
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-10 15:35:53
 * @FilePath: \CCCC\base.md
 * @Description: 
 * 概述 
 -->
 ### 终端命令
  - dotnet new console -o ./CsharpProjects/TestProject --生成控制台应用成熟
  - dotnet build -- 编译
  - dotnet run --运行

# why
C# 通常应用与windows桌面应用程序 web
# what
面向对象的 安全的 
# how

# 输出
Console.WriteLine()
## 数据类型
int
decimal
float
double
string
Toupper() Tolower() 全部大写 和全部小写方法 字符串
Trim() 删除空格方法
char
struct 

## 分支
if
if else
switch

## 循环
for
foreach
while
do while


## 数据类型转换
其他类型转换字符串
ToString()方法 
字符串转int
int.parse()
Convert 类 将String 转换为 int 适合小数数字转换成整数 其他时刻尽量用tryarse方法
Conver.ToInt32(); 这个方法有四舍五入

Tryparse()方法
- 他会尝试将字符串分析给成定的数字数据类型
- 如果成功，他会将转换后的值存储在 out 参数中
- 它将返回bool，只是操作成功还是失败

## 数组

数据类型【】 数组名
int[] a;
方法 

排序方法
Sort()
Reverse()

删除元素
clear(数组名字,start,end)

创建数组的其他方法
ToCharArry()
Solit()

使用Join() 创建传入char数组的新字符串，并将数组转换单个字符串

添加元素
Resize(ref 数组名, 6) 该方法也会删除 数目是后面的数字
数组名[4] = ...
数组名[5] = ...

## 格式化输出
  

### 对象 
- 创建 new
  - Random dice = new Random( ) or Random dice = new() 
- 重载方法 -- 原理对象输入不同的值 输出不同的东西
