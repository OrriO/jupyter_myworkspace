#-*- coding: utf-8 -*-
# @Time    : 2018/12/9 18:02
# @Author  : Z
# @Email   : S
# @File    : 5.0Sampiling.py
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=5000, n_features=2, n_informative=2,
                            n_redundant=0, n_repeated=0, n_classes=3,
                            n_clusters_per_class=1,
                            weights=[0.01, 0.05, 0.94],
                            class_sep=0.8, random_state=0)
from collections import Counter
print(sorted(Counter(y).items()))
from imblearn.under_sampling import ClusterCentroids
ros = ClusterCentroids(random_state=0)
X_resampled, y_resampled = ros.fit_sample(X, y)
from collections import Counter
print(sorted(Counter(y_resampled).items()))
# [(0, 4674), (1, 4674), (2, 4674)]

# [(0, 64), (1, 262), (2, 4674)]
# [(0, 64), (1, 64), (2, 64)]