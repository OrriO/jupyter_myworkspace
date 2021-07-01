#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 8:54
# @Author  : Z
# @Email   : S
# @File    : 14.estimatePi.py
import random
#times是表示落入正方形内的次数
def estimatePiDemo(times):
    #定义变量表示落入圆内次数
    hists=0
    #在落入正方形之上如何落入圆内
    for i in range(times):
        x=random.random()*2-1 #x in the interval [0, 1)
        y=random.random()*2-1 #x in the interval [0, 1)
        if x*x+y*y <1:
            hists+=1
    return 4.0*hists/times

#测试
if __name__ == '__main__':
    PI=estimatePiDemo(10000)
    print(PI)
