#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:40
# @Author  : Z
# @Email   : S
# @File    : 9.0cut.py
import numpy as np
import pandas as pd
print(pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True))
# (0.19, 3.367],(3.367, 6.533], (6.533, 9.7]
# ([(0.191, 3.367], (0.191, 3.367], (0.191, 3.367], (3.367, 6.533],
#   (6.533, 9.7], (0.191, 3.367]]
# Categories (3, object): [(0.191, 3.367] < (3.367, 6.533] < (6.533, 9.7]],
# array([ 0.1905    ,  3.36666667,  6.53333333,  9.7       ]))
pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3,
           labels=["good","medium","bad"])
# [good, good, good, medium, bad, good]
# Categories (3, object): [good < medium < bad]
pd.cut(np.ones(5), 4, labels=False)
# array([1, 1, 1, 1, 1], dtype=int64)
print(pd.qcut(range(5), 3, labels=["good", "medium", "bad"]))

