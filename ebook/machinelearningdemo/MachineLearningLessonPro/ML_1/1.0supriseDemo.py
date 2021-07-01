#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:03
# @Author  : Z
# @Email   : S
# @File    : 1.0supriseDemo.py
#安装：pip install suprise
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin('ml-100k')
# We'll use the famous SVD algorithm.
algo = SVD()
# Run 5-fold cross-validation and print results
print(cross_valiFdate(algo, data, measures=['RFMSE', 'MAE'], cv=5, verbose=True))