#!/usr/bin/python
#-*- coding: utf-8 -*- 
#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import pymysql
import pandas as pd
import numpy as np
import sklearn as sk
from sqlalchemy import create_engine
import sys
from itertools import chain

connect_info = 'mysql+pymysql://root:123456@192.168.3.24:3306/good_doctor_ranking?charset=utf8'
engine = create_engine(connect_info)

sql="""select DISTINCT wy_hosp_name,wy_hosp_id from fudan_hosp_dept_rank_new where wy_hosp_id !=' '"""
read_sql = pd.read_sql(sql=sql, con=engine)
str_split = lambda x: x.split(',')
tolist = tuple(set(chain.from_iterable(read_sql['wy_hosp_id'].apply(str_split).tolist())))
print (tolist)








