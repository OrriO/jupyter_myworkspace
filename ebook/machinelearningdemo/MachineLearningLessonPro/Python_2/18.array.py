#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:00
# @Author  : Z
# @Email   : S
# @File    : 18.array.py
import numpy as np
r1=[[1,2,3],[4,5,6],[7,8,9]]
print(type(r1))#<class 'list'>
#矩阵得array定义
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="float32") #<class 'numpy.ndarray'>
print(type(arr1))
print(arr1)
#矩阵的性质
print("shape",arr1.shape) #shape (3, 3)
print("ndim",arr1.ndim)#向量-1维度  矩阵-2维度  数组-3维度
print("dtype:",arr1.dtype)
print("dtype:",arr1.size)
#其他数据类型的转换
print(np.array((1,2,3,4)))
print(np.array({1,2,3,4}))
print(np.array({1:"apple",2:"banana"}))
# [1 2 3 4]
# {1, 2, 3, 4}
# {1: 'apple', 2: 'banana'}