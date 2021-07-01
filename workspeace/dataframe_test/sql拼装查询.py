#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import sklearn as sk
from sqlalchemy import create_engine
import sys

dict = {
    "test": """
    123
    """,
    "fudan_hosp_dept_rank": {
        "base": """
                    SELECT
                        data_type AS rank_type,
                        fudan_dept_name,
                        dr.liangyi_department_name AS dept_name,
                        fudan_hosp_name,
                        hdf_hosp_id,
                        wy_hosp_id 
                    FROM
                        fudan_hosp_dept_rank_new fdh
                        LEFT JOIN department_relation dr ON fdh.fudan_dept_name = dr.fudan_department_name 
                """,
        "limit": """
                    WHERE
                        dr.liangyi_department_name IN %s
                """,
        "group": """
                    GROUP BY
                        fdh.data_type,
                        fdh.fudan_dept_name,
                        fdh.fudan_hosp_name
                """
    }
}

connect_info = 'mysql+pymysql://root:123456@192.168.3.24:3306/good_doctor_ranking?charset=utf8'
engine = create_engine(connect_info)
sql = dict.get('fudan_hosp_dept_rank').get('base') + dict.get('fudan_hosp_dept_rank').get('group')
print sql
wy_expert_df = pd.read_sql(sql=sql, con=engine)
print  wy_expert_df
sql2= dict.get('fudan_hosp_dept_rank').get('base') +dict.get('fudan_hosp_dept_rank').get('limit')%"('皮肤科')"+ dict.get('fudan_hosp_dept_rank').get('group')
wy_expert_df2 = pd.read_sql(sql=sql2, con=engine)
print  wy_expert_df2