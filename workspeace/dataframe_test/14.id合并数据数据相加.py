#!/usr/bin/python
#-*- coding: utf-8 -*- 

import pandas as pd
import numpy as np

dic1 = {'name': ['a', 'a', 'a', 'a', 'b', 'b', 'b'],'id': ['B', 'B', 'B', 'C', 'C', 'D', 'E'],
        'score_2': [1, -1, 2, 4, 21, 23, 7], 'score_3': [1, 1, 2, 22, 22, 23, 7]}

frame1 = pd.DataFrame(dic1)
# print(frame1)
#
# agg = frame1.groupby(['name','id']).agg({'score_2': np.sum})
# print(agg)
# g = agg['score_2'].groupby(level=0, group_keys=False)
# apply = g.apply(lambda x: x.sort_values(ascending=False))
# print(apply)
# print(type(apply))
# apply=apply.to_frame()
# print(apply)
# # name__apply = apply.groupby(['name']).agg({'id':[','.join]})
# name__apply = apply.groupby(['name']).apply(lambda x : ','.join(x.id))
#
# print(name__apply)
#
# # apply1 = apply.groupby(['name','id']).apply(lambda x: x.head(1))
# apply1 = apply.groupby(['name']).head(1)
# print(apply1)
# # agg

# agg.to_csv('123.csv')
# apply = frame1.groupby(['name']).agg({'id':[','.join]})
# print(type(apply))
# print(apply)
l = list(frame1['name'])
print(l)
