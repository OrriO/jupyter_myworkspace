# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 14:46
# @Author  : Z
# @Email   : S
# @File    : 14.1MatplotlibDemo.py
import matplotlib as pl
# 1.打印Matplotlib版本
print(pl.__version__) #2.2.2
#2.绘制y=x+5和y=2x+5两条曲线
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,10,50)
y1=x+5
y2=2*x+5
plt.plot(x,y1)
plt.plot(x,y2)
plt.title(u"This is y=X 函数",fontproperties="SimHei")
plt.savefig("sen.jpg")
#显示
plt.show()