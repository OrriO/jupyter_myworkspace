import pandas as pd
# import lightgbm as lgb
from config import Config
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import KFold
import numpy as np
import ast
import pickle
import json
'''
user_id_num: 70711
item_id_num:  3687156
author_id: 778113
item_city: 456
music_id: 82841
device_id: 71681
Duration: 128
'''


'''
onehot：
item_city
duration_time

对于vector特征：
"uid", "user_city", "item_id", "author_id",
"channel", "music_id", "device"
1.提取每个id的数量
2.每个id的正样本数
3.每个id的转化率
4.user_id 跟 item_id组合出现次数
5.组合正样本次数
'''


def g_deep():
    columns = ["uid", "user_city", "item_id", "author_id", "item_city",
                "channel", "finish", "like", "music_id", "device",
                "create_time", "duration_time"]

    data = pd.read_csv(Config["raw_data_path"], sep='\t', names=columns)
    test_data = pd.read_csv(Config['raw_test_path'], sep='\t', names=columns)
    print("finish reading")

    # outline data
    data[data["duration_time"] == 70000] = data.duration_time.median()
    data[data["finish"] == 10] = 0
    data[data["like"] == 10] = 0
    data = data.astype(int)
    test_data = test_data.astype(int)

    # output field size for each feature
    for c in data.columns:
        max_id = max(data[c].max(), test_data[c].max())
        min_id = min(data[c].max(), test_data[c].min())
        print(c, ':', " min: ", min_id, " max: ", max_id+1)

    # data clean
    # user_city, item_city, music_id should plus one
    data["user_city"] = data["user_city"] + 1
    data["item_city"] = data["item_city"] + 1
    data["music_id"] = data["music_id"] + 1
    test_data["user_city"] = test_data["user_city"] + 1
    test_data["item_city"] = test_data["item_city"] + 1
    test_data["music_id"] = test_data["music_id"] + 1

    # split target to finish_lisk: 01, 11, 10, 00
    data["fl_00"] = 0
    data["fl_01"] = 0
    data["fl_11"] = 0
    data["fl_10"] = 0

    test_data["fl_00"] = 0
    test_data["fl_01"] = 0
    test_data["fl_11"] = 0
    test_data["fl_10"] = 0

    data["fl_00"][(data.finish == 0)&(data.like == 0)] = 0
    data["fl_01"][(data.finish == 0)&(data.like == 1)] = 1
    data["fl_11"][(data.finish == 1)&(data.like == 1)] = 2
    data["fl_10"][(data.finish == 1)&(data.like == 0)] = 3

    data["target"] = data["fl_00"] + data["fl_01"] + data["fl_11"] + data["fl_10"]

    # add title data


    # split
    train_size = int(data.shape[0] * (1 - 0.2))
    train = data.iloc[:train_size]
    val = data.iloc[train_size:]
    train.to_csv(Config["train_path"], index=False)
    print("finish train")
    val.to_csv(Config["val_path"], index=False)
    print("finish val")
    test_data.to_csv(Config["test_path"], index=False)
    print("finish test")
    data.to_csv(Config["all_data_path"], index=False)


def g_train(data):
    columns = data.columns
    data = data.copy().values
    vector_f = ["uid", "user_city", "item_id", "author_id", "item_city",
                "channel", "music_id", "device", "duration_time"]
    kf = KFold(n_splits=7, shuffle=False)
    count = 0
    for train_index, test_index in kf.split(data):
        count += 1
        print("*************"+str(count)+"*****************")
        train = pd.DataFrame(data=data[train_index], columns=columns)
        test = pd.DataFrame(data=data[test_index], columns=columns)
        for i in range(len(vector_f)):
            print("first_order_feature: " + vector_f[i])
            for label in ["finish", "like"]:
                f = vector_f[i]
                label_rate = train.groupby(f)[label].mean().rename(f + "_" + label + "_rate").reset_index()  # 转化率
                label_sum = train.groupby(f)[label].sum().rename(f + "_" + label + "_num").reset_index()  # 正样本个数
                test = test.merge(right=label_rate, how="left", left_on=f, right_on=f)
                test = test.merge(right=label_sum, how="left", left_on=f, right_on=f)

            feature_num = train.groupby(f)[label].count().rename(f + "_num").reset_index()
            test = test.merge(right=feature_num, how="left", left_on=f, right_on=f)

            print("second_order_feature")
            for j in range(i+1, len(vector_f)):
                f1 = vector_f[i]
                f2 = vector_f[j]
                print("start: "+f1+"_"+f2)
                for label in ["finish", "like"]:
                    label_rate = train.groupby([f1, f2])[label].\
                        mean().rename(f1+"_"+f2+"_"+label+"_rate").reset_index()
                    label_sum = train.groupby([f1, f2])[label].\
                        sum().rename(f1+"_"+f2+"_"+label+"_sum").reset_index()
                    print("start merge")
                    test = test.merge(right=label_rate, how="left", on=[f1, f2])
                    print(test.shape)
                    test = test.merge(right=label_sum, how="left", on=[f1, f2])
                    print(test.shape)
                feature_num = train.groupby([f1, f2])[label]\
                    .count().rename(f1+"_"+f2+"_count").reset_index()

                test = test.merge(right=feature_num, how="left", on=[f1, f2])
                print(test.head(1))
                print("check null number")
                print(np.sum(test.isnull())/test.shape[0])

        test.fillna(0, inplace=True)
        test.to_csv(Config["save_all_data_path"]+str(count), index=False)


def g_test_two(train, test):
    vector_f = ["uid", "user_city", "item_id", "author_id", "item_city",
                "channel", "music_id", "device", "duration_time"]
    for i in range(len(vector_f)):
        print("first_order_feature: " + vector_f[i])
        for label in ["finish", "like"]:
            f = vector_f[i]
            label_rate = train.groupby(f)[label].mean().rename(f + "_" + label + "_rate").reset_index()  # 转化率
            label_sum = train.groupby(f)[label].sum().rename(f + "_" + label + "_num").reset_index()  # 正样本个数
            test = test.merge(right=label_rate, how="left", left_on=f, right_on=f)
            test = test.merge(right=label_sum, how="left", left_on=f, right_on=f)

        feature_num = train.groupby(f)[label].count().rename(f + "_num").reset_index()
        test = test.merge(right=feature_num, how="left", left_on=f, right_on=f)

        print("second_order_feature")
        for j in range(i + 1, len(vector_f)):
            f1 = vector_f[i]
            f2 = vector_f[j]
            print("start: " + f1 + "_" + f2)
            for label in ["finish", "like"]:
                label_rate = train.groupby([f1, f2])[label]. \
                    mean().rename(f1 + "_" + f2 + "_" + label + "_rate").reset_index()
                label_sum = train.groupby([f1, f2])[label]. \
                    sum().rename(f1 + "_" + f2 + "_" + label + "_sum").reset_index()
                print("start merge")
                test = test.merge(right=label_rate, how="left", on=[f1, f2])
                print(test.shape)
                test = test.merge(right=label_sum, how="left", on=[f1, f2])
                print(test.shape)
            feature_num = train.groupby([f1, f2])[label] \
                .count().rename(f1 + "_" + f2 + "_count").reset_index()

            test = test.merge(right=feature_num, how="left", on=[f1, f2])
            print(test.head(1))
            print("check null number")
            print(np.sum(test.isnull()) / test.shape[0])

    test.fillna(0, inplace=True)
    test.to_csv(Config["save_test_path"], index=False)


def get_feature():
    '''
    :param train: can be train.csv or all_data.csv
    :param test: can be val.csv or test.csv
    (train.csv, val_csv), (all_data.csv, test.csv)
    :return:
    '''
    print("start reading data")
    columns = ["uid", "user_city", "item_id", "author_id", "item_city",
               "channel", "music_id", "device", "duration_time", "finish", "like"]
    data = pd.read_csv(Config["all_data_path"])
    data = data[columns]
    test = pd.read_csv(Config["test_path"])
    test = test[columns]

    print("finish reading data")

    print("start feature extraction")

    g_train(data)
    print("finish train data")
    g_test_two(data, test)
    print("finish test data")


def collect_train_val_split():
    '''
    查看样本有多大，才决定是否合并all_data的所有分片
    :return:
    '''
    data = pd.read_csv(Config["save_all_data_path"])
    L = data.shape[0]
    train = data[:int(0.8*L)]
    val = data[int(0.8*L):]
    train.to_csv(Config["save_train_path"], index=False)
    val.to_csv(Config["save_test_path"], index=False)


def g_face_data():
    '''
    item_id	male_perc	female_perc	faces	maleBeauty	femaleBeauty	faceSquare	male_num	femalie_num
    to json
    :return:
    '''
    face_data = pd.read_csv(Config["raw_face_data_path"])
    # fill mean value with zero
    def m(x):
        if x["faces"] == 0:
            x["maleBeauty"] = 0
            x["femaleBeauty"] = 0
        else:
            pass
        return x

    face_data = face_data.apply(m, 1)
    face_data["male_num"] = face_data.male_perc * face_data.faces
    face_data["female_num"] = face_data.female_perc * face_data.faces
    face_data.male_num = face_data.male_num.apply(lambda x: round(x))
    face_data.female_num = face_data.female_num.apply(lambda x: round(x))

    # cut value
    # male_perc
    def cut_value(data):
        for col in ["male_perc", "female_perc", "maleBeauty", "femaleBeauty", "faceSquare"]:
            mask = data[col] == 0
            t = pd.cut(np.log(data[col] + 1), bins=100, labels=np.arange(100) + 1).astype(int)
            t[mask] = 0
            data[col] = t
        return data

    face_data = cut_value(face_data)
    le = LabelEncoder()
    face_data["male_num"] = le.fit_transform(face_data["male_num"].astype(int))
    le = LabelEncoder()
    face_data["female_num"] = le.fit_transform(face_data["female_num"].astype(int))
    le = LabelEncoder()
    face_data["faces"] = le.fit_transform(face_data["faces"].astype(int))
    print(face_data.head())
    print(face_data.columns)
    print(face_data.nunique())
    # face_data.to_csv("test.csv", index=False)

    # face_data.to_csv(Config["face_data_path"], index=False)
    big_dict = {}
    for i in face_data.values:
        big_dict[int(float(i[0]))] = list(i[1:])
    with open(Config["face_data_path"], "w") as f:
        json.dump(big_dict, f)
    print("finish generate face data")
    for i in big_dict:
        print(big_dict[i])
        break


def g_title_data(column_l=10):
    '''
    一共有134409 + 2个词
    item_id
    title_length
    word_0
    word_1
    word_2
    word_3
    word_4
    word_5
    word_6
    word_7
    word_8
    word_9
    to json
    :param column_l:
    :return:
    '''
    # extract title data
    title = []
    with open(Config["raw_title_data_path"]) as f:
        for i in f:
            # print (i)
            a = ast.literal_eval(i)
            # print (a)
            title.append(a)
    print("title num: ", len(title))
    # word frequenty
    word = {}
    for i in title:
        for key in i["title_features"].keys():
            if key in word:
                word[key] += i["title_features"][key]
            else:
                word[key] = i["title_features"][key]
    # remove word which frequently appearance
    word_data = pd.DataFrame.from_dict(word, orient="index").reset_index()
    word_data.columns = ["word_id", "word_num"]
    useful_word = set(word_data[word_data.word_num < word_data.word_num.quantile(0.999)].word_id.values)

    # 提取前30个词保存为dataframe
    data_c = np.zeros((len(title), column_l+2))
    for i, v in enumerate(title):
        data_c[i, 0] = v["item_id"]
        data_c[i, 1] = sum(v["title_features"].values())
        c = 2
        for j in v["title_features"].keys():
            if not j in useful_word:
                continue
            if c > column_l + 1:
                break
            for z in range(v["title_features"][j]):
                if c > column_l + 1:
                    break
                data_c[i, c] = int(j)
                c += 1
    columns = ["item_id", "title_length"]
    columns.extend(["word_" + str(i) for i in range(column_l)])
    title_data = pd.DataFrame(data_c, columns=columns).astype(int)
    # label encoder
    le = LabelEncoder()
    title_data["title_length"] = le.fit_transform(title_data["title_length"].astype(int))

    print(title_data.shape)
    print(title_data.head(2))
    print(title_data.nunique())
    # title_data.to_csv(Config["title_data_path"], index=False)
    # save to json
    big_dict = {}
    for i in title_data.values:
        big_dict[str(int(float(i[0])))] = [int(j) for j in i[1:]] # list(i[1:])
    with open(Config["title_data_path"], "w") as f:
        json.dump(big_dict, f)
    for i in big_dict:
        print(big_dict[i])
        break


def g_vedio():
    '''
    to json
    item_id, video_feature_dim_128
    {"item_id_int":list_dim_128_float(a list not numpy array),
    1:[1.2,3.43 ... ]
    }
    :return:
    '''
    big_dict = {}
    print("start video reading")
    with open(Config["raw_video_data_path"]) as f:
        for i in f:
            a = ast.literal_eval(i)
            big_dict[a["item_id"]] = a["video_feature_dim_128"]
    print("finish video reading")
    with open(Config["video_data_path"], "w") as jj:
        json.dump(big_dict, jj)
    print("finish video saving")


def g_audio():
    '''
    to json
    item_id, video_feature_dim_128
    {"item_id_int":list_dim_128_float(a list not numpy array),
    1:[1.2,3.43 ... ]
    }
    :return:
    '''
    big_dict = {}
    print("start audio reading")
    with open(Config["raw_audio_data_path"]) as f:
        for i in f:
            a = ast.literal_eval(i)
            big_dict[a["item_id"]] = a["audio_feature_128_dim"]
    print("finish audio reading")
    with open(Config["audio_data_path"], "w") as jj:
        json.dump(big_dict, jj)
    print("finish audio saving")

# 生成train,test,val,all_data作为deepFM等等的输入，只有9个特征
# g_deep()

# 生成一阶和二阶的特征来作为lgb的训练
# get_feature()

# 将生成的all_data_lgb进行train和val的切分
# collect_train_val_split()

# face_data生成
# g_face_data()

# title data生成
# g_title_data()

# video data 生成
# g_vedio()

# audio data生成
# g_audio()