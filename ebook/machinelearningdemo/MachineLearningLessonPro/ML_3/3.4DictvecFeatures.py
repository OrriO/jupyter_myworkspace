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
# print("train_pos_data",type(train_pos_data))#train_pos_data <class 'pandas.core.frame.DataFrame'>
print("train_pos_data", len(train_pos_data))
test_pos_data = posdata.iloc[int(len(posdata) * 0.8):].copy()
print("test_pos_data", len(test_pos_data))
train_neg_data = negdata.iloc[:int(len(negdata) * 0.8), :].copy()
print("train_neg_data", len(train_neg_data))
test_neg_data = negdata.iloc[int(len(negdata) * 0.8):].copy()
print("test_neg_data", len(test_neg_data))
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
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)
train_data_dv = dv.fit_transform(train_data.to_dict(orient="records"))
# AttributeError: 'str' object has no attribute 'items'
test_data_dv = dv.transform(test_data.to_dict(orient="records"))
print(test_data_dv)
# test_data_dv=pd.DataFrame(test_data_dv,columns=)
# test_data_dv.to_csv("tesedemo.csv",sep=",")
print(dv.feature_names_)
