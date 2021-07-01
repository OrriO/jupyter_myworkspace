# -*- coding: utf-8 -*-
# @Time : 2018/12/12 14:44
# @Author : Z
# @Email : S
# @File : test1.py


# age = 18
# name = "xiaohua"
# print("我的姓名是%s,年龄是%d"%(name,age))
# print("sssssssssssss\nlllllllllll")
#
# password = input("请输入密码:")
# print ('您刚刚输入的密码是:', password)
# a=5
# b=3
# c=a%b
# print(c)
from functools import reduce

from numpy import long

# x='234'
# print(type(x))
# print(type(int(x)))
# print(float(x))

# todo:demo01
# age = 30
# print("------if判断开始------")
# if age >= 18:
#     print("我已经成年了")
# print("------if判断结束------")

# todo:demo02
# i = 0
# while i < 5:
#     print("当前是第%d次执行循环" % (i + 1))
#     print("i=%d" % i)
#     i += 1

# todo:demo03
# i = 1
# while i<=9:
#     j=1
#     while j<=i:
#         print("%d*%d=%-2d "%(j,i,i*j),end='')
#         j+=1
#     print('\n')
#     i+=1

# todo:demo04
# name = 'abcdef'
# print(name[3:5])  # 取 下标为3、4 的字符
# print(name[::-1])
#
# a = "hello itcast"
# print(a.title())

# todo:demo05 list
# a = ['a', 'b', 'c', 'a', 'b']
# print(a.index('a',1,4))

# a = [1, 4, 2, 3]
# a.sort()
# print(a)
# a.reverse()
# print(a)

# chars = ['a', 'b', 'c', 'd']
# for i, chr in enumerate(chars):
#     print(i, chr)

# a=1
# b=a
# print(b)
# a=2
# print(b)

# def test(a,b):
#     '用来完成对2个数求和'
#     print("%d"%(a+b))
#
# test(11,12)
# help(test)
#
# map()
# reduce()
#
# seq1=['foo','x41','?1','***']
# def func(x):
#     return x.isalnum()
# print(filter(func,seq1)) #返回filter对象
# print(list(filter(func,seq1))) #将filter转化为列表
# import tkinter.simpledialog as dl
# import tkinter.messagebox as mb
#
# mb.showinfo(title="llalla",message="HelloWorld")
# dl.askinteger("ask integer","Please input your age:")

# todo:等差数列

import numpy as np

# r1 = np.linspace(1, 9, num=9)
# print(r1)

# n1=np.random.rand(3,3)
# n2=np.random.randn(3,3)
# print(n1)
# print(type(n1))
# print(n2)
# print(type(n2))

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[6, 23], [-1, 7], [8, 9]])
# print(x)
# print(y)
# print(x.dot(y))
# print(np.dot(x,y))
from numpy.linalg import qr

# Q,R=qr(x)
# print(Q)
# print(R)
# print(Q.dot(R))
from numpy.linalg import eig
#
# value,vector = eig(x)
# print(value)
# print(vector)

# todo:pandas
import pandas as pd

# s1 = pd.Series((1, 2, 3, 4),("a","b","c","c"))
# s1.index.name="in"
# s1.name="2"
# print("------",type(s1.name))
# print(s1)
# print(type(s1))
# print(s1["c"])

# obj= pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# unique=obj.unique()
# print(unique)
# print(obj.value_counts())

# df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9, 9]], ("a", "b", "b"),["a",1,"a","D"])
# print(df1)
# print(df1["a"])
# df1.ix["b","a"]=100
# print(df1)
# print("-------------------")
# print(df1["b"])
# print(df1.dropna(axis=0))
# print(df1)
# print(df1.drop(["a"],axis=1))
# print("-------------------")
#
# df2=df1-df1.drop(["a"],axis=1)
# print(df2)
# pd.read_csv()

import matplotlib.pyplot as plt

plt.plot([1,2],[5,9])
plt.show()
print(pd.__version__)
