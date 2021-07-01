#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:34
# @Author  : Z
# @Email   : S
# @File    : 22.numpyFunction.py
import  numpy as np

randn = np.random.randn(3, 3)
print(randn)
# 1.元素计算函数
# np.ceil(): 向上最接近的整数，参数是 number 或 array
print(np.ceil(randn))
# np.floor(): 向下最接近的整数，参数是 number 或 array
print(np.floor(randn))
# np.rint(): 四舍五入，参数是 number 或 array
print(np.rint(randn))
# np.isnan(): 判断元素是否为 NaN(Not a Number)，参数是 number 或 array
print(np.isnan(randn))
# np.multiply(): 元素相乘，参数是 number 或 array
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,2],[3,4]])
print(np.multiply(arr1,arr2))
# np.divide(): 元素相除，参数是 number 或 array
print(np.divide(arr1,arr2))
# np.abs()：元素的绝对值，参数是 number 或 array
print(np.abs(randn))
# np.where(condition, x, y): 三元运算符，x if condition else y
print(np.where(arr1>0,1,-1))