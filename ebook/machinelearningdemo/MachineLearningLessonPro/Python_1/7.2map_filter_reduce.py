#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 16:36
# @Author  : Z
# @Email   : S
# @File    : 7.2map_filter_reduce.py
#way1
print(list(map(str,range(3))))
#way2
def add1(X):
    return X+5
r1=list(map(add1,range(10)))
print(r1)
#way3
def add2(X,Y):
    return X+Y
r2=list(map(add2,range(5),range(5)))
print(r2)
#等同于
print(list(map(lambda x,y:x+y,range(5),range(5,10))))
#等同于
print([add2(x,y) for x,y in zip(range(5),range(5,10))])

#导入reduce函数
from functools import reduce
print(reduce(add2,range(5))) #1+...5
print(reduce(lambda x,y:x+y,range(5)))

#filter过滤函数
seq1=['foo','x41','?1','***']
def func(x):
    return x.isalnum()
filter(func,seq1) #返回filter对象
print(list(filter(func,seq1))) #将filter转化为列表
#使用列表推到式实现相同的功能
print([x for x in seq1 if x.isalnum()])