# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 16:15
# @Author  : Z
# @Email   : S
# @File    : 7.1listDeriveApplication.py
# 1.使用列表推到式实现嵌套列表的平铺（两个for循环） #1, 2, 3,4, 5, 6,7, 8, 9
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(vec)
#使用列表表达式完成
print([num for elem in vec for num in elem]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
result=[] #[1, 2, 3, 4, 5, 6, 7, 8, 9]
for elem in vec:
    for num in elem:
        result.append(num)
print(result)
##2.过滤不符合条件的元素
aList=[1,2,3,4,0,-1,-2,-3]
r=[elem for elem in aList if elem >0]  #[1, 2, 3, 4]
print(r)
#等价于
result1=[]
for elem in aList:
    if elem>0:
        result1.append(elem)
print(result1)
##3.列表推导中使用多个循环实现多序列元素任意的组合，并过滤元素
r2=[(x,y) for x in range(10) for y in range(10) if x!=y]
print(r2)
#等价于
result2=[]
for x in range(10):
    for y in range(10):
        if x!=y:
            result2.append((x,y))
print(result2)
##4.实现列表推到式实现矩阵转置
vec=[[1,2,3],[4,5,6],[7,8,9]] #1,4,7
print(vec)
r3=[[row[i] for row in vec] for i in range(3)]
print(r3)
#zip函数
print(list(map(list,zip([1,2,3],[4,5,6],[7,8,9])))) #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

##5.使用列表推导生成100以内的所有素数
#素数--只能被1和本身整除的数，1肯定不是素数
r4=[p for p in range(2,101) if 0 not in [p%q for q in range(2,p)]]
print(r4)
import numpy as np
r5=[p for p in range(2,101) if 0 not in [p%q for q in range(2,int(np.sqrt(p))+1)]]
print(r5)
