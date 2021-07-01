import lightgbm as lgb
from config import Config
import pandas as pd
import pickle
import json
import numpy as np


def merge_all_train():
    start = int(input("start: "))
    end = int(input("end: "))
    for i in range(start, end+1):
        path = Config["save_all_data_path"] + str(i)
        data = pd.read_csv(path)

        print("reading title data")
        # title data
        with open(Config["title_data_path"], "r") as f:
            title = json.load(f)
        title = pd.DataFrame.from_dict(title, orient='index')
        title.reset_index(inplace=True)
        print(title.shape)
        columns = ["item_id", "title_length"]
        columns.extend(["word_" + str(i) for i in range(10)])
        print(len(columns))
        title.columns = columns
        title = title.astype(int)

        # merge, fill and delete
        data = data.merge(title, on="item_id", how="left")
        print(data.head())
        print(np.sum(data[columns].isnull()))
        print(data.shape)
        data.fillna(0, inplace=True)
        del title
        print("finish title")

        print("reading face data")
        with open(Config["face_data_path"], "r") as f:
            face = json.load(f)
        face = pd.DataFrame.from_dict(face, orient='index')
        face.reset_index(inplace=True)
        print(face.shape)
        columns = ["item_id", "male_perc","female_perc","faces","maleBeauty","femaleBeauty","faceSquare", "male_num", "femalie_num"]
        print(len(columns))
        face.columns = columns
        face = face.astype(int)

        # merge, fill and delete
        data = data.merge(face, on="item_id", how="left")
        print(data.head())
        print( np.sum(data[columns].isnull()))
        print(data.shape)
        data.fillna(0, inplace=True)
        del face
        print("finish face")

        print("reading video data")
        with open(Config["video_data_path"], "r") as f:
            video = json.load(f)
        video = pd.DataFrame.from_dict(video, orient='index')
        video.reset_index(inplace=True)
        columns = ["item_id"]
        columns.extend(["video_"+str(i) for i in range(128)])
        video.columns = columns
        video["item_id"] = video["item_id"].astype(int)

        # merge, fill and delete
        data = data.merge(video, on="item_id", how="left")
        print(data.head())
        print(np.sum(data[columns].isnull()))
        print(data.shape)
        data.fillna(0, inplace=True)
        del video
        print("finish video")

        print("reading audio data")
        with open(Config["audio_data_path"], "r") as f:
            audio = json.load(f)
        audio = pd.DataFrame.from_dict(audio, orient='index')
        audio.reset_index(inplace=True)
        columns = ["item_id"]
        columns.extend(["audio_"+str(i) for i in range(128)])
        audio.columns = columns
        audio["item_id"] = audio["item_id"].astype(int)

        # merge, fill and delete
        data = data.merge(audio, on="item_id", how="left")
        print(data.head())
        print( np.sum(data[columns].isnull()))
        print(data.shape)
        data.fillna(0, inplace=True)
        del audio
        print("finish aduio")

        print("saving data")
        data.to_csv(Config["big_data_all_feature_path"]+str(i))
        print("finish saving data")


def merge_all_test():
    path = Config["save_test_path"]
    data = pd.read_csv(path)

    print("reading title data")
    # title data
    with open(Config["title_data_path"], "r") as f:
        title = json.load(f)
    title = pd.DataFrame.from_dict(title, orient='index')
    title.reset_index(inplace=True)
    print(title.shape)
    columns = ["item_id", "title_length"]
    columns.extend(["word_" + str(i) for i in range(10)])
    print(len(columns))
    title.columns = columns
    title = title.astype(int)

    # merge, fill and delete
    data = data.merge(title, on="item_id", how="left")
    print(data.head())
    print(np.sum(data[columns].isnull()))
    print(data.shape)
    data.fillna(0, inplace=True)
    del title
    print("finish title")

    print("reading face data")
    with open(Config["face_data_path"], "r") as f:
        face = json.load(f)
    face = pd.DataFrame.from_dict(face, orient='index')
    face.reset_index(inplace=True)
    print(face.shape)
    columns = ["item_id", "male_perc", "female_perc", "faces", "maleBeauty", "femaleBeauty", "faceSquare", "male_num",
               "femalie_num"]
    print(len(columns))
    face.columns = columns
    face = face.astype(int)

    # merge, fill and delete
    data = data.merge(face, on="item_id", how="left")
    print(data.head())
    print(np.sum(data[columns].isnull()))
    print(data.shape)
    data.fillna(0, inplace=True)
    del face
    print("finish face")

    print("reading video data")
    with open(Config["video_data_path"], "r") as f:
        video = json.load(f)
    video = pd.DataFrame.from_dict(video, orient='index')
    video.reset_index(inplace=True)
    columns = ["item_id"]
    columns.extend(["video_" + str(i) for i in range(128)])
    video.columns = columns
    video["item_id"] = video["item_id"].astype(int)

    # merge, fill and delete
    data = data.merge(video, on="item_id", how="left")
    print(data.head())
    print(np.sum(data[columns].isnull()))
    print(data.shape)
    data.fillna(0, inplace=True)
    del video
    print("finish video")

    print("reading audio data")
    with open(Config["audio_data_path"], "r") as f:
        audio = json.load(f)
    audio = pd.DataFrame.from_dict(audio, orient='index')
    audio.reset_index(inplace=True)
    columns = ["item_id"]
    columns.extend(["audio_" + str(i) for i in range(128)])
    audio.columns = columns
    audio["item_id"] = audio["item_id"].astype(int)

    # merge, fill and delete
    data = data.merge(audio, on="item_id", how="left")
    print(data.head())
    print(np.sum(data[columns].isnull()))
    print(data.shape)
    data.fillna(0, inplace=True)
    del audio
    print("finish aduio")

    print("saving data")
    data.to_csv(Config["big_test_all_feature_path"])
    print("finish saving test")

