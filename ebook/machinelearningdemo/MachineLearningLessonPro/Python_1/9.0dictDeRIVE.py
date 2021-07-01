#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 16:51
# @Author  : Z
# @Email   : S
# @File    : 9.0dictDeRIVE.py
#符合条件的字典---字典表达式
#1.
print({i:str(i) for i in range(10)})
#2.
x=['A','B','C','D']
y=['a','b','c','d']
e_dict={i:j for i,j in zip(x,y)}
print(e_dict)
#3.有序字典
from collections import OrderedDict
ord1=OrderedDict() #将类初始化为一个对象
ord1["apple"]=1
ord1["pear"]=2
ord1["banana"]=3
print(ord1)
# OrderedDict([('apple', 1), ('pear', 2), ('banana', 3)])