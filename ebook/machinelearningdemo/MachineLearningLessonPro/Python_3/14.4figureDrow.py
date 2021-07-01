#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:01
# @Author  : Z
# @Email   : S
# @File    : 14.3figureDrow.py
import matplotlib.pyplot as plt
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)

ax1.plot([1,2],[2,1])
ax2.plot([1,-2],[-2,1])
ax3.plot([-1,-2],[-2,-1])
ax4.plot([1,-2],[2,-1])

plt.show()
