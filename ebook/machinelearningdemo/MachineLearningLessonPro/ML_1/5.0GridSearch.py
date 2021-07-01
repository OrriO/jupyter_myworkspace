#-*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:26
# @Author  : Z
# @Email   : S
# @File    : 5.0GridSearch.py

from surprise import SVD
from surprise import Dataset
from surprise.model_selection import GridSearchCV
#超参数验证时需要网格搜索的步骤
# Use movielens-100K
data = Dataset.load_builtin('ml-100k')
param_grid = {'n_epochs': [1,2,5, 10,15], 'lr_all': [0.002, 0.005,0.5,5],
              'reg_all': [0.4, 0.6,0.8,1]}
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)

gs.fit(data)

# best RMSE score
print(gs.best_score['rmse'])

# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])