#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:21
# @Author  : Z
# @Email   : S
# @File    : 21.mat.py
import numpy as np
r1=np.matrix([1,2,3,4])
print(r1)
print(r1.ndim) #2
print(r1.shape) #(1, 4)
print(r1.size) #4
r2=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(r2)
print(r2.ndim) #2
print(r2.shape) #(3, 3)
print(r2.size) #9
# r2=np.matrix([[[1,2,3],[4,5,6],[7,8,9]]]) #ValueError: matrix must be 2-dimensional
r3=np.array([[[1,2,3],[4,5,6],[7,8,9]]]) #ValueError: matrix must be 2-dimensional
print(r3.shape) #(1, 3, 3)
print(r3.ndim) #3

#mat和matrix区别？
#mat是matrix的别名-----------
r3=np.mat([1,2,3,4])
print(r3)
r4=np.mat("1,2;4,5")
print(r4)
# [[1 2]
#  [4 5]]