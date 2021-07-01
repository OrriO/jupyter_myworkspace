# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 15:24
# @Author  : Z
# @Email   : S
# @File    : 3.2Features.py
import pandas as pd

talentData = pd.read_csv("./train.csv")

# 0.类别标签
# Attrition                   1100 non-null int64
# 1.数值型
# Age                         1100 non-null int64
# MonthlyIncome               1100 non-null int64
# NumCompaniesWorked          1100 non-null int64
# PercentSalaryHike           1100 non-null int64
# StandardHours               1100 non-null int64
# TotalWorkingYears           1100 non-null int64
# YearsAtCompany              1100 non-null int64
# YearsInCurrentRole          1100 non-null int64
# YearsSinceLastPromotion     1100 non-null int64
# YearsWithCurrManager        1100 non-null int64
num_cols = ["Age", "MonthlyIncome", "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
            "TotalWorkingYears", "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion",
            "YearsWithCurrManager"]
# 2.类别型
# BusinessTravel              1100 non-null object
# Department                  1100 non-null object
# EducationField              1100 non-null object
# Gender                      1100 non-null object
# JobRole                     1100 non-null object
# MaritalStatus               1100 non-null object
# Over18                      1100 non-null object
# OverTime                    1100 non-null object
# cat_cols=["BusinessTravel","Department","EducationField","Gender",
#           "JobRole","MaritalStatus","Over18","OverTime"]
cat_cols = ["Gender", "MaritalStatus", "OverTime"]
# 3.有序性
# DistanceFromHome            1100 non-null int64
# Education                   1100 non-null int64
# EnvironmentSatisfaction     1100 non-null int64
# JobInvolvement              1100 non-null int64
# JobLevel                    1100 non-null int64
# JobSatisfaction             1100 non-null int64
# PerformanceRating           1100 non-null int64
# RelationshipSatisfaction    1100 non-null int64
# StockOptionLevel            1100 non-null int64
# TrainingTimesLastYear       1100 non-null int64
# WorkLifeBalance             1100 non-null int64
ord_cols = ["DistanceFromHome", "Education", "EnvironmentSatisfaction",
            "JobInvolvement", "JobLevel", "JobSatisfaction", "PerformanceRating",
            "RelationshipSatisfaction", "StockOptionLevel", "TrainingTimesLastYear",
            "WorkLifeBalance"]
# 将三种数据类型进行组合
total_cols = num_cols + cat_cols + ord_cols
# 选择标签列
target_cols = ["Attrition"]
# 对已有的数据进行整合
useData = talentData[total_cols + target_cols]
print(type(useData))
print(useData.head())
print("有多少列作为特征：", len(total_cols))  # 24
# 筛选出正负样本1
# posdata=useData[useData["Attrition"]==1] #<class 'pandas.core.frame.DataFrame'>
# negdata=useData[useData["Attrition"]==0] #<class 'pandas.core.frame.DataFrame'>
# print("="*100)
# print(type(posdata))
# print(posdata)
# print(type(negdata))
# print(negdata)
# print("posdata and negdata sample is:%.2f%%"%(len(posdata)/len(negdata)*100))#posdata and negdata sample is:19.31%
# 筛选出正负样本2
posdata = useData[useData["Attrition"] == 1].reindex()  # <class 'pandas.core.frame.DataFrame'>
negdata = useData[useData["Attrition"] == 0].reindex()  # <class 'pandas.core.frame.DataFrame'>
print("=" * 100)
print(type(posdata))
print(posdata)
print(type(negdata))
print(negdata)
# 如何取出pandas处理的数据之后的values？
# posdata1=useData[useData["Attrition"]==1].values #<class 'pandas.core.frame.DataFrame'>
# print(posdata1)
# # [[34 6074 1 ... 3 3 1]
# #  [28 2596 1 ... 2 3 1]
# #  [24 1555 1 ... 2 3 1]
# #  ...
# #  [38 4855 4 ... 2 3 1]
# #  [22 2472 1 ... 2 3 1]
# #  [26 2042 6 ... 2 3 1]]
# 对正负样本进行训练集和测试集的划分
train_pos_data = posdata.iloc[:int(len(posdata) * 0.8), :].copy()
test_pos_data = posdata.iloc[int(len(posdata) * 0.8):].copy()
train_neg_data = negdata.iloc[:int(len(negdata) * 0.8), :].copy()
test_neg_data = negdata.iloc[int(len(negdata) * 0.8):].copy()
# len(train_pos_data) 142
# test_pos_data 36
# train_neg_data 737
# test_neg_data 185
# 利用pandas的concat函数
train_data = pd.concat([train_pos_data, train_neg_data])
test_data = pd.concat([test_pos_data, test_neg_data])
print(test_data.shape)  # (221, 25)
# print(len(train_data))
# print(len(test_data))
# print(len(train_pos_data)/len(train_neg_data))

# cat_cols = ["Gender", "MaritalStatus", "OverTime"]
# 目的：将类别型变形转化为数值性-onehot编码
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

Gender_le = LabelEncoder()
train_data["Gender_label"] = Gender_le.fit_transform(train_data["Gender"])
MaritalStatus_le = LabelEncoder()
train_data["MaritalStatus_label"] = MaritalStatus_le.fit_transform(train_data["MaritalStatus"])
OverTime_le = LabelEncoder()
train_data["OverTime_label"] = OverTime_le.fit_transform(train_data["OverTime"])
# print(Gender_le_label)
# print(MaritalStatus_le_label)
# print(OverTime_le_label)
# 对于测试集的lableencoder编码
test_data["Gender_label"] = Gender_le.transform(test_data["Gender"])
test_data["MaritalStatus_label"] = MaritalStatus_le.transform(test_data["MaritalStatus"])
test_data["OverTime_label"] = OverTime_le.transform(test_data["OverTime"])

print(test_data.shape)  # (221, 28)
# 简单聚合操作
print("Gender数据：")
print(train_data.groupby("Gender_label").size())
# Gender数据：
# Gender_label
# 0    363
# 1    516
print("MaritalStatus数据：")
print(train_data.groupby("MaritalStatus").size())
# MaritalStatus
# Divorced    184
# Married     414
# Single      281
print("OverTime数据：")
print(train_data.groupby("OverTime").size())
# OverTime
# No     636
# Yes    243
# dtype: int64

ohe = OneHotEncoder()
train_cat_feat = ohe.fit_transform(train_data[["Gender_label", "MaritalStatus_label", "OverTime_label"]]).toarray()
test_Cat_feat = ohe.transform(test_data[["Gender_label", "MaritalStatus_label", "OverTime_label"]]).toarray()
print(train_cat_feat[:5, :])
# [[0. 1. 0. 0. 1. 0. 1.]
#  [0. 1. 1. 0. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0.]
#  [1. 0. 0. 0. 1. 0. 1.]
#  [1. 0. 0. 1. 0. 0. 1.]]
# 整合所有的特征
train_num_cols = train_data[num_cols].values
print(type(train_num_cols))
print(train_num_cols)
# [[   34  6074     1 ...     7     0     6]
#  [   28  2596     1 ...     0     0     0]
#  [   24  1555     1 ...     0     0     0]
#  ...
#  [   37  8834     1 ...     5     7     7]
#  [   49 19161     3 ...     4     4     3]
#  [   38  2821     3 ...     2     2     2]]
train_ord_cols = train_data[ord_cols].values
test_num_cols = test_data[num_cols].values
test_ord_cols = test_data[ord_cols].values
import numpy as  np

train_feats = np.hstack((train_num_cols, train_ord_cols, train_cat_feat))
train_target = train_data[target_cols].values
test_feats = np.hstack((test_num_cols, test_ord_cols, test_Cat_feat))
test_target = test_data[target_cols].values
print(test_feats)
print(type(test_feats))
# [[1.900e+01 1.675e+03 1.000e+00 ... 1.000e+00 0.000e+00 1.000e+00]
#  [3.400e+01 5.304e+03 8.000e+00 ... 1.000e+00 0.000e+00 1.000e+00]
#  [2.900e+01 2.439e+03 1.000e+00 ... 1.000e+00 0.000e+00 1.000e+00]
#  ...
#  [3.500e+01 4.014e+03 3.000e+00 ... 0.000e+00 0.000e+00 1.000e+00]
#  [3.800e+01 5.405e+03 2.000e+00 ... 0.000e+00 0.000e+00 1.000e+00]
#  [3.700e+01 6.334e+03 4.000e+00 ... 0.000e+00 1.000e+00 0.000e+00]]
# 查看训练集和测试集的比例
print(len(test_feats))
print(test_feats.shape)
print(len(train_feats))
print(train_feats.shape)
# 221
# (221, 28)
# 879
# (879, 28)
