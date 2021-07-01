#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 18:22
# @Author  : Z
# @Email   : S
# @File    : 02functionParameters.py
#默认参数
def showNumber(x,y=1,z=1):
    print(x+y+z)
showNumber(1,1,1)
#关键字参数
def addThreeNumber(a,b,c=1):
    print(a+b+c)
addThreeNumber(1,2,3)
addThreeNumber(a=1,b=2,c=3)
addThreeNumber(c=3,a=1,b=2)
addThreeNumber(a=1,b=2)
#VarArgs参数
#* 表示可迭代的对象---元祖或列表
#**表示的是字典--key：value
def printFunction(fparameters,*tuple1,**dict1):
    print(fparameters)
    print(tuple1)
    print(dict1)
printFunction(1,2,3,4,5,"okok",age="12",name="zhangsan")

vec=[[1,2,3],[4,5,6],[7,8,9]]
print(list(map(list,zip(*vec))))
print(list(map(list,zip([1,2,3],[4,5,6],[7,8,9]))))


#4.传递参数时的序列解包
def demo3(a,b,c):
    print(a+b+c)
seq=[1,2,3]
demo3(*seq)

tup=(1,2,3)
demo3(*tup)
