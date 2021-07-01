#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:50
# @Author  : Z
# @Email   : S
# @File    : 12.to_numberic.py
import pandas as pd
s = pd.Series(['1.0', '2', -3])
print(pd.to_numeric(s))
s = pd.Series(['apple', '1.0', '2', -3])
# print(pd.to_numeric(s))
print(pd.to_numeric(s, errors='ignore'))
print(pd.to_numeric(s, errors='coerce'))