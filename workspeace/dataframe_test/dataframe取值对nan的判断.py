#!/usr/bin/python
#-*- coding: utf-8 -*- 
import pandas as pd
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

dic={'name':['a','a','b','b','b','b','b','c'],'score_1':[1,2,10,11,13,13,12,6],'score_2':[1,3,1,2,20,21,21,7],'score_3':[1,0,1,2,22,22,21,7]}
frame = pd.DataFrame(dic)


print frame

frame['score']=frame['score_1']+frame['score_2']
print frame


# dic1={'name':['a','a','b','b','b','b','b','c'],'score_1':[1,2,10,11,10,np.nan,np.nan,6],'score_2':[1,3,1,2,20,21,21,7],'score_3':[1,0,1,2,22,22,21,7]}
# frame1 = pd.DataFrame(dic1)
#
# tolist = frame1[(frame1['name'] == 'b') |(frame1['name'] == 'a')][['score_1','score_2']]
# score___tolist = tolist['score_1'].tolist()
# print score___tolist
#
# if 10 in tolist:
#     print "1111"