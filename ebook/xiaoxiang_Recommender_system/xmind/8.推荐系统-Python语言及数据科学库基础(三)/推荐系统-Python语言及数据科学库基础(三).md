# 机器学习语言必备-数据科学必备库

## 1.Pandas介绍

* Pandas是panel data面板数据，Pandas及处理结构化数据的利器，利用python数据以及数据结构完成对结构化数据的处理和分析功能。

## 2.Series数据结构详解

* Series=index：value
* 根据index完成value的值的打印
* 创建：可以根据list、tuple、dict、set等方式进行创建，指定index的值，查询的时候根据index查询value的值，删除和更新的操作也是使用index查询value的值。
* 属性：
  * shape、index、values、head、unique、size、dtype属性或函数

## 3.Pandas-DataFrame详解

* dataframe是数据框？
* 处理二维以上数据组织形式
* pd.DataFrame方式进行定义，指定row或列columns
* 增删改查部分操作
* iloc和loc方法(掌握)
  * iloc-index
  * loc直接根据i列名和行的名字进行打印

## 4.Pandas的对齐运算

* 对齐操作，对于多个值的求和或加减乘除问题的求解方法
* add(变量，fill_value)
* 对于Series和DataFrame均适用

## 5.Pandas的函数应用

* fillna
* dropna
* isnull
* drop(labels，axis-0 or1)
* pandas:sort_index

## 6.层次索引

* 指定多层索引
* 如何查询，df [外层索引][内层索引]
* 如何交换内外层索引：swaplevel
* 如何进行索引重排序：sortlevel

## 7.Pandas统计计算和描述

* describtion描述信息
  * count
  * min
  * max
  * std
  * var
* 统计计算一定需要按照行or列进行计算

## 8.Pandas读取文件（掌握）

* Pandas读取文件函数read_csv(file,sep="")
* 对数据采用基础属性信息查看
* ndim、shape、dtype、info()
* 数据处理---ix\iloc\loc\drop\。。。。。

## 9.Pandas函数补充(1)

* to_pickle（）转化为pickle文件
* cut对连续型数值离散化
* concat方法按照行或列进行合并
* to_numberic函数

## 10.Pandas函数补充(2)

* 聚合操作

* ```
  print(data.groupby(by=["one"])["two"].mean()) #等价写法
  print(data["two"].groupby(by=data["one"]).mean())
  ```

## 11.Pandas函数补充(3)

* 总结：
  * 总结Pandas的基本语法
  * 读取数据
  * 对数据尽心处理
  * 保存回到原理

## 12.Pandas函数补充(5)

## 13.Pandas数据处理案例一个简单的电影推荐系统

* 推荐系统之前数据预处理

## 14.Matplotlib&Seaborn数据可视化库

* Matplotlib是2D绘图库
* Seaborn是Maplotlib的上层的绘图库，只需要执行几行代码就可以执行
* import matplotlib.pyplot as plt
* plt.plot绘制直线图或折线图
* plt.show进行展示图形

## 15.Matplotlib入门案例

* 版本通过__version__进行输出
* 如果需要保存图片话，需要使用saveig直接给定名字绑定
* 如果想使用中文在标题上进行输出，需要指定u“标题内容”，fontproperties=“simhei”

## 16.figure对象及多图绘制

* 多图的绘制依赖于创建多个figure对象
* ax1=fig.add_subplot(111) #1行1列的第一个图形
* ax2=fig2.add_subplot(111) 
* add_subplot(222) #2行2列的第2个图形

## 17.figure对象子图创建

* figure对象通过使用add_subplot方法进行图像绘制
* plt.subplot（2，2,1）方法进行图像的绘制---plt.sca(ax1)

## 18.Matplotlib各种图形的绘制实战

* 散点图scatter
* 直方图hist
* 箱线图boxplot绘制
* 饼状图pie
* 折线图plot方式

## 19.Matplotlib网格Grid实战

* grid网格--设置网格的颜色，设置网格的线条类型，设置网格的线条宽度等

## 20.Matplotlib图例的用法 

* lenged用于指示图片的类型
* plt.legend或ax1.legend方式进行

## 21.Matplotlib颜色、标记、线型说明

* 通常在图片中会指定图的颜色color，标记marker，线条linestyle
* “r--"----red,--虚线---显式指定：color=red，linestyle=”--“
* 面向对象和面向过程区分
* plt.title()-----ax1.set_title（）

## 22.Matplotlib综合案例分析

* 面向对象和面向过程
* plt.title   ax1.set_title()
* plt.xlim  ax1.set_xlim()
* plt.legend ax1.legend()
* 绘制图像的时候一定要加上标题、x和y轴坐标、legend图例

## 23.Seaborn绘图实战(1)

* seaborn绘图
* import matplotlib.pyplot as plt
* import seaborn as sns
* sns.boxplot绘制图形，hue选项含义参考那个参数
* sns.relplot绘制图形
* sns.指定不同方法

## 24.Seaborn绘图实战(2)

* 通过seaborn获取绘图信息
* 解决泰坦尼克号的获救问题---女性较男性获救概率更高，头等仓位比其他仓位获救概率较高
* sns.catplot
* 只要指定x和y的数据就可以进行图形展示

## 25.Scipy了解

* Scipy是基于numpy之上可以实现科学计算、工程计算】图形图像处理、fft等形式
* 数学上定积分、求解多项式、导数等问题均可求解
* 重点详述了Scipy中的sparse矩阵中的svds矩阵分解
* 利用svds和eigs等进行矩阵分解，从而实现矩阵分解方式的推荐系统

##26.Sklearn了解

* 包含机器学习各种算法，目前集成了
  * 分类
  * 回归
  * 聚类
  * 降维
  * 特征工程
* 以线性回归的例子为例展开
  * 求解机器学习模型问题---机器学习参数的求解问题
  * 使用fit方法训练模型
  * 使用predict方法进行预测















