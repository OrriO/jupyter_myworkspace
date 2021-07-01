#-*- coding: utf-8 -*- 
# @Time : 2018/12/4 16:50
# @Author : Z
# @Email : S
# @File : uv_python.py
from pyspark import SparkConf,SparkContext

spark_conf = SparkConf().setAppName("uv_python").setMaster("local[2]")
sc = SparkContext(spark_conf)
data = sc.textFile("C:\\BigData\\07.大数据\\day20_spark02\\资料\\运营商日志\\access.log")
ips = data.map(lambda line:line.split(" ")(0))
count = ips.distinct().count()
print("count:"+count)
sc.stop()


