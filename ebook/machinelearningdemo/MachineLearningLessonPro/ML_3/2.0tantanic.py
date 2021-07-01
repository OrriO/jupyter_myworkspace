#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 10:29
# @Author  : Z
# @Email   : S
# @File    : 2.0tantanic.py
#1.读取数据
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
datapath=os.path.join(".","tantanic.txt")
tantanic=pd.read_csv(datapath)


def show_data_info():
    print(tantanic.shape)  # (1313, 11)
    print(tantanic.info())
    sns.catplot(x="sex", y="survived", hue="pclass", kind="bar", data=tantanic);
    plt.show()
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 1313 entries, 0 to 1312
    # Data columns (total 11 columns):
    # row.names    1313 non-null int64
    # pclass       1313 non-null object
    # survived     1313 non-null int64
    # name         1313 non-null object
    # age          633 non-null float64
    # embarked     821 non-null object
    # home.dest    754 non-null object
    # room         77 non-null object
    # ticket       69 non-null object
    # boat         347 non-null object
    # sex          1313 non-null object
#调用显示图像和属性函数
show_data_info()
#2.特征工程
#2.1选择特征
X=tantanic[["age","pclass","sex"]]
print(X)
y=tantanic["survived"]
#2.2缺失值处理---age年龄列---均值插补技术
X["age"].fillna(X["age"].mean(),inplace=True)#31.194181
print(X)
#2.3切分数据
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=22)
#2.3类别型变量处理---labelencoder+onehotencoder====>DictVector
from sklearn.feature_extraction import DictVectorizer
dv=DictVectorizer(sparse=False)
X_train_dv=dv.fit_transform(X_train.to_dict(orient="records"))
X_test_dv=dv.transform(X_test.to_dict(orient="records"))
print(X_train_dv)
print(dv.feature_names_)
# [[45.          0.          0.          1.          1.          0.        ]
#  [31.19418104  0.          0.          1.          0.          1.        ]
#  [31.19418104  1.          0.          0.          1.          0.        ]
#  ...
#  [31.19418104  0.          0.          1.          0.          1.        ]
#  [36.          1.          0.          0.          1.          0.        ]
#  [31.19418104  0.          0.          1.          0.          1.        ]]
# ['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male']
#3.建立模型
from sklearn.ensemble import GradientBoostingClassifier
dtc=GradientBoostingClassifier(criterion="mse")
print(dtc.fit(X_train_dv,y_train))
#4.模型预测
y_pred=dtc.predict(X_test_dv)
print(y_pred)
#5.模型校验
print("model in trainset:",dtc.score(X_train_dv,y_train))
print("model in testset:",dtc.score(X_test_dv,y_test))
# model in trainset: 0.8657142857142858
# model in testset: 0.779467680608365
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,y_pred))
# [[152  14]
#  [ 44  53]]
print(classification_report(y_test,y_pred))
