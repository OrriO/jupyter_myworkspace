import os
import pandas as pd
path = os.path.abspath('.')
print(path)
# pd.set_option('display.max_rows', 50)
# pd.set_option('display.max_columns', 40000)
# click_data = pd.read_csv('data/click_data1.csv')
# pre_data = pd.read_csv('data/pre_data1.csv')
# scene_order = pd.read_csv('data/scene_order.csv')
# all_order = pd.read_csv('data/all_order.csv')


# 清洗数据
# def clean_data(pre, act):
#     pre = pre[['user_id', 'doctor_id']]
#     act = act[['user_id', 'doctor_id']]
#     concat = pd.merge(left=act, right=pre, left_on='user_id', right_on='user_id', how='inner')
#     # print(concat)
#     print(concat.shape)
#     # concat = concat.dropna(axis=0, how='any')
#     # print(concat.shape)
#     le = len(concat)
#     print(le)
#     return concat, le

from xgboost import plot_importance

plot_importance()
from matplotlib import pyplot
pyplot.show()

import xgboost as xgb

booster = xgb.Booster()


# 校验数据,计算命中率
# def cal_acc(concat, le):
#     is_true = 0
#     num = 0
#     for num in range(1, 101, 1):
#         for index, row in concat.iterrows():
#             user_id, data1, data2 = row
#             if len(set(eval(data1)).intersection(set(eval(data2)[0:num]))):
#                 is_true += 1
#         print(is_true / le)
#         is_true = 0


# concat, le=clean_data(pre_data,click_data)
# cal_acc(concat, le)

# 分析高命中用户的特点
# def cal_acc_cnt(concat, le):
#     is_true = 0
#     num = 0
#     for index, row in concat.iterrows():
#         user_id, data1, data2 = row
#         if len(set(eval(data1)).intersection(set(eval(data2)))):
#             is_true += 1
#             print(user_id)
#     # print(is_true / le)
#     is_true = 0
#
#
# concat, le = clean_data(pre_data, click_data)
# cal_acc_cnt(concat, le)
# import pandas as pd
#
# df = pd.DataFrame([['a',1,41],['a',2,98],['a',3,53],['b',1,15],['b',2,64],['b',3,36]], columns=['code', 'date','count'])
#
# d = dict()
# for _, row in df.iterrows():
#     code, data, count = row
#     d.setdefault(code, {}).update({str(data): count})
#
# print d


# groupby = pre_data.groupby(by='user_id').apply(lambda x: x.sort_values('score', ascending=False))
# print(groupby)

# click_data = 'data/click_data1.csv'
# pre_data = 'data/pre_data1.csv'
#
# for line in open(click_data):
#     # print(line)
#     line_split = line.split(',')
#     print(line_split)
#     user_id,doctor_id,dirty_data=line_split
#     # print(user_id)
#     user_click_list[user_id].append(doctor_id)
# print(user_click_list)
