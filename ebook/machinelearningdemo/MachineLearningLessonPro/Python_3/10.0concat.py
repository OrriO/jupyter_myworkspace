#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:42
# @Author  : Z
# @Email   : S
# @File    : 10.0concat.py
import pandas as pd
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
print(s1)
print(s2)
print(pd.concat([s1, s2],axis=0))
print(pd.concat([s1, s2],axis=1))

import numpy as np
df1 = pd.DataFrame([['a', 1], ['b', 2]],columns = ['letter', 'number'])
print(df1)
df2 = pd.DataFrame([['c', 3], ['d', 4]],columns = ['letter', 'number'])
print(df2)
print(pd.concat([df1, df2],ignore_index=True))
print(pd.concat([df1, df2],ignore_index=True,axis=1))
# print(np.vstack((df1,df2)))
# print(np.hstack((df1,df2)))