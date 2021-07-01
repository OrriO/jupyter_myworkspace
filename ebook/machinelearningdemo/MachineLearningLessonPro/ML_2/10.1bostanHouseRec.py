#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 12:04
# @Author  : Z
# @Email   : S
# @File    : 4.0bostanHouseRec.py
#读取数据
from sklearn.datasets import load_boston
bostan=load_boston()
print(bostan.keys())#dict_keys(['data', 'target', 'feature_names', 'DESCR'])
print(bostan.DESCR) #:Number of Instances: 506 -:Number of Attributes: 13 numeric/categorical predictive
print(bostan.data)
print(bostan.target)
print(bostan.feature_names)
# ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO'
 # 'B' 'LSTAT']
#数据处理
X=bostan.data
y=bostan.target
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22,test_size=0.2)
# print(X_train)
# print(y_train)
#模型建立
from sklearn.ensemble import GradientBoostingRegressor
lr=GradientBoostingRegressor()
lr.fit(X_train,y_train)
#模型预测
y_pred=lr.predict(X_test)
print(y_pred)
#模型校验
print("model in trains set score is:",lr.score(X_train,y_train))
print("model in tests set score is:",lr.score(X_test,y_test))
# model in trains set score is: 0.9782530327891484
# model in tests set score is: 0.8442713715157044
#mae\mse\r2
from  sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
print("mae:",mean_absolute_error(y_test,y_pred))
print("mse",mean_squared_error(y_test,y_pred))
# mae: 3.4240698961589606
# mse 20.765767538052017
print("r2",r2_score(y_test,y_pred)) #r2 0.7658020514461032