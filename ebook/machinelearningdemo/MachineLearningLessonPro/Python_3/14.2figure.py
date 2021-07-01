#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 14:53
# @Author  : Z
# @Email   : S
# @File    : 14.2figure.py

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,20))
ax1=fig.add_subplot(212)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)
ax1.plot([1,2],[2,1])
ax2.plot([1,2],[2,1])
ax3.plot([1,2],[2,1])
ax4.plot([1,2],[2,1])
fig2=plt.figure(figsize=(10,20))
ax2=fig2.add_subplot(111)
ax2.plot([1,2],[2,1])
plt.show()
