#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

dic = {'name': ['a', 'a', 'b', 'b', 'b', 'b', 'b', 'c'], 'score_1': [1, -2, 10, 11, 13, -13, 12, 6],
       'score_2': [1, 3, 1, 2, 20, 21, 21, 7], 'score_3': [1, 0, -1, 2, 22, -22, 21, 7]}
frame = pd.DataFrame(dic)

frame.describe()
frame.drop_duplicates()

print (frame)
#
# col_lst = frame.columns.values.tolist()
# for val in col_lst:
#     frame.ix[frame[val] < 0, val] = 0
# print (frame)
#
#
#
# fill_dict = {'patient_cnt': 0, 'avg_reply_time': 0, 'praise_rate': 0, 'like_cnt': 0,
#                      'registration_reputation_rate': 0,
#                      'patient_apply_cnt': 0, 'total_pv': 0}
#
# keys = fill_dict.keys()
# print keys

