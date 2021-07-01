#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 9:17
# @Author  : Z
# @Email   : S
# @File    : 2.0Dataframe.py
import pandas as pd
df1=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=("a","b","c"),columns=("A","B","C"))
print(df1)
import  numpy as np
df2=pd.DataFrame(np.random.randn(4,4),index=("a","b","c","d"),columns=("A","B","C","D"))
print(df2)
#属性信息
print(df1.shape)
print(df1.head(1))
print(df1.ndim)
print(df1.info())
print(df1.columns) #Index(['A', 'B', 'C'], dtype='object')
print(df1.index) #Index(['a', 'b', 'c'], dtype='object')
# <class 'pandas.core.frame.DataFrame'>
# Index: 3 entries, a to c
# Data columns (total 3 columns):
# A    3 non-null int64
# B    3 non-null int64
# C    3 non-null int64
# dtypes: int64(3)
# memory usage: 96.0+ bytes
#查询
# print(df1["a"])
print(df1["A"]) #通过[]指定对应的列信息
print("::"*100)
print(df1.A)
print("::"*100)
print(df1.ix["a","A"])
print(df1.ix[:,"A"])
print(df1.ix["a",:])
print(df1.ix[:,:])
print("::"*100)
print(df1.loc[:,"A"])
print(df1.loc["a",:])
print(df1.loc[:,:])
print("::"*100)
print(df1.iloc[0,0])
print(df1.iloc[:,0])
print(df1.iloc[0,:])
print("+"*100)
print(df1.iloc[0:2])
#    A  B  C
# a  1  2  3
# b  4  5  6
print(df1.iloc[0:2,0:2])
print(df1.loc["a":"c"])
print(df1.loc["a":"b"])
print(df1.loc["a":"b","A":"B"])
print(df1.loc[:, lambda df: ['A', 'B']])
print("+"*100)
#更改
df1.ix["a","A"]=100
print(df1)
#删除操作
del df1["A"]
print(df1)
#增加一列
df1["D"]=[1,2,3]
print(df1)

