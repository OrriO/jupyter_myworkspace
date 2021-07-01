#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 16:16
# @Author  : Z
# @Email   : S
# @File    : 20.scipy.py
from scipy import signal,misc
import numpy as np
import matplotlib.pyplot as plt
image=misc.ascent() #二维图像，公寓图像
w=np.zeros((50,50))
w[0][0]=1.0 #修改参数调整滤波器
w[49][25]=1.0 #可以根据需要调整
image_new=signal.fftconvolve(image,w) #使用FFT算法进行卷积

plt.figure()
plt.imshow(image_new) #显示滤波后的图像
plt.gray()
plt.title("Filteres image!")
plt.show()