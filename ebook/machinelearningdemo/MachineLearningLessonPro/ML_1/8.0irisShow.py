#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 16:11
# @Author  : Z
# @Email   : S
# @File    : 8.0irisShow.py
from sklearn.datasets import load_iris
iris=load_iris()
#打印iris的基础信息
# print(iris.keys()) #dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
# print(iris.data)
# [5.8 2.7 5.1 1.9]
# [6.8 3.2 5.9 2.3]
# [6.7 3.3 5.7 2.5]
# [6.7 3.  5.2 2.3]
# [6.3 2.5 5.  1.9]
# [6.5 3.  5.2 2.]
import numpy as np
# print(np.unique(iris.target))
# print(iris.target_names)#['setosa' 'versicolor' 'virginica']
# print(iris.DESCR)#
# print(iris.feature_names)#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# Data Set Characteristics:
#     :Number of Instances: 150 (50 in each of three classes)
#     :Number of Attributes: 4 numeric, predictive attributes and the class
#     :Attribute Information:
#         - sepal length in cm
#         - sepal width in cm
#         - petal length in cm
#         - petal width in cm
#         - class:
#                 - Iris-Setosa
#                 - Iris-Versicolour
#                 - Iris-Virginica
#     :Summary Statistics:
#选择特征和标签
X=iris.data
y=iris.target
#切分数据
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22,test_size=0.2)
#训练模型
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
#训练
dtc.fit(X_train,y_train)
print(dtc.feature_importances_)#[0.01672241 0.         0.59033215 0.39294544]
#预测
y_pred=dtc.predict_proba(X_test)
print(y_pred)
#验证
print("model in train set score is:",dtc.score(X_train,y_train))
print("model in test set score is:",dtc.score(X_test,y_test))
# model in train set score is: 1.0
# model in test set score is: 0.8666666666666667
#可视化
from sklearn.tree import export_graphviz
export_graphviz(dtc,out_file="iris.dot",filled=True,
                class_names=iris.target_names,
                feature_names=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],)