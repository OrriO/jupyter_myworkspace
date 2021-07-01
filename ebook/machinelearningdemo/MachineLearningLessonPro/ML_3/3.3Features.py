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
useData = talentData[total_cols]  # X
useDataLabel = talentData[target_cols]  # Y
print(useData.shape)  # (1100, 25)
print(useData.info())  ##<class 'pandas.core.frame.DataFrame'>
print(useDataLabel.shape)  # (1100, 25)
print(useDataLabel.info())  ##<class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1100 entries, 0 to 1099
# Attrition    1100 non-null int64
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(useData, useDataLabel, test_size=0.2, random_state=22)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
# (880, 24)
# (220, 24)
# (880, 1)
# (220, 1)
