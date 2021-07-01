#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 8:58
# @Author  : Z
# @Email   : S
# @File    : 1.0Series.py
import pandas as pd
#使用pandas
#1.创建
s1=pd.Series([1,2,3,4],index=("a","b","c","d"))
s2=pd.Series({"a":1,"b":2,"c":3,"d":4})
print(s2)
print(":"*100)
print(s1)
print(type(s1))
#2.查询
print(s1["a"])
#3.更改
s1["a"]=100
print(s1)

#4.属性信息打印
print(s2.index) #Index(['a', 'b', 'c', 'd'], dtype='object')
print(s2.values) #[1 2 3 4]
print(s2.shape) #(4,)
print(s2.ndim) #1
print(s2.size) #4
print(s2.dtype) #int64
print(s2.head()) #前5行数据获取
s2.index.name="ok"
print(s2)
# ok
# a    1
# b    2
# c    3
# d    4
# dtype: int64
print(s2.index.name)
s2.name="hello"
# print(s2)
# ok
# a    1
# b    2
# c    3
# d    4
# Name: hello, dtype: int64

s3=pd.Series([-1,-2,3,-1,-4,3,0,0,1])
print(s3)
print(s3.unique()) #[-1 -2  3 -4  0  1]
