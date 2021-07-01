#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:35
# @Author  : Z
# @Email   : S
# @File    : 6.0PandasCountFunction.py
import pandas as pd
import numpy as np
df1=pd.DataFrame(np.random.randn(5,4),index=("a","b","c","d","e"),
                 columns=("A","B","C","D"))
print(df1)
# sum, mean, max, min… axis = 0
# 按列统计，axis = 1
# 按行统计
# skipna 排除缺失值， 默认为True
print(df1.sum(axis=1))
print(df1.sum(axis=0))
print(df1.mean(axis=1))
print(df1.mean(axis=0))
print(df1.max(axis=0))
#description
print(df1.describe())
#               A         B         C         D
# count  5.000000  5.000000  5.000000  5.000000  有几个样本
# mean  -0.196643  0.510580 -0.076933  0.144531  均值
# std    0.759045  0.882974  0.542685  1.179448  标准差
# min   -1.342553 -0.751580 -0.815040 -1.210786  最小值
# 25%   -0.460303  0.352631 -0.388602 -0.983421  1/4分位数
# 50%   -0.137811  0.460187  0.049356  0.623713  中位数
# 75%    0.422771  0.789292  0.168337  0.816850  3/4分位数
# max    0.534681  1.702369  0.601287  1.476297  最大值
print(df1)
print(df1.query("A>B"))

#
# count 非Nan数量
print(df1.count())
# describe 针对个列汇总统计
# min和max 最大最小值
# argmin、argmax 计算最大值或最小值对应的索引位置
# print(df1.argmin(axis=0))
# quantile 计算样本的分位数（0-1）
print(df1.quantile(0.65))
# mean 均值
print(df1.mean(axis=0))
# median 中位数
# mad 平均绝对离差
# var 样本方差
# std 样本的标准差
# skew 样本值的偏度----正态分布的偏度为0
# kurt 样本值的峰度------正态分布的峰度为3
# cumsum样本值的累计和
print(df1.cumsum())