# -*- coding: utf-8 -*-
# @Time : 2018/12/13 17:16
# @Author : Z
# @Email : S
# @File : test2.py

from pyspark.mllib.linalg import Matrix, Matrices

# Create a dense matrix ((1.0, 2.0), (3.0, 4.0), (5.0, 6.0))
dm2 = Matrices.dense(3, 2, [1, 3, 5, 2, 4, 6])
print(dm2)

# Create a sparse matrix ((9.0, 0.0), (0.0, 8.0), (0.0, 6.0))
sm = Matrices.sparse(3, 2, [0, 1, 3], [0, 2, 1], [9, 6, 8])
print(sm)

import tensorflow as tf

print(tf.__version__)


