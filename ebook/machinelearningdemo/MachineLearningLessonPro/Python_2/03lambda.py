#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 18:32
# @Author  : Z
# @Email   : S
# @File    : 03lambda.py
# 语法：lambda 变量：表达式
# x*x
#lambda 匿名函数
g=lambda x:x*x
print(g(9))
#三个数字的之和
g1=lambda x,y,z=0:x+y+z
print(g1(1,1,1))
#直接输出结果
print((lambda x,y,z=0:x+y+z)(1,2,3))
#lambda函数直接用于map、reduce、filter函数
addNumber=list(map(lambda x,y,z:x+y+z,range(5),range(5),range(5)))
print(addNumber)


data=list(range(20))
print(data)
import random
random.shuffle(data)
print("shuffle data:",data)
print((lambda x:x)(data)) #[19, 16, 9, 17, 14, 12, 10, 3, 4, 8, 0, 2, 7, 13, 11, 1, 15, 6, 18, 5]
data.sort(key=lambda x:x)
print(data)
print("="*100)
print((lambda x:len(str(x)))(data)) #[19, 16, 9, 17, 14, 12, 10, 3, 4, 8, 0, 2, 7, 13, 11, 1, 15, 6, 18, 5]
data.sort(key=lambda x:len(str(x))) #使用lambda表达式指定排序规则
print(data)
data.sort(key=lambda x:len(str(x)),reverse=True)
print(data)