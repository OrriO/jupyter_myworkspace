#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:30
# @Author  : Z
# @Email   : S
# @File    : 16.0legend.py
import matplotlib.pyplot as plt
fig=plt.figure()
# ax1=fig.add_subplot(211)
# ax2=fig.add_subplot(212)
ax1=fig.add_subplot(111)
import numpy as np
x=np.linspace(1,10,50)
ax1.scatter(x,x**2)
ax1.scatter(x,x**3)
# ax1.legend(loc=0)
ax1.legend(labels=["y=x**2","y=x**3"],loc="best",ncol=2)
plt.show()