#!/usr/bin/python
#-*- coding: utf-8 -*-
import pandas as pd
dic={'name':['a','a','b','b','b','b','b','c'],'score_1':[1,2,10,11,13,13,12,6],'score_2':[1,3,1,2,20,21,21,7],'score_3':[1,0,1,2,22,22,21,7]}
frame = pd.DataFrame(dic)
print(frame)
frame.columns=['a','b','c','d']
print(frame)