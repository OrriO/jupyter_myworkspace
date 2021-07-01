#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 12:00
# @Author  : Z
# @Email   : S
# @File    : 4.0input.py
#python2中input是原样输入
#如果输入的是字符串类型，请务必加上括号，明确表示
# input1 = input("please input your age:") #NameError: name 'zhangsan' is not defined
# print(input1)
# print(type(input1))
# # please input your age:"zhangsan"
# # zhangsan
# # <type 'str'>

#raw——input--无论输入的是什么输出的都是string类型
# input2=raw_input("please input your age:")
# print(input2)
# print(type(input2)) #<type 'str'>

#python3中的input和python2中raw_input一致
age=int(input("please input your age:"))
print(age)
print(type(age))