#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 18:10
# @Author  : Z
# @Email   : S
# @File    : 01function.py
#函数有几种类型：
#1.函数的返回值
#2.函数的参数

#无返回值无参数
def repeatString():
    print("helloWorld\t"*5)
repeatString()
repeatString()
#有返回值没有参数
def repeatString():
    return "Hello"
output=repeatString()
print(output)
#没有返回值有参数
def addThreeNumwer(a,b):
    print(a+b)
addThreeNumwer(1,2)
#有返回值有参数
def addThreeNumber1(a,b):
    return a+b
print(addThreeNumber1(1,2))

#全局变量和局部的变量
X=60
def showValue(X):
    print("Current X values is :",X)
    X=100
    print("Change X values is:",X)
showValue(X)
print("Final X value is:",X)

Y=60
def showValueY():
    global Y
    print("current values result is:",Y)
    Y=100
    print("change  values result is:",Y)
showValueY()
print("Final Y result is:",Y)