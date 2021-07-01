#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
#
# a = pd.read_excel('D:\\workspace\\data_local_test\\data\\良医榜二期医生排班信息(1)(2)(1).xlsx')
# # 将groupby对象转换为dataframe
# # b=a.groupby(['医生名字','好大夫id'],as_index=False).first()
# # print(a)
# # b=a.duplicated(['医生名字','好大夫id'])
# # print(list(b['医生名字','好大夫id']))
# b=tuple(set(a['微医医生ID']))
# print(b)
# # #
# print(len(b))





z='a|b|a'
q,w,e= z.split('|')
print(q)
# print(w)
# print(type(float(e)))
print(q==e)
if q==e:
    print(1)

# print(a=a)

