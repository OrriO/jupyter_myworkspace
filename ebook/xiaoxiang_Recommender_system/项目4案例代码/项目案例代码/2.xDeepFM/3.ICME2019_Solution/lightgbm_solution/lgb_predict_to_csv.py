import pandas as pd
import lightgbm as lgb
from config import Config
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import KFold
import numpy as np
import ast
import pickle
import json
import gc

test_data = pd.read_csv(Config["save_test_path"])
test_data.drop(["finish", "like"], axis=1, inplace=True)
finish_model = []
like_model = []

uid = test_data["uid"].values
print(uid.shape)
item_id = test_data["item_id"].values
print(item_id.shape)


def lgb_predict_media():
    for i in range(1, 8):
        with open(Config["model_path_media"] + "_" + "finish" + "_" + str(i), "rb") as f:
            clf_finish = pickle.load(f)
        with open(Config["model_path_media"] + "_" + "like" + "_" + str(i), "rb") as f:
            clf_like = pickle.load(f)

        finish_pred = clf_finish.predict_proba(test_data)[:, 1][:, None]
        print(finish_pred.shape)
        like_pred = clf_like.predict_proba(test_data)[:, 1][:, None]
        print(like_pred.shape)

        result = np.concatenate([uid[:, None], item_id[:, None],
                                     finish_pred, like_pred], 1)
        result_columns = ["uid", "item_id", "finish_probability", "like_probability"]
        result = pd.DataFrame(result, columns=result_columns)
        result.to_csv(Config["predict_file"] + "_lgb_"+str(i),
                      index=None, float_format="%.6f")
        del result
        del finish_pred
        del like_pred
        del clf_finish
        del clf_like
        gc.collect()


def lgb_predict_big():
    for i in range(1, 8):
        with open(Config["model_path_all_views"] + "_" + "finish" + "_" + str(i), "rb") as f:
            clf_finish = pickle.load(f)
        with open(Config["model_path_all_views"] + "_" + "like" + "_" + str(i), "rb") as f:
            clf_like = pickle.load(f)

        finish_pred = clf_finish.predict_proba(test_data)[:, 1][:, None]
        print(finish_pred.shape)
        like_pred = clf_like.predict_proba(test_data)[:, 1][:, None]
        print(like_pred.shape)

        result = np.concatenate([uid[:, None], item_id[:, None],
                                     finish_pred, like_pred], 1)
        result_columns = ["uid", "item_id", "finish_probability", "like_probability"]
        result = pd.DataFrame(result, columns=result_columns)
        result.to_csv(Config["predict_file"] + "_lgb_all_views_"+str(i),
                      index=None, float_format="%.6f")
        del result
        del finish_pred
        del like_pred
        del clf_finish
        del clf_like
        gc.collect()


lgb_predict_big()