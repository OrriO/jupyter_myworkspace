#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:24
# @Author  : Z
# @Email   : S
# @File    : 15.0plotScatter.py
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(111)
import numpy as np
x=np.linspace(1,10,50)
ax1.scatter(x,x**2)
ax1.grid(color="r",linestyle="--",linewidth=10)
plt.show()