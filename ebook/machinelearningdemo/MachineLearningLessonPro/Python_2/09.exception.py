#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:50
# @Author  : Z
# @Email   : S
# @File    : 09.exception.py
# 2/0 #ZeroDivisionErro r: division by zero
# print(name*4) #NameError: name 'name' is not defined
try:
    2/0 #ZeroDivisionError: division by zero
    age=int(input("please input your age:"))
    print(age) #ValueError: invalid literal for int() with base 10: '80098090-=='
except:
    print("input again!")
finally:
    print("Finish")