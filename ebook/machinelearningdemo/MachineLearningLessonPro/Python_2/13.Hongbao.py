#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 21:14
# @Author  : Z
# @Email   : S
# @File    : 13.Hongbao.py
import random
def hongbao(total,num):
    #total指的是有多少钱
    #num指的是红包有多少个
    result=[]
    #规则：N个人，首先给前N-1个人发红包，在给最后一个人发
    already=0
    for  i in range(1,num):
        t=random.randint(1,(total-already)-(num-i))
        result.append(t)
        already+=t
    result.append(total-already)
    return  result

if __name__ == '__main__':
    total=int(input("please input your money:"))
    num=int(input("please input your num:"))
    for i in range(30):
        result=hongbao(total,num)
        print(result)
