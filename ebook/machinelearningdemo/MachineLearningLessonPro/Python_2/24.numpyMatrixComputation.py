#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 11:18
# @Author  : Z
# @Email   : S
# @File    : 24.numpyMatrixComputation.py
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
#矩阵乘法
#way1
print(np.dot(arr1,arr1))
#way2
print(arr1.dot(arr1))
#矩阵的转置
print(arr1.T)
print(arr1.T.dot(arr1))
#矩阵的行列式
from numpy.linalg import det
print("行列式",det(arr1))
arr2=np.array([[1,2],[2,4]])
print(det(arr2)) #0.0
#矩阵求逆---伴随矩阵/行列式----行列式为0的话，整个求逆的结果不存在
from numpy.linalg import inv
print(inv(arr1))
# print(inv(arr2))#numpy.linalg.linalg.LinAlgError: Singular matrix
#矩阵的分解-QR分解
from numpy.linalg import  qr
Q,R=qr(arr1)
print(Q)
print(R)
#验证乘积的结果
print(Q.dot(R))
#矩阵的分解-特征值分解
from numpy.linalg import eig
value,vector=eig(arr1)
print(value)
#[ 1.61168440e+01 -1.11684397e+00 -9.75918483e-16]
print(vector)
# [[-0.23197069 -0.78583024  0.40824829]
#  [-0.52532209 -0.08675134 -0.81649658]
#  [-0.8186735   0.61232756  0.40824829]]
#如何将特征值和特征向量转化为原来的矩阵
#A=Vector*value*inv(Vector)
print(vector.dot(np.dot(np.diag(value),inv(vector))))
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
#矩阵的分解-奇异值分解
from numpy.linalg import svd
U,Sigma,VT=svd(arr1)
print(U)
print(Sigma)#[1.68481034e+01 1.06836951e+00 3.33475287e-16]
print(VT)
#是否正交
print(U.dot(inv(U)))
print(VT.dot(inv(VT)))
# print(9999999999999999999999*99999999999999999999999999999)
#转换回去
print(np.dot(U,np.dot(np.diag(Sigma),VT)))
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print(np.allclose(np.dot(U,np.dot(np.diag(Sigma),VT)),arr1))