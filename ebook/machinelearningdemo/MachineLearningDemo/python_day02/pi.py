#-*- coding: utf-8 -*- 
# @Time : 2018/12/3 8:59
# @Author : Z
# @Email : S
# @File : pi.py

import random

def piDemo(times):
    hists=0
    for i in range(times):
        x=random.random()
        y=random.random()
        # if x*x + y*y<1