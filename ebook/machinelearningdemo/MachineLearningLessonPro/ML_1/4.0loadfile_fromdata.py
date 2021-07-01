#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:08
# @Author  : Z
# @Email   : S
# @File    : 3.0loadfile_fromdata.py
import  os

from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
# 1.path to dataset file
file_path = os.path.expanduser('./u.data')
# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader=reader)
#2.切分数据
trainset, testset = train_test_split(data, test_size=.25)
# # We can now use this dataset as we please, e.g. calling cross_validate
# cross_validate(BaselineOnly(), data, verbose=True)
#3.初始化算法
algo=BaselineOnly()
#4.fit--结合算法+数据。构建模型-------algo
algo.fit(trainset)
#5.通过test进行预测
predictions = algo.test(testset)
print(predictions)
#6.检验算法
# Then compute RMSE
print(accuracy.rmse(predictions))