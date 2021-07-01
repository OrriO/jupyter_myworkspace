#!/usr/bin/python
# -*- coding: utf-8 -*- 

import pandas as pd
# import pymysql
from sqlalchemy import create_engine
from itertools import chain


def get_list(df, str):
    """
    榜单匹配中一对多情况，对数据进行切分合并
    :param df:
    :param str:
    :return:
    """
    str_split = lambda x: x.split(',')
    tolist = set(chain.from_iterable(df[str].apply(str_split).tolist()))
    return tolist

connect_info = 'mysql+pymysql://root:123456@192.168.3.24:3306/good_doctor_ranking?charset=utf8'
sql = """SELECT hosp_name,wy_hosp_id FROM `technology_hosp_rank` """
engine = create_engine(connect_info)

data_frame = pd.read_sql(sql=sql, con=engine)

print(data_frame)

ll = lambda x: x.split(',')

tolist = get_list(data_frame, 'wy_hosp_id')
print(tolist)
if '103f8180-abfd-4488-b5c7-dd7ad39e97a6000' in tolist:
    print('11111111111')
