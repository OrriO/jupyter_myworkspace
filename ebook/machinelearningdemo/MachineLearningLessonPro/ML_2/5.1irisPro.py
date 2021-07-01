#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 9:21
# @Author  : Z
# @Email   : S
# @File    : 1.0irisPro.py
#1.进行数据的读入---导入数据
from sklearn.datasets import load_iris
iris=load_iris()
#2.对数据进行简单的统计分析和图形化的展示
print(iris.keys())#['data', 'target', 'target_names', 'DESCR', 'feature_names']
print("iris data:",iris.data)
print("iris data:",type(iris.data))#iris data: <class 'numpy.ndarray'>
print("iris target:",iris.target)
print("iris targetname:",iris.target_names)
print("iris DESCR:",iris.DESCR)
print("iris  features_names:",iris.feature_names)
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# import  pandas as pd
# df=pd.DataFrame(iris)
# print(df)
#2.1绘制图形
import seaborn  as sns
import matplotlib.pyplot as plt
# sns.pairplot(iris, hue="sepal length (cm)")
# plt.show()
#3.确定特征和标签-X和y
X=iris.data
y=iris.target

#4.1降维---pca
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
X=pca.fit_transform(X)#Fit the model with X.
print(":"*1000)
print(X)
print(":"*1000)
# print(pca.explained_variance_)#[0.24301994 0.03386828 0.01034326 0.00170887]


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=22)
#4.特征处理-特征工程
from sklearn.preprocessing import StandardScaler,MinMaxScaler
sc=MinMaxScaler() #feature_range : tuple (min, max), default=(0, 1)
#"""Standardize features by removing the mean and scaling to unit variance
X_train_std=sc.fit_transform(X_train)
# """Fit to data, then transform it.
X_test_std=sc.transform(X_test)
# """Perform standardization by centering and scaling

#5.建立机器学习模型
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion="gini",
                            max_depth= 12,
                            min_samples_split=3,
                            splitter='best')
dtc.fit(X_train_std,y_train)
#6.利用模型进行预测
y_pred=dtc.predict(X_test_std)
print(y_pred)
#7.校验模型
print("model in trainset score is:",dtc.score(X_train_std,y_train))
print("model in testset score is:",dtc.score(X_test_std,y_test))
# model in trainset score is: 1.0
# model in testset score is: 1.0
# #7.保存模型
# from sklearn.externals import joblib
# joblib.dump(dtc,"dtctree.pkl")
# #8.模型可视化
# from sklearn.tree import export_graphviz
# export_graphviz(dtc,filled=True)