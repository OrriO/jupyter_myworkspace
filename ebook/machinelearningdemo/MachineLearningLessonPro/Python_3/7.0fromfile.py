#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 10:51
# @Author  : Z
# @Email   : S
# @File    : 7.0fromfile.py
import pandas as pd
file=pd.read_csv("./SklearnTest.txt")
print(file)
#1.取出height列
print(file["height"])
print(file.height)
#2.取出heigt和house两列
print(file.ix[:,"height":"house"])
print(file.iloc[:,0:2])
print(file.loc[:,"height":"house"])
#3.取出样本数据0-5行样本数据
print(file.iloc[0:6,:])
print(file.loc[0:6,:])
#4.选择特征列和列别标签列
X1=file.ix[:,"height":"job"]
print(X1)
print(type(X1))
Y1=file.ix[:,"is_date"]
print(Y1)
print(type(Y1)) #<class 'pandas.core.series.Series'>
#5.选择is_date=
new_Date=file.query("is_date==-1")
data=file.query("is_date!=-1")
print(new_Date)
#    height  house  car  handsome  job  is_date
# 8    1.65      0    1       6.6    0       -1
print(data)
#    height  house  car  handsome  job  is_date
# 0    1.80      1    0       6.5    2        1
# 1    1.62      1    0       5.5    0        1
# 2    1.71      0    1       8.5    1        1
# 3    1.58      1    1       6.3    1        1
# 4    1.68      0    1       5.1    0        0
# 5    1.63      1    0       5.3    1        0
# 6    1.78      0    0       4.5    0        0
# 7    1.64      0    0       7.8    2        0
#6.将data已经处理好的数据分为X和y
X=data.iloc[:,0:5]
y=data.iloc[:,5]
print(X)
print(type(X)) #<class 'pandas.core.frame.DataFrame'>
print(y)
print(type(y)) #<class 'pandas.core.series.Series'>

X=data.drop("is_date",axis=1)
print(X)
print(type(X)) #<class 'pandas.core.frame.DataFrame'>
# data["is_date"]
# data.is_date
# data.ix
# data.iloc
# data.loc

X.to_csv("result.txt",sep=",")
datafile=pd.read_csv("result.txt")
print(datafile)