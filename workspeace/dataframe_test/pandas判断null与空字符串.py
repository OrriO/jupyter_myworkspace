#!/usr/bin/python
#-*- coding: utf-8 -*-


import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

connect_info = 'mysql+pymysql://root:123456@192.168.3.24:3306/good_doctor_ranking?charset=utf8'
engine = create_engine(connect_info)

# sql = """select DISTINCT department_uuid FROM `department_detail_copy1`"""
sql="""SELECT gmt_created,doctor_uuid,wy_doctor_uuid FROM `doctor_detail_copy1` LIMIT 100"""
fd_hosp = pd.read_sql(sql=sql, con=engine)

print fd_hosp

isnull_ = fd_hosp[fd_hosp['wy_doctor_uuid']!='']
print isnull_

hdf_df = pd.read_excel('D:\\workspace\\liangyibang\\test_data\\feature_engineering\\data\\hdf_1.xlsx')
print hdf_df





['association_member_score', 'academic_leader_score', 'hosp_rank_score','hosp_level_score', 'dept_rank_score', 'expert_level_score']['patient_cnt_score', 'patient_apply_cnt_score', 'praise_rate_score',
                         'avg_reply_time_score', 'like_cnt_score', 'registration_reputation_rate_score',
                         'total_pv_score', 'hosp_niq_score', 'other_influence_score']


[0.16213016, 0., 0.45814334, 0.17033636, 0.00463337, 0.31277735, 0.01076189, 0.11950029, 0.00866538, 0.01682643, -0.02869474, 0.00876804, 0.04134832, 0.00434798, -0.00536017]