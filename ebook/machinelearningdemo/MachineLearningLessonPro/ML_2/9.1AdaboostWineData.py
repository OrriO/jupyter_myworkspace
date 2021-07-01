#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 19:21
# @Author  : Z
# @Email   : S
# @File    : 9.1AdaboostWineData.py

import pandas as pd
df_wine=pd.read_csv("wine.data",sep=",")
df_wine.columns=["Class_label","Alcohol","Malic acid","Ash",
                 "Alcalinity of ash","Magnesium","Total phenols",
                 "Flavanoids","Nonflavanoid phenols","Proanthocyanins",
                 "Color intensity","Hue","OD280/OD315 of diluted wines","Proline "]
print(df_wine)
print(df_wine.info())
print(df_wine.shape)
print(df_wine.columns)
# (177, 14)
# Index(['Class_label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
#        'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols',
#        'Proanthocyanins', 'Color intensity', 'Hue',
#        'OD280/OD315 of diluted wines', 'Proline '],
#       dtype='object')
df_wine=df_wine[df_wine["Class_label"]!=1]

X=df_wine[["Alcohol","Hue"]].values
print(type(df_wine[["Alcohol","Hue"]])) #<class 'pandas.core.frame.DataFrame'>
print(type(X))
y=df_wine["Class_label"].values
print(type(y))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=22)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import  AdaBoostClassifier
tree=DecisionTreeClassifier()
ada=AdaBoostClassifier()

# tree.fit(X_train,y_train)
# y_train_pred=tree.predict(X_train)
# y_test_pred=tree.predict(X_test)

ada.fit(X_train,y_train)
y_train_pred=ada.predict(X_train)
y_test_pred=ada.predict(X_test)

from sklearn.metrics import  accuracy_score
train_train=accuracy_score(y_train,y_train_pred)
train_test=accuracy_score(y_test,y_test_pred)
print(train_train,train_test)