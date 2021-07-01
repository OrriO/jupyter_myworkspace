#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:01
# @Author  : Z
# @Email   : S
# @File    : 14.3figureDrow.py
import matplotlib.pyplot as plt
ax1=plt.subplot(221)
plt.sca(ax1)
plt.plot([1,2],[2,1])

ax2=plt.subplot(222)
plt.sca(ax2)
plt.plot([1,-2],[-2,1])


ax3=plt.subplot(223)
plt.sca(ax3)
plt.plot([-1,-2],[-2,-1])

ax4=plt.subplot(224)
plt.sca(ax4)
plt.plot([1,-2],[2,-1])


plt.show()
