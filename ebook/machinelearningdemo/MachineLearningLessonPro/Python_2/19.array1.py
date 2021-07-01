#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:09
# @Author  : Z
# @Email   : S
# @File    : 19.array1.py
import numpy as np
r1=np.zeros(shape=(3,3))
print(r1)
r2=np.ones(shape=(3,3))
print(r2)
r3=np.diag([1,2,3,4])
print(r3)
np.eye(2, dtype=int)
A = np.diag([1.0, 2, 3])
print(A)
# array([[1., 0., 0.],
#        [0., 2., 0.],
#        [0., 0., 3.]])
print(np.flipud(A))
# array([[0., 0., 3.],
#        [0., 2., 0.],
#        [1., 0., 0.]])

A = np.diag([1., 2., 3.])
print(A)
# array([[1., 0., 0.],
#        [0., 2., 0.],
#        [0., 0., 3.]])
print(np.fliplr(A))
# array([[0., 0., 1.],
#        [0., 2., 0.],
#        [3., 0., 0.]])