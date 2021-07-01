#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 11:46
# @Author  : Z
# @Email   : S
# @File    : 3.0carLinearRegression.py
import pandas as pd
cardata=pd.read_csv("./car.csv")
print(cardata)
#      Miles   Deliveries  Travel Time
# 0     100           4          9.3
# 1      50           3          4.8
# 2     100           4          8.9
# 3     100           2          6.5
# 4      50           2          4.2
# 5      80           2          6.2
# 6      75           3          7.4
# 7      65           4          6.0
# 8      90           3          7.6
# 9      90           2          6.1
X=cardata.drop(labels="Travel_Time",axis=1)
y=cardata.Travel_Time
print(X)
print(type(X)) #<class 'pandas.core.frame.DataFrame'>
print(type(y)) #<class 'pandas.core.series.Series'>
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22,test_size=0.2)
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)
print(lr.coef_) #[0.05909188,0.94214744]
print(lr.intercept_)  #-0.7296207264957264
#预测
y_pred=lr.predict(X_test)
print(y_pred)
#校验
print("model in trainset score is:",lr.score(X_train,y_train))
print("model in testset score is:",lr.score(X_test,y_test))
# model in trainset score is: 0.8537581648463358
# model in testset score is: 0.9922035806481854