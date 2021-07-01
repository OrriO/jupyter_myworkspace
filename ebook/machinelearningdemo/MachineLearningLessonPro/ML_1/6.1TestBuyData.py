#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 15:51
# @Author  : Z
# @Email   : S
# @File    : 6.1TestBuyData.py
import pandas as pd
#1.导入数据、
buyData=pd.read_csv("buy.csv",sep=",")
#2.数据处理
X=buyData.drop(labels="Class:buy_computer",axis=1)
y=buyData["Class:buy_computer"]
#3.特征工程
#数据集切分
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22,test_size=0.2)
#7.读取模型
from sklearn.externals import joblib
dtc=joblib.load("buy.pkl")
#5.模型预测
print('---------------')
print(X_test.info())
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
