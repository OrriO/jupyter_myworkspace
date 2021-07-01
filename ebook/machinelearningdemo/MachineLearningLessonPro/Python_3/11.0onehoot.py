#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:46
# @Author  : Z
# @Email   : S
# @File    : 11.0onehoot.py
#one-hot编码形式
import pandas as pd
s = pd.Series(list('abca'))
print(s)
# 0    a
# 1    b
# 2    c
# 3    a
pd.get_dummies(s)
#    a  b  c
# 0  1  0  0
# 1  0  1  0
# 2  0  0  1
# 3  1  0  0
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                    'C': [1, 2, 3]})
print(df)
#    A  B  C
# 0  a  b  1
# 1  b  a  2
# 2  a  c  3
print(pd.get_dummies(df, prefix=['col1', 'col2']))