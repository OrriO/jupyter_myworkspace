#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

dic = {'name': ['a', 'b', 'b', 'b', 'b', 'b', 'c'], 'score_1': [1, -10, 11, 13, 13, 12, 6],
       'score_2': [1, -1, 2, -2, 21, 21, 7], 'score_3': [1, 1, 2, 22, 22, 21, 7]}
frame = pd.DataFrame(dic)

# df[
#             ((df['sent_cnt'] >= 30) & (df['ratio'] >= df['ratio_1'])) |
#             ((df['sent_cnt'] >= 10) & (df['sent_cnt'] < 30) & (
#                     df['ratio'] >= df['ratio_2']))
#             | ((df['sent_cnt'] < 10) & (df['ratio'] >= df['ratio_3']))]
print(type(frame))
print (frame)
# frame.loc[[frame['score_2'] < 0].index, ['score_2']] = 0

# frame.loc[frame['score_2']<0]['score_2']=0
# frame[frame['score_2'].values<0]['score_2']=0


frame.loc[frame['score_2'] < 0,'score_2']=0

tolist = frame.columns.values.tolist()

for i in tolist:
       frame.loc[frame[i] < 0, i] = 0
# data_frame = pd.DataFrame()
# data_frame.i
print(frame)

# print data1
# print data2



