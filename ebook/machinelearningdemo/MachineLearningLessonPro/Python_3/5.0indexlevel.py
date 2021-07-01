#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:27
# @Author  : Z
# @Email   : S
# @File    : 5.0indexlevel.py
import  pandas as pd
import numpy as np
s1=pd.Series(np.random.randn(12),
          index=[["a","a","a","b","b","b","c","c","c","d","d","d"],
                 [1,2,3,1,2,3,1,2,3,1,2,3]])
print(s1)
print(s1["a"][1])
s1["a"][1]=100
print(s1)
#两个index的互换
print(s1.swaplevel())
print(s1.swaplevel().sortlevel())

