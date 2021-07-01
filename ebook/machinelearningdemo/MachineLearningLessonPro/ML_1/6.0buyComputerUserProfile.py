#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 15:30
# @Author  : Z
# @Email   : S
# @File    : 6.0buyComputerUserProfile.py
import pandas as pd
#1.导入数据、
buyData=pd.read_csv("buy.csv",sep=",")
print(buyData)
#     age  income  student  credit_rating  Class:buy_computer
# 0     1       3        0              1                   0
# 1     1       3        0              0                   0
# 2     2       3        0              1                   1
# 3     3       2        0              1                   1
# 4     3       1        1              1                   1
# 5     3       1        1              0                   0
# 6     2       1        1              0                   1
# 7     1       2        0              1                   0
# 8     1       1        1              1                   0
# 9     3       2        1              1                   1
# 10    1       2        1              0                   1
# 11    2       2        0              0                   1
# 12    2       3        1              1                   1
# 13    3       2        0              0                   0
print(buyData.shape)#(14, 5)
print(buyData.ndim) #2
# print(buyData.dtype)
print(buyData.info())
# RangeIndex: 14 entries, 0 to 13
# Data columns (total 5 columns):
# age                   14 non-null int64
# income                14 non-null int64
# student               14 non-null int64
# credit_rating         14 non-null int64
# Class:buy_computer    14 non-null int64
# dtypes: int64(5)
# memory usage: 640.0 bytes
print(buyData.head())
#    age  income  student  credit_rating  Class:buy_computer
# 0    1       3        0              1                   0
# 1    1       3        0              0                   0
# 2    2       3        0              1                   1
# 3    3       2        0              1                   1
# 4    3       1        1              1                   1
print(buyData.index) #RangeIndex(start=0, stop=14, step=1)
print(buyData.columns)
#Index(['age', 'income', 'student', 'credit_rating', 'Class:buy_computer'], dtype='object')
#2.数据处理
X=buyData.drop(labels="Class:buy_computer",axis=1)
y=buyData["Class:buy_computer"]
#3.特征工程
#数据集切分
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22,test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
#4.建立决策树模型
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion="entropy",max_depth=6,min_samples_leaf=2)#超参数
dtc.fit(X_train,y_train)
#5.模型预测
y_pred=dtc.predict(X_test)
print(y_pred) #[0 1 1]
#6.模型校验
print("model in trainset score is %.2f"%(dtc.score(X_train,y_train)))
print("model in trainset score is %.2f"%(dtc.score(X_test,y_test)))
# model in trainset score is 0.82
# model in trainset score is 0.67
from sklearn.metrics import confusion_matrix,classification_report
print("confusion matrix:",confusion_matrix(y_test,y_pred))
print("conputetion matrix:",classification_report(y_test,y_pred))
#7.保存模型
from sklearn.externals import joblib
joblib.dump(dtc,"buy.pkl")
#8.模型可视化
from sklearn.tree import export_graphviz
export_graphviz(dtc,out_file="buy.dot",feature_names=X.columns,class_names=["no","yes"],
                filled=True)