#-*- coding: utf-8 -*- 
# @Time : 2018/12/5 10:55
# @Author : Z
# @Email : S
# @File : Demo07_FromFile.py

import pandas as pd

file = pd.read_csv("./SklearnTest.txt")
#取出height列
print(file["height"])
print(file.height)
#取出height和house两列
print(file.ix[:,"height":"house"])
print(file.iloc[:,0:2])
print(file.loc[:,"height":"house"])