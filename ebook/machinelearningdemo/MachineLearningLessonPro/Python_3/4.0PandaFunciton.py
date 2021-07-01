#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:14
# @Author  : Z
# @Email   : S
# @File    : 4.0PandaFunciton.py
import pandas as pd
import  numpy as np
print(np.random.randn(3))
df1=pd.DataFrame([np.random.randn(3),[np.nan,2,2],[1,np.nan,3]],
                 columns=("A","B","C"),index=("a","b","c"))
print(df1)
#isnull
print(df1.isnull())
#fillna
print(df1.fillna(100))
#dropna
print(df1.dropna(axis=0))
#          0         1         2
# 0 -0.85841 -0.647983 -1.414457
print(df1.dropna(axis=1))
#           2
# 0 -1.414457
# 1  2.000000
# 2  3.000000
# drop操作- Drop specified labels from rows or columns.
import pandas as pd
import  numpy as np
print(np.random.randn(3))
df1=pd.DataFrame([np.random.randn(3),[np.nan,2,2],[1,np.nan,3]],
                 columns=("A","B","C"),index=("a","b","c"))
print(df1.drop(["A"],axis=1))
# print(df1.drop([0]))
print(df1.drop(["a"]))