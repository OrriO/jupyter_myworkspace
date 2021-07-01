#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 12:09
# @Author  : Z
# @Email   : S
# @File    : 4.1printFunction.py
age=12
name="zhangsan"
print("name is:",name,"age is:",age,"Over")
print("name is:"+name+"age is:"+str(age)+" Over") #TypeError: must be str, not int
print("name is {},age is {},Over".format(name,age))
print("name is {0},age is {1},Over".format(name,age))
print("name is:%s,age is %d,Over"%(name,age))