#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:15
# @Author  : Z
# @Email   : S
# @File    : 20.arange.py
print(list(range(1,10,1)))
import numpy as np
r1=np.arange(10)
print(r1)
print(type(r1)) #<class 'numpy.ndarray'>
print(np.array(np.random.randn(3,3)))
#shape
r1.shape=2,5
print(r1)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
#reshape
r2=np.arange(10).reshape(5,2)
print(r2)
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]

zeros_int_arr = r2.astype(np.int32)
print(zeros_int_arr)
print(zeros_int_arr.dtype)  # int32