#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import pymysql

# db = pymysql.connect("192.168.3.24", "root", "123456", "good_doctor_ranking", charset='utf8mb4', port=3306)
cursor = db.cursor()

datas = pd.read_excel("D:\\workspace\\data_local_test\\工程测试\\lydata\\2019年5月17日hdf科室匹配.xlsx")

to_dict = datas.to_dict(orient="recoder")
for data in to_dict:
    print(data)
    # data.decode()
    fudan_department = data['fudan_department']
    print(type(fudan_department))
    hos_department = data['hos_department']
    liangyi_department = data['liangyi_department']
    sql = "INSERT INTO `good_doctor_ranking`.`department_relation`(`fudan_department_name`, `liangyi_department_name`, `hdf_department_name`, `gmt_modified`, `gmt_created`) " \
          "VALUES ('%s', '%s', '%s', NOW(), NOW())" % (fudan_department, liangyi_department, hos_department)
    cursor.execute(sql)
db.commit()
db.close()
