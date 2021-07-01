#-*- coding: utf-8 -*-
# @Time    : 2018/10/29 12:25
# @Author  : Z
# @Email   : S
# @File    : 25HongbaoDev.py
#-*-coding:utf8-*-
#模拟发红包程序
import random
def hongbao(total,num):
    total=float(total)#红包数
    num=int(num)#红包总额
    min = 0.01  # 最小红包
    if (num < 1):
        return
    if num == 1:
        print("第%d个人拿到红包数为：%.2f" % (num, total))
        return
    i = 1
    while (i < num):
        #过程解释：
        #num=4,total=10
        #i=1,1<4,10-0.03=9.97,k=1,if假,max=9.97/1=9.97,money=随机数(1,997),假设650，取余得到6.50，total=10-6.5=3.5
        #total=3.5 i=2,2<4,max=3.5-0.01*(4-2)=3.5-0.02=3.48,k=0,k=2,max=3.48/2=1.24 money=(1,124),假设20，取余得到0.2，total=3.5-0.2=3.3
        #total=3.3 i=3,3<4,max=3.3-0.01(4-3)=3.29,k=0,k=1,max=3.3,money=(1,330),假设130，取余得1.3，total=3.3-1.3=2
        #total=2,i=4不小于num=4,退出while循环，将剩余的2元钱拿到自己手里，程序结束

        # 保证即使一个红包是最大的了, 后面剩下的红包, 每个红包也不会小于最小值
        max = total - min * (num - i)
        k = int((num - i) / 2)
        #保证最后两个人拿的红包不超出剩余红包
        if num - i <= 2:
            k = num - i
        #最大的红包限定的平均线上下
        max = max / k
        #保证每个红包大于最小值,又不会大于最大值
        monney = random.randint(int(min * 100), int(max * 100))
        #保留两位小数
        monney = float(monney) / 100
        total = total - monney
        print("第%d个人拿到红包数为：%.2f, 余额为: %.2f" % (i, monney, total))
        i += 1

    print("第%d个人拿到红包数为：%.2f, 余额为: %.2f" % (i, total, 0.0))#最后一个人拿走剩下的红包
    # each=[]
    # already=0
    # for i in range(1,num):
    #     t=random.randint(1,(total-already)-(num-i))
    #     each.append(t)
    #     already=already+t
    # each.append(total-already)
    # return each
if __name__=='__main__':
    total = input('输入红包总金额:')
    num = input('输入发红包数量:')
    try:
        # 模拟30次
        for i in range(30):
            each = hongbao(total, num)
            print(each)
    except:
        print('Error')