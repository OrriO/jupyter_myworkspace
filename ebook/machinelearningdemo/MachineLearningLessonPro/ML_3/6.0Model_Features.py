# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 15:24
# @Author  : Z
# @Email   : S
# @File    : 3.2Features.py
import pandas as pd

talentData = pd.read_csv("./train.csv")

num_cols = ["Age", "MonthlyIncome", "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
            "TotalWorkingYears", "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion",
            "YearsWithCurrManager"]

cat_cols = ["Gender", "MaritalStatus", "OverTime"]

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
# 筛选出正负样本2
posdata = useData[useData["Attrition"] == 1].reindex()  # <class 'pandas.core.frame.DataFrame'>
negdata = useData[useData["Attrition"] == 0].reindex()  # <class 'pandas.core.frame.DataFrame'>
print("=" * 100)
print(type(posdata))
print(posdata)
print(type(negdata))
print(negdata)
# 对正负样本进行训练集和测试集的划分
train_pos_data = posdata.iloc[:int(len(posdata) * 0.8), :].copy()
test_pos_data = posdata.iloc[int(len(posdata) * 0.8):].copy()
train_neg_data = negdata.iloc[:int(len(negdata) * 0.8), :].copy()
test_neg_data = negdata.iloc[int(len(negdata) * 0.8):].copy()

# 利用pandas的concat函数
train_data = pd.concat([train_pos_data, train_neg_data])
test_data = pd.concat([test_pos_data, test_neg_data])
print(test_data.shape)  # (221, 25)

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
train_ord_cols = train_data[ord_cols].values
test_num_cols = test_data[num_cols].values
test_ord_cols = test_data[ord_cols].values
import numpy as  np

train_feats = np.hstack((train_num_cols, train_ord_cols, train_cat_feat))
train_target = train_data[target_cols].values
test_feats = np.hstack((test_num_cols, test_ord_cols, test_Cat_feat))
test_target = test_data[target_cols].values

# from collections import Counter
# print(sorted(Counter(train_target).items()))
from imblearn.over_sampling import SMOTE

ros = SMOTE(random_state=0)
train_feats, train_target = ros.fit_sample(train_feats, train_target)
# from collections import Counter
# print(sorted(Counter(y_resampled).items()))
print(train_feats.shape)
print(train_target.shape)
# (1474, 28)
# (1474,)

# 训练模型
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100)
rf.fit(train_feats, train_target)
y_pred = rf.predict(test_feats)
print("model in train set score is:", rf.score(train_feats, train_target))
print("model in test set score is:", rf.score(test_feats, test_target))
from sklearn.metrics import confusion_matrix

print(confusion_matrix(test_target, y_pred))
# model in train set score is: 0.9988623435722411
# model in test set score is: 0.8597285067873304
# [[181   4]
#  [ 27   9]]
from sklearn.metrics import classification_report, accuracy_score

print(classification_report(test_target, y_pred))
print("accuracy:", accuracy_score(test_target, y_pred))
# 逻辑斯特回归-LR
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_feats, train_target)
y_pred_lr = lr.predict(test_feats)
print("model in train set score is:", lr.score(train_feats, train_target))
print("model in test set score is:", lr.score(test_feats, test_target))
from sklearn.metrics import confusion_matrix

print(confusion_matrix(test_target, y_pred_lr))
# model in train set score is: 0.8816837315130831
# model in test set score is: 0.8461538461538461
# [[174  11]
#  [ 23  13]]
