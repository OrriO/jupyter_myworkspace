import pandas as pd
import numpy as np
from config import Config

nffm_result = pd.read_csv(Config["predict_file"] + "nffm")
uid = nffm_result["uid"].values
item_id = nffm_result["item_id"].values
nffm_finish = nffm_result["finish_probability"].values
nffm_like = nffm_result["like_probability"].values
del nffm_result

# lgb
finish = np.zeros(uid.shape[0], dtype=np.float64)
like = np.zeros(uid.shape[0], dtype=np.float64)
for i in range(1, 8):
    print (i)
    lgb_result = pd.read_csv(Config["predict_file"]+"_lgb_"+str(i))
    finish += lgb_result["finish_probability"].values
    like += lgb_result["like_probability"].values
    del lgb_result

finish /= 7
like /= 7
finish = (finish + nffm_finish) / 2
like = (like + nffm_like) / 2

data = np.concatenate([uid[:,None], item_id[:, None], finish[:, None], like[:, None]], 1)
result = pd.DataFrame(data, columns=["uid", "item_id", "finish_probability", "like_probability"])
result.to_csv(Config["predict_file"], index=None, float_format="%.6f")