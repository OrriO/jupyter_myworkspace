#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 15:46
# @Author  : Z
# @Email   : S
# @File    : 17.1way1Figureplot.py
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(-10,10,100)
y1=np.sin(X)
y2=np.sign(X)
y3=np.tanh(X)
fig=plt.figure(figsize=(20,20))
ax1=fig.add_subplot(221)
ax1.plot(X,y1,"r--",linewidth=2)
ax1.set_title("Y=sin(x)")
ax1.set_xlim(2,8)
ax1.grid(color="b")
ax1.legend(loc=0,labels=["Y=sin(x)"])


ax2=fig.add_subplot(222)
ax2.plot(X,y2,"r-.",linewidth=5,label=["Y=sign(x)"])
ax2.set_title("Y=SIGN(X)")
ax2.set_xlim(-5,5)
ax2.set_ylim(-2,2)
ax2.legend(loc=0)



ax3=fig.add_subplot(212)
ax3.plot(X,y3)
ax3.set_xlabel("X")
ax3.set_ylabel("Tahn(X)")
ax3.grid()
ax3.legend(loc=1,labels=["Y=tanh(X)"])

plt.show()