#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:40
# @Author  : Z
# @Email   : S
# @File    : 23numpyCountCompute.py
# np.mean(), np.sum()：所有元素的平均值，所有元素的和，参数是 number 或 array
# 	np.max(), np.min()：所有元素的最大值，所有元素的最小值，参数是 number 或 array
# 	np.std(), np.var()：所有元素的标准差，所有元素的方差，参数是 number 或 array
# 	np.argmax(), np.argmin()：最大值的下标索引值，最小值的下标索引值，参数是 number 或 array
# 	np.cumsum(), np.cumprod()：返回一个一维数组，每个元素都是之前所有元素的 累加和 和 累乘积，参数是 number 或 array
# 	多维数组默认统计全部维度，axis参数可以按指定轴心统计，值为0则按列统计，值为1则按行统计。
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
print(np.sum(arr1,axis=0)) #列
print(np.sum(arr1,axis=1)) #行
print(np.mean(arr1))
print(np.max(arr1,axis=0))
print(np.max(arr1,axis=1))
print(np.std(arr1,axis=0))
print(np.var(arr1,axis=0))
print(np.argmax(arr1,axis=0))
print(np.argmax(arr1,axis=1))
print(np.cumsum(arr1,axis=0))
print(np.cumprod(arr1,axis=0))

arr2=np.array([1,2,1,2,1,2,-1,-2,-4])
print(np.unique(arr2,return_inverse=True))
a = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
print(a)
print(np.unique(a, axis=0))
print(np.unique(a, axis=1))
# array([[1, 0, 0], [2, 3, 4]])