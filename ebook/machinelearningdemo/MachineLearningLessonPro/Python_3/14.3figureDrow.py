#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:01
# @Author  : Z
# @Email   : S
# @File    : 14.3figureDrow.py
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)
ax1.plot([1,2],[2,1])
ax2.plot([1,-2],[-2,1])
ax3.plot([-1,-2],[-2,-1])
ax4.plot([1,-2],[2,-1])

plt.show()
