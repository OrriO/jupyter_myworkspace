#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:09
# @Author  : Z
# @Email   : S
# @File    : 14.6pltfigure.py
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(10,10))
#first
ax1=fig.add_subplot(221)
X=np.random.randn(100)
ax1.hist(X,bins=4)
#second
ax2=fig.add_subplot(222)
X1=np.linspace(-10,10,10)
Y=X1**2
ax2.plot(X1,Y)
#third
ax3=fig.add_subplot(223)
x=[0.2,0.4,0.2,0.2]
labels=["A","B","C","D"]
ax3.pie(x, explode=[0,0.4,0,0], labels=labels,shadow=True)
#箱线图--小提琴图----分位数
# ax4=fig.add_subplot(224)
# X3=np.random.randn(100)
# ax4.boxplot(X3,whis=0.5,sym="*")

#散点图
ax4=fig.add_subplot(224)
X1=np.linspace(-10,10,10)
Y=X1**2
ax4.scatter(X1,Y)
plt.show()