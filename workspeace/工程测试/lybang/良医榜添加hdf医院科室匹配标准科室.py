#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import sklearn as sk
from sqlalchemy import create_engine
import sys

connect_info = 'mysql+pymysql://root:123456@192.168.3.24:3306/good_doctor_ranking?charset=utf8'
engine = create_engine(connect_info)

sql1 = """SELECT department_name,GROUP_CONCAT(department_uuid) FROM `department_detail_copy1` where gmt_modified>'2019-05-14'  GROUP BY department_name"""
sql2 = """SELECT DISTINCT hdf_department_name from department_relation"""
df1 = pd.read_sql(sql=sql1, con=engine)
df2 = pd.read_sql(sql=sql2, con=engine)

lst1 = df2['hdf_department_name'].tolist()
rea_e = pd.read_excel("D:\\workspace\\data_local_test\\工程测试\\hdf无法匹配科室名称.xlsx")
lst2 = rea_e['dept_name'].tolist()
lst = set(lst1 + lst2)
print(lst)
print(lst2)

print(df1)
frame = df1[~df1['department_name'].isin(lst)]
#
#
#
print(frame)
frame.to_excel("D:\\workspace\\data_local_test\\工程测试\\hdf待匹配科室名称.xlsx")
