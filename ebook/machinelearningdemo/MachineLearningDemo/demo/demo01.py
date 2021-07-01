#!/usr/bin/python
# -*- coding: utf-8 -*-


# class demo01(object):
#     # def city_weather_update(self):
#     #     self.logging = log(className=self.__class__.__name__)
#
#     def usemysql(self):
#
#
# from api.db import mysql
#
# mysql.set_db("operation", connect=0)
# sql = "SELECT * FROM user WHERE phone='17681862709' "
# # data = mysql.pandas_readsql(sql)
#
# mysql_get = mysql.get(sql)
#
# print(mysql_get)
from impala.dbapi import connect
import pandas as pd

db = connect(host='120.27.241.54', port=21050, timeout=3600)
sql = """SELECT * FROM ids.mysql_boxdetail_wide INNER JOIN ids.mysql_user_wide ON ids.mysql_boxdetail_wide.userid=ids.mysql_user_wide.id
INNER JOIN
  (SELECT boxid,
          saled,
          price AS boxprice
   FROM ids.box_attribute) boxAttributeintro ON ids.mysql_boxdetail_wide.boxid=boxAttributeintro.boxid
INNER JOIN
  (SELECT id AS productid,
          spuid,
          cate1,
          cate2,
          cate3
   FROM ids.mysql_product_wide) productwide ON ids.mysql_boxdetail_wide.prodid=productwide.productid
INNER JOIN
  (SELECT id AS spuid,
          brand AS spubrand
   FROM ods.spu) spuintro ON productwide.spuid=spuintro.spuid
INNER JOIN
  (SELECT id AS brandid,
          ranking AS brandranking,
          price AS brandprice,
          domesticfamous AS branddomesticfamous,
          overseas AS brandoverseas,
          brandawareness AS brandawareness
   FROM ods.productbrand) productbrandintro ON spuintro.spubrand=productbrandintro.brandid
INNER JOIN
  (SELECT id BoxId,
          coatprice AS Boxcoatprice,
          pantsprice AS BOxpantsprice,
          shirtprice AS Boxshirtprice,
          shoesprice AS Boxshoesprice,
          teeprice AS Boxteeprice
   FROM ids.mysql_box_wide
   GROUP BY id,
            coatprice,
            pantsprice,
            shirtprice,
            shoesprice,
            teeprice) mysqlBoxWide ON ids.mysql_boxdetail_wide.boxid=mysqlBoxWide.BoxId
WHERE ids.mysql_boxdetail_wide.status IN(2, 3) limit 20000"""
df = pd.read_sql(sql, con=db)
df.to_excel('D:\data2.xlsx', index=0)

print("-------------")
db.close()
