# 机器学习语言必备-Python语言入门(一）

## 1.Python语言介绍& 为什么Python如此受欢迎？

* Python语言特点
  * Python：面向对象+解析性
  * Python解析器：4种
    * Cpython
    * Jpython
    * IronPython
    * PYPY
  * Python版本
    * Python2.x版本
    * Python3.x版本
    * 最大的区别就是print
  * Python的应用广、优点多、缺点：Python执行速度较慢---Julia语言
  * Python设计哲学---接近人类自然语言------Python胶水语言---------Python不要重复造轮子

## 2.Python基础环境及PyPi介绍

* Python基础环境安装---参考python官网：www.python.org
* python2和python3-直接下载exe或msi文件进行安装即可
* 安装完按成后使用python2和python3进行简单的代码编写-----python module/comand line
* Java---组织java代码的方式.java文件-----jar包-------maven仓库-----在线(maven install)和离线下载
* Python---组织python语言的方式.py文件----whl包-----------pypi(python package index)-------在线和离线下载
  * 在线安装pip install numpy
  * [numpy-1.15.4-cp27-cp27m-manylinux1_i686.whl ](https://files.pythonhosted.org/packages/8c/e1/9b86aaefeba4992331dd059cae71addad85be6d89b03dd4369ed8e1b05ca/numpy-1.15.4-cp27-cp27m-manylinux1_i686.whl)(10.2 MB)
  * numpy-1.15.4-----------cp27(python27)-------------manylinux(linux版本)----i686平台
  * 文件后缀whl轮子文件

## 3. Anaconda数据科学环境安装

* Anaconda分为Python2和Python3版本----平台版本
* 安装的时候直接下一步安装，需要注意的是将Anaconda环境变量配置到PATH中，并且注意位置
* Anaconda中很多的组件---注意：Anaconda是数据科学开发环境(集成了python环境+多个数据科学包)
* Anaconda Navigater--导航---打开jupyter、Spyder
* Anaconda Ipython----增强式的python
* Anaconda jupyter notebook-----提供web服务访问网站交互式的书写代码
* 学会使用jupyter书写代码----------公司工业场景+pycharm
* Spyder---IDE(集成开发环境)

## 4.Conda的主要操作

* conda命令---pip命令----均可完成python包的安装、卸载、更新等操作
* pip list   conda list
* pip install  xxx    conda install   xxx
* pip instal  -U xxxx   conda install -U xxx
* pip uninstall  xxx   conda uninsgall xxx
* Conda究竟和pip差别在哪里?
  * 在conda安装时候显示是使用pip显式安装
  * conda命令可以创建单独的python环境
    * conda create tensorflow python==2.7.0
    * 创建了一个名字叫做tensorflow的环境并且python版本是2.7.0
    * 该命令创建好之后是独立的沙箱环境

## 5.Pycharm+Anaconda环境整合

* 安装pycharm-------准备好了
* 通过pycharm整合Anaconda
* 通过setting的python-interpreter功能设置python解析器(全局设置)
* 通过python文件的右上角设置环境，进行局部设置
* 将python script进行设置---加入编码方式、名字、作者、时间、文件名

## 6.Python版本差异

* PYTHON的print差别
  * python2中-print是一个语句
  * python3中print是一个函数-()
* Python编码方式差别
  * python2中是ascii码
  * python3中是unicode码

## 7.python编码解码

* Python编码方式差别
  * python2中是ascii码
  * python3中是unicode码

## 8.python语言的数据类型

* Python的导入
  * import 操作
* 数值类型
  * 直接定义使用type查看类型
  * 同时id查看内存中的值，hash吃哈看hash值
  * +、-、*、/*、*
  * 单目运算符
  * 双目运算符
  * 其他操作
* 字符串、常量
  * 科学计数法
  * 引号--三引号进行原样输出，如何去掉，加\

## 9.python的输入

* python2和python3区别
  * python2中
    * raw_input--无论输入的是什么，输出一定是string类型
    * input---原样输入，如果是string类型务必加引号
  * python3中
    * input和raw_input是一致的，如果输入的是整形的数据，请务必进行强制类型转换

## 10.python输出语句

* print
  * 格式输出
  * 1.直接用逗号进行拼接
  * 2.直接用+进行拼接，需要注意的是数值类型需要转换为str类型
  * 3.用{}形式，.format结构
  * 4.用{0}-{1}...format()结构
  * 5.用%形式给定类型进一步输出

## 11.python随机数生成程序

* python自带的random
* python的numpy中的random模块产生的是矩阵的随机数

## 12.python的四种数据结构详解

* list列表：有序、异质、根据下标进行查询、更新、删除等操作
* tuple元祖:有序，异质，根据下标进行查询，但是更新和删除操作的话无法实现
* dict字典：无序、异质、根据key查询value，根据key更改value，根据key删除value
* set集合：集合的三要素

## 13.python的list详解

* list列表：有序、异质、根据下标进行查询、更新、删除等操作
* list中各个类型数据的转换
* list()工厂函数转换
* 切片操作----非常重要-----l1[start,stop,step]

## 14.zip和enumerate函数详解

* zip函数将各个不同组的元素进行组合
* enumerate函数能够完成枚举类型变量输出，对start的值进行调整

## 15.list函数实战

* list的函数---对list的基本操作
* 求长度、最大值、最小值、排序，删除、更改等操作

## 16.tuple操作

* 定义一个只有一个元素的tuple，一定要加逗号，或者通过type查看
* 在tuple中定义list可以直接更改list中各个元素的
* tuple中最重要的操作是切片---重点掌握

## 17.dict详解及函数操作

* dict字典
  * 创建方式
    * dict对象
    * { k:v}
  * 查询：根据key，但是key必须唯一，key必须是具备hash值的不可改变类型
  * 直接对key进行删除
* dict函数
  * 字典的增删改查、字典的各种函数的实现

## 18.set集合详解

* set-确定性、唯一性、无序性
* set的基本创建----{元素}
* set根据update\add\等方法进行更新和增加元素的值
* set作用就是对原有的数据加上set集合去重
* set运算----交并补集

## 19.列表推导式

* 推导式：求解满足条件的列表
* 列表推导式--本质上还是一个列表
* 语法：[表达式 for 变量 in 序列或迭代对象 if  条件]
  * 序列或迭代对象指的是list、tuple、dict、set
* 应用场景：
  * 使用列表推导式完成矩阵的转置、矩阵元素的平铺
  * 使用列表推导式完成不符合条件的元素的过滤等操作

## 20.几个补充函数理解

* map函数
  * 将函数作用于序列爽
* reduce函数
  * 将函数作用于序列上，直接做的是累计求和
* filter函数
  * 将函数作用于序列上，求解满足过滤条件的元素

## 21.元祖和字典推导式

* 元祖推导式----生成器推导式---求解满足条件的元祖---惰性求值----__next\__（）求解

* 字典推导式----求解满足条件的字典----{key:value for key,vaue in zip(xx,xxx)}

* 有序字典

  * ```python
    from collections import OrderDict
    dict=OrderDict（）
    dict["apple"]=1
    ```

## 22.扩展-Vscode+Anaconda

* 扩展
* vscode通过配置文件配置环境变量进行python开发

## 23.总结