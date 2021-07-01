# 机器学习语言必备-Python语言入门(二)

## 1.函数详解

* 函数分为4中类型
  * 根据参数和返回值进行判断
    * 没有返回值没有参数
    * 有参数没有返回值
    * 没有返回值有参数
    * 有参数有返回值的
  * 全局变量和局部变量
    * global

## 2.函数详解-参数

* 参数
* 默认参数
  * 默认参数需要注意他的顺序
* 关键字参数
  * 关键字参数可以调换顺序，但是需要明确指明具体参数名字
* VarArgs参数
  * \* 表示的是tuple
  * \** 表示的是dict
* ​

## 3. 函数详解-Lambda函数

* lambda函数---匿名函数
* 语法：lambda 变量：表达式
* 平方：lambda x:x*x,可以在其中跟上默认参数，如果直接想输出的话直接使用括号进行输出即可
* lambda函数需要结合map函数使用，直接将lambda函数应用于可迭代对象或序列上
* 了解sort函数和lambda结合的形式

## 4.Python控制语句详解

* if_elif_else条件控制
  * 条件判断
* while循环
  * 在不确定次数的时候使用while循环
* for循环
  * 常用于迭代可迭代的对象，如列表。元祖等

## 5.Python文件读写详解

* Python的文件读写简单
  * open(file,mode="r") 读
    * 如何判断文件读到末尾？
      * 循环读取
      * 如果指定读取行的长度为0，结束
  * open(file,mode="w")写
    * f.writeline()

## 6.Python异常控制详解

* try-----except----finally
* 改写python的猜数字游戏

## 7.Python面向对象

* Python通过class关键字进行面向对象的设计
* 如何通过py文件导入python的类？
  * 使用from py文件 import 类名
  * 直接进行计算

## 8.Python-GUI程序设计

* tkinter包
* messagebox和askinteger包实现猜数字游戏
* 学会将猜数字游戏使用GUI实现

## 9.阶段小练习-HongBao程序实战

* 练习python的语法
* 设置两个参数---total---num
* 设置存放红包的数据结构---list数据结构
* 设置already就是将已经发放的金额进行保存
* 最后一个用户直接用total-already

## 10.Python实战-蒙特卡罗方法求解近似值

* Spark中实际案例演示
* 蒙特卡洛---近似值求解方法
* 以圆周率为求解目标：设定用圆的面积除以正方形面积*4近似计算圆周率，使用扔飞镖方式模拟求解面积，如果落入园内的飞镖数值/落入正方形内的飞镖数值*4近似求解PI的近似值。
* 使用python近似求解

## 11.Python实战-卷积的练习操作

* 卷积---实际上对图像进行操作
* 使用卷积核对原图像进行处理
* 通过移动卷积核分别对原图像进行先累乘在累加得到图像处理后的结果
* 说明：在工程方面求解卷积方面需要将卷积核进行翻转的，凡是在深度学习或图像处理领域通过不对卷积核进行饭庄，而是直接使用卷积核对原来的图形进行卷积，卷积之后的结果就是对图像处理的结果。

## 12.Numpy简介和创建随机数实例

* Numpy矩阵运算库

* ndarray---所有矩阵类的父类

* 底层C语言---速度快，数据科学基础的矩阵运算

* Scipy-基于Numpy基础上的数据科学运算库

* 如何创建随机数？

* ```python
  import numpy as np
  np.random.randn(5,5)
  ```

  使用随机数可以模拟数据

## 13.Numpy-array方式创建矩阵及矩阵属性详解

* ndarray父类实现矩阵的创建基本方式
* np.array方法创建多维度的矩阵
* np.array([[1,2,,3],[4,5,6]])
* shape属性--几行几列
* ndim属性---几维度
* size属性---多少元素
* dtype-----类型

## 14.Numpy-ndarray特殊矩阵创建

* 0矩阵
  * np.zeros()
* 1矩阵
  * np.ones()
* 对角阵
  * np.eye()
  * np.diag()

## 15.Numpy-arange方式创建矩阵及dtype数据类型简介

* arange创建方式类似于range对象
* arange如何形成矩阵
  * shape赋值维度
  * reshape调整维度
* astype
* dtype

## 16.Numpy的mat和matrix矩阵创建

* matrix必须是2维度矩阵
* mat是maitrix的别名，直接使用分号和引号将其分开

## 17.Numpy的等差和等比数列的创建

* numpy中等差
  * linspace
* numpy中等比
  * logspace
  * logspace换底

## 18.Numpy基础函数计算详解

* Numpy基础函数
  * ceil、floor、rint等
* Numpy统计函数
  * std、mean、var等
* Numpy的unique函数
  * sorted、unique

## 19.Numpy线性代数运算详解

* Numpy线性代数运算
  * 矩阵的乘法
  * 矩阵的转置
  * 矩阵的求逆
  * 矩阵的分解
    * 矩阵的QR分解
    * 矩阵的特征值分解
    * 矩阵的奇异值分解

## 20.总结