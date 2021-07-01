#-*- coding: utf-8 -*-
# @Time    : 2018/12/9 14:43
# @Author  : Z
# @Email   : S
# @File    : 3.0DataInformation.py
import pandas as pd
import os
#1.导入数据文件
datapath=os.path.join(".","train.csv")
talentData=pd.read_csv(datapath,sep=",")
#2.数据基础信息描述
print(talentData.shape) #(1100, 31)
print(talentData.ndim)  #2
print(talentData.head())
print(talentData.info())
# Attrition                   1100 non-null int64
# Age                         1100 non-null int64
# DistanceFromHome            1100 non-null int64
# Education                   1100 non-null int64
# EmployeeNumber              1100 non-null int64
# EnvironmentSatisfaction     1100 non-null int64
# JobInvolvement              1100 non-null int64
# JobLevel                    1100 non-null int64
# JobSatisfaction             1100 non-null int64
# MonthlyIncome               1100 non-null int64
# NumCompaniesWorked          1100 non-null int64
# PercentSalaryHike           1100 non-null int64
# PerformanceRating           1100 non-null int64
# RelationshipSatisfaction    1100 non-null int64
# StandardHours               1100 non-null int64
# StockOptionLevel            1100 non-null int64
# TotalWorkingYears           1100 non-null int64
# TrainingTimesLastYear       1100 non-null int64
# WorkLifeBalance             1100 non-null int64
# YearsAtCompany              1100 non-null int64
# YearsInCurrentRole          1100 non-null int64
# YearsSinceLastPromotion     1100 non-null int64
# YearsWithCurrManager        1100 non-null int64
# BusinessTravel              1100 non-null object
# Department                  1100 non-null object
# EducationField              1100 non-null object
# Gender                      1100 non-null object
# JobRole                     1100 non-null object
# MaritalStatus               1100 non-null object
# Over18                      1100 non-null object
# OverTime                    1100 non-null object
# dtypes: int64(23), object(8)
print(talentData.columns)
# Index(['Attrition', 'Age', 'BusinessTravel', 'Department', 'DistanceFromHome',
#        'Education', 'EducationField', 'EmployeeNumber',
#        'EnvironmentSatisfaction', 'Gender', 'JobInvolvement', 'JobLevel',
#        'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
#        'NumCompaniesWorked', 'Over18', 'OverTime', 'PercentSalaryHike',
#        'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
#        'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
#        'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
#        'YearsSinceLastPromotion', 'YearsWithCurrManager'],
#       dtype='object')