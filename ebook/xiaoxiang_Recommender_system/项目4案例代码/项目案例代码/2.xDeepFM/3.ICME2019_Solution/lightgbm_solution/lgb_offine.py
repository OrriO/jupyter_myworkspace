import lightgbm as lgb
import pandas as pd
import numpy as np
from config import Config

data = pd.read_csv(Config["big_data_all_feature_path"] + str(1))
like = data["like"]
# finish = data["finish"]
data.drop(["finish", "like"], axis=1, inplace=True)
train_data = lgb.Dataset(data, label=like)
print("train data lgb")
del data
del like

val = pd.read_csv(Config["big_data_all_feature_path"] + str(2))
like = val["like"].iloc[:10000]
val = val.iloc[:10000]
val.drop(["finish", "like"], axis=1, inplace=True)
val_data = lgb.Dataset(val, label=like)
print("val data lgb")
del val
del like

parameters = {
    "boosting_type": "gbdt",
    'num_leaves': 31,
    'reg_alpha': 0.0,
    'reg_lambda': 1,
    'max_depth': -1,
    'n_estimators': 1500,
    'objective': "binary",
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'subsample_freq': 1,
    'learning_rate': 0.05,
    'min_child_weight': 50,
    'random_state': 2019,
    'n_jobs': 5,
    'is_unbalance': True,
    "metric": "auc",
    "verbose": 1,
    "device": "gpu"
}

clf = lgb.train(params=parameters,
                train_set=train_data,
                valid_sets=val_data,
                early_stopping_rounds=100)
