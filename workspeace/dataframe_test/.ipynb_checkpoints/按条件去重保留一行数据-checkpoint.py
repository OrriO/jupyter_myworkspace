#!/usr/bin/python
#-*- coding: utf-8 -*- 
import pandas as pd
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

dic={'name':['a','a','b','b','b','b','b','c'],'score_1':[1,2,10,11,13,13,12,6],'score_2':[1,3,1,2,20,21,21,7],'score_3':[1,0,1,2,22,22,21,7]}
frame = pd.DataFrame(dic)

# data = frame.groupby('name')['score_1'].idmax()
data1 = frame.sort_values(['score_1','score_2','score_3'], ascending=False).groupby('name', as_index=False).first()
#score的顺序就是排序有先后顺序，ascending=false是降序配合first选取分组中的最大值
data2 = frame.sort_values(['score_3','score_1','score_2'], ascending=False).groupby('name', as_index=True).first()
# print(frame)

# print data1
# print data2
print (frame)
# a=frame[['name','score_1']]
# print a
# print type(a)


agg = frame.groupby('name',as_index=False).agg({'score_1': np.max, 'score_2': np.max, 'score_3': np.max})
print (agg)
print (type(agg))


