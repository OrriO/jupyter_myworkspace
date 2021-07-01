#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 20)

dic1 = {'score_1': [1, -10, 11, 13, 13, 12, 6], 'name': ['a', 'c', 'd', 'e', 'f', 'g', 'h'],
        'score_2': [1, -1, 2, -2, 21, 21, 7], 'score_3': [1, 1, 2, 22, 22, 21, 7]}
dic2 = {'name': ['b', 'a', 'd', 'e', 'f', 'g'], 'score_1': [1, -10, 11, 13, 13, 12],
        'score_2': [1, -1, 2, -2, 21, 21], 'score_3': [1, 1, 2, 22, 22, 21]}
frame1 = pd.DataFrame(dic1)
frame2 = pd.DataFrame(dic2)

# print (frame1)
# print(frame1)
# concat = pd.merge(left=frame1, right=frame2,left_on='name',right_on='name',how='outer')
# print (concat)

concat = frame1.append(frame1,ignore_index=True)
# print (concat)
concat = concat.drop(columns=['score_1'])
# print (concat)



i='huhuu'
print('-----'+i+'--------')

# tolist = frame1['name'].tolist()


# print tolist

# if frame1['name'].isin(['a','c']):
#        frame1['score_4']=100
# # elif frame1['name'] in ('g','h'):
# #        frame1['score_4']=200
#
# print frame1

# def func(a, b, c):
#     if a in b:
#         return c
#     else:
#         return 0

# dic1 = {'score_1': [1, -10, 11, 13, 13, 12, 6], 'name': ['a', 'c', 'd', 'e', 'f', 'g', 'h'],
#         'score_2': [1, -1, 2, -2, 21, 21, 7], 'score_3': [1, 1, 2, 22, 22, 21, 7]}
#
# frame1 = pd.DataFrame(dic1)
#
# bbb = ('a', 'b','c','d')
# ccc=('a','c','e','g')
# ll = lambda x:100 if x in bbb else 200 if x in ccc else 0
# frame1['score_4'] = frame1['name'].apply(ll)
#
# print frame1
#
# frame1['max_score'] = frame1[['score_1', 'score_2', 'score_3']].max()
# print frame1
#
# # frame_ = str[frame1]
# # print frame_
# # print type(frame_)

