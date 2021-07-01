#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 21:01
# @Author  : Z
# @Email   : S
# @File    : testAri.py
from ArithMaticDemo import ArithMatic
x=int(input("please input your number:"))
y=int(input("please input your another number:"))
artical=ArithMatic(x,y)
print(artical.add())
print(artical.sub())
print(artical.mul())
print(artical.div())