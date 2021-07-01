#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:36
# @Author  : Z
# @Email   : S
# @File    : 8.0pickle.py
import pandas as pd
original_df = pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
print(original_df)
pd.to_pickle(original_df, "./dummy.pkl")
unpickled_df = pd.read_pickle("./dummy.pkl")
print(unpickled_df)