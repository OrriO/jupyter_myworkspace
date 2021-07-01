#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:08
# @Author  : Z
# @Email   : S
# @File    : 3.0SeriesDataframe.py
import  pandas as pd
s1=pd.Series(data=range(5),index=range(5))
s2=pd.Series(data=range(10),index=range(10))
print(s1+s2)
print(s1.add(s2,fill_value=100))
import numpy as np
df1=pd.DataFrame(data=np.ones((2,2)),columns=("a","b"))
df2=pd.DataFrame(data=np.ones((3,3)),columns=("a","b","c"))
print(df1+df2)
print(df1.add(df2,fill_value=100))