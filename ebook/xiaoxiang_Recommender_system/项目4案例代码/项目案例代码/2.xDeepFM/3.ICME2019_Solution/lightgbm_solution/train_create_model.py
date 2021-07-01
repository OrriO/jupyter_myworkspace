import pandas as pd
import lightgbm as lgb
from config import Config
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import KFold
import numpy as np
import ast
import pickle
import json
import time
import gc

start = int(input("start: "))
end = int(input("end: "))


def lgb_all_views():
    for i in range(start, end+1):
        data = pd.read_csv(Config["big_data_all_feature_path"] + str(i))
        data_label = dict()
        data_label["like"] = data["like"]
        data_label["finish"] = data["finish"]

        data.drop(["finish", "like"], axis=1, inplace=True)
        for task in ["finish", "like"]:
            print("number of data: ", i)
            print("task: ", task)
            s = time.time()
            clf = lgb.LGBMClassifier(
                boosting_type="gbdt", num_leaves=31, reg_alpha=0.0, reg_lambda=1,
                max_depth=-1, n_estimators=2000, objective="binary",
                subsample=0.7, colsample_bytree=0.7, subsample_freq=1,
                learning_rate=0.05, min_child_weight=50, random_state=2019, n_jobs=9
            )
            clf.fit(data, data_label[task], verbose=True,
                    eval_set=[(data, data_label[task])], eval_metric="auc")
            with open(Config["model_path_all_views"] + "_" + task + "_" + str(i), "wb") as f:
                pickle.dump(clf, f)
            e = time.time()
            print("time consuming: ", e - s)
            gc.collect()

            del clf
        del data
        del data_label


def lgb_media():
    for i in range(start, end + 1):
        data = pd.read_csv(Config["save_all_data_path"] + str(i))
        data_label = dict()
        data_label["like"] = data["like"]
        data_label["finish"] = data["finish"]

        data.drop(["finish", "like"], axis=1, inplace=True)
        for task in ["finish", "like"]:
            print("number of data: ", i)
            print("task: ", task)
            s = time.time()
            clf = lgb.LGBMClassifier(
                boosting_type="gbdt", num_leaves=31, reg_alpha=0.0, reg_lambda=1,
                max_depth=-1, n_estimators=1000, objective="binary",
                subsample=0.7, colsample_bytree=0.7, subsample_freq=1,
                learning_rate=0.05, min_child_weight=50, random_state=2019, n_jobs=5
            )
            clf.fit(data, data_label[task], verbose=True,
                    eval_set=[(data, data_label[task])], eval_metric="auc")
            with open(Config["model_path_media"] + "_" + task + "_" + str(i), "wb") as f:
                pickle.dump(clf, f)
            e = time.time()
            print("time consuming: ", e - s)
            del clf
            gc.collect()

        del data
        del data_label


lgb_all_views()