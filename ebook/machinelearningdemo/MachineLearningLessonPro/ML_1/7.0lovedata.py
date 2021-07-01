#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 15:57
# @Author  : Z
# @Email   : S
# @File    : 7.0lovedata.py
import pandas as pd
file=pd.read_csv("./SklearnTest.txt")
#数据处理--is_date=
new_Date=file.query("is_date==-1")
data=file.query("is_date!=-1")
# print(new_Date)
#    height  house  car  handsome  job  is_date
# 8    1.65      0    1       6.6    0       -1
# print(data)
#    height  house  car  handsome  job  is_date
# 0    1.80      1    0       6.5    2        1
# 1    1.62      1    0       5.5    0        1
# 2    1.71      0    1       8.5    1        1
# 3    1.58      1    1       6.3    1        1
# 4    1.68      0    1       5.1    0        0
# 5    1.63      1    0       5.3    1        0
# 6    1.78      0    0       4.5    0        0
# 7    1.64      0    0       7.8    2        0
#2.将data已经处理好的数据分为X和y
X=data.drop("is_date",axis=1)
y=data["is_date"]
#3.进行切分
from sklearn.model_selection import  train_test_split
#random_state=9随机数种子，如果指定随机数种子，保证每次切分的时候结果的可重复性
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=9)
#4.训练模型
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(X_train,y_train)
print(dtc.feature_importances_)
#5.预测
y_pred=dtc.predict(X_test)
print(y_test)
#6.校验
print("model in train set score is:",dtc.score(X_train,y_train))
print("model in test set score is:",dtc.score(X_test,y_test))
from sklearn.metrics import classification_report,confusion_matrix
print("classification_report score is:",classification_report(y_test,y_pred))
print("confusion_matrix score is:",confusion_matrix(y_test,y_pred))
#可视化
from sklearn.tree import export_graphviz
# export_graphviz(dtc,out_file="love.dot",feature_names=X.columns,filled=True,class_names=["no","yes"])
# y_pred.to_csv("result.txt",sep=",")
