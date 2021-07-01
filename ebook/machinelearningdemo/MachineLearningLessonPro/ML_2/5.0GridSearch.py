#-*- coding: utf-8 -*-
# @Time    : 2018/12/8 15:53
# @Author  : Z
# @Email   : S
# @File    : 5.0GridSearch.py
from sklearn import tree, datasets
from sklearn.model_selection import GridSearchCV
iris = datasets.load_iris()
parameters = {'criterion':('gini', 'entropy'), 'splitter':["random", "best"],
              'max_depth': [1,2,3,10,12],
              'min_samples_split': (2,3),
              'max_features': (1,2,3),}
dtc = tree.DecisionTreeClassifier()
# criterion="gini",
#                  splitter="best",
#                  max_depth=None,
#                  min_samples_split=2,
#                  min_samples_leaf=1,
#                  min_weight_fraction_leaf=0.,
#                  max_features=None,
#                  random_state=None,
#                  max_leaf_nodes=None,
#                  min_impurity_decrease=0.,
clf = GridSearchCV(dtc, parameters, cv=5)
clf.fit(iris.data, iris.target)
print(clf.best_params_)
# {'criterion': 'gini', 'max_depth': 12, 'max_features': 3, 'min_samples_split': 3, 'splitter': 'best'}
# ...
# GridSearchCV(cv=5, error_score=...,
#        estimator=SVC(C=1.0, cache_size=..., class_weight=..., coef0=...,
#                      decision_function_shape='ovr', degree=..., gamma=...,
#                      kernel='rbf', max_iter=-1, probability=False,
#                      random_state=None, shrinking=True, tol=...,
#                      verbose=False),
#        fit_params=None, iid=..., n_jobs=None,
#        param_grid=..., pre_dispatch=..., refit=..., return_train_score=...,
#        scoring=..., verbose=...)
print(sorted(clf.cv_results_.keys()))
# ...
# ['mean_fit_time', 'mean_score_time', 'mean_test_score',...
#  'mean_train_score', 'param_C', 'param_kernel', 'params',...
#  'rank_test_score', 'split0_test_score',...
#  'split0_train_score', 'split1_test_score', 'split1_train_score',...
#  'split2_test_score', 'split2_train_score',...
#  'std_fit_time', 'std_score_time', 'std_test_score', 'std_train_score'...]