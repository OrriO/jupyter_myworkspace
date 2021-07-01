#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:54
# @Author  : Z
# @Email   : S
# @File    : 13.groupby.py
# data.groupby(func, axis=0).mean()
# data.groupby(['col1', 'col2'])['col3'].mean()
import pandas as pd
data=pd.DataFrame([[1,2,3],[1,3,3],[4,5,6],[4,3,6]],columns=["one","two","three"])
#    one  two  three
# 0    1    2      3
# 0    1    3      3
# 1    4    5      6
# 1    4    3      6
print(data)
print("="*100)
print(data.groupby(by=["one"])["two","three"])
print(data.groupby(by=["one"])["two"])
print("="*100)
print(data.groupby(by=["one"])["two"].mean())
# one
# 1    2.5
# 4    4.0
#等价写法
print(data["two"].groupby(by=data["one"]).mean())
# print(data.groupby(['one', 'two']).mean())
# one
# 1    2.5
# 4    4.0
# Name: two, dtype: float64
# one
# 1    2.5
# 4    4.0
# Name: two, dtype: float64
print("==-=="*100)
import numpy as np
#根据one列进行聚合，在对其余列进行求解均值
print(data.groupby(['one']).mean())
print("=="*100)
#根据one列进行聚合，在对其余列进行求解均值
print(data.groupby(["one"]).transform(lambda x:np.mean(x)))
print(data.groupby(["one"]).transform(lambda x:(x-np.mean(x))/(np.std(x))))
print("=="*100)
#根据one列进行聚合，在对指定列进行求解均值，如”two“
print(data.groupby(["one"]).apply(lambda data:np.mean(data["two"])))

print("="*100)
df = pd.DataFrame(np.random.randn(3, 3),columns=["a","b","c"],dtype="int32")
# >>> df
#     0         1          2
# 0  -0.029638  1.081563   1.280300
# 1   0.647747  0.831136  -1.549481
# 2   0.513416 -0.884417   0.195343
# df = df.applymap(lambda x: '%.2f' % x)
# print(df)
# df1 = df.applymap(lambda x:x.max())
# print(df1)
print("****************************")
# df
#     0         1          2
# 0  -0.03      1.08       1.28
# 1   0.65      0.83      -1.55
# 2   0.51     -0.88       0.20

# df2=df.drop(["a"],axis=1)
df2=df.drop("a",axis=1)
print(df2)
print("****************************")
df3=pd.DataFrame(np.random.randn(3, 3),columns=["a","b","c"],index=["one","two","three"])
print(df3)
df4=df3.reindex(["three","two","one"])
print(df4)
#
# df4.select("two")