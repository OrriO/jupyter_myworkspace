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

plt.figure(figsize=(15,15))

plt.subplot(221)
plt.plot(X,y1,"r--",linewidth=2)
plt.title("Y=sin(x)")
plt.xlim(2,8)
plt.grid(color="b")
plt.legend(loc=0,labels=["Y=sin(x)"])


plt.subplot(222)
plt.plot(X,y2,"r-.",linewidth=5,label=["Y=sign(x)"])
plt.title("Y=SIGN(X)")
plt.xlim(-5,5)
plt.ylim(-2,2)
plt.legend(loc=0)



plt.subplot(212)
plt.plot(X,y3)
plt.xlabel("X")
plt.ylabel("Tahn(X)")
plt.grid()
plt.legend(loc=1,labels=["Y=tanh(X)"])

plt.show()