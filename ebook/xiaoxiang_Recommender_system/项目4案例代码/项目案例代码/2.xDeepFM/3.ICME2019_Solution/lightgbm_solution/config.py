Config = {
        "model_name": "lgb",
        "large_file": False,
        'use_cuda': False,
        'device_id': 0,
        "num_workers": 8,
        'pretrain': False,
        "model_path_all_views": '../../cache/track2/checkpoints/lgb_all_views.model',
        "model_path_media": "../../cache/track2/checkpoints/lgb_media.model",
        "train_path": "../../cache/track2/tmp/train.csv",  # or ../../data/track2/final_track2_train.txt # train + val
        "val_path": "../../cache/track2/tmp/val.csv",
        "test_path": "../../cache/track2/tmp/test.csv",
        "all_data_path": "../../cache/track2/tmp/all_data.csv",
        "raw_data_path": "../../data/track2/final_track2_train.txt",
        "predict_file": "../../cache/track2/result/result.csv",
        # for lgb
        "save_test_path": "../../cache/track2/tmp/test_lgb.csv",
        "save_all_data_path": "../../cache/track2/tmp/all_data_lgb.csv",
        # title data
        "raw_title_data_path": "../../data/track2/track2_title.txt",
        "title_data_path": "../../cache/track2/tmp/title_data.json",
        # face data
        "raw_face_data_path": "../../cache/track2/tmp/track2_face_attrs_fill.csv",
        "face_data_path": "../../cache/track2/tmp/face_data.json",
        # video data
        "raw_video_data_path": "../../data/track2/track2_video_features.txt",
        "video_data_path": "../../cache/track2/tmp/video_data.json",
        # audio data
        "raw_audio_data_path": "../../data/track2/track2_audio_features.txt",
        "audio_data_path": "../../cache/track2/tmp/audio_data.json",
        # lgb all feature big data
        "big_data_all_feature_path": "../../cache/track2/tmp/big_data_all_feature.csv",
        "big_test_all_feature_path": "../../cache/track2/tmp/big_test_all_feature.csv"
    }
normal_config = {
    # interaction
    # behaviour
    'uid': 73974,
    'user_city': 397,
    'item_id': 4122689,
    'author_id': 850308,
    'item_city': 462,
    'channel': 5,
    'music_id': 89779,
    'device': 75085,
    "duration_time": 641,
    # not interaction
    # title length
    "title_length": 67 + 2,
    # face
    "male_perc": 100 + 2,
    "female_perc": 100 + 2,
    "faces": 91 + 2,
    "maleBeauty": 100 + 2,
    "femaleBeauty": 100 + 2,
    "faceSquare": 100 + 2,
    "male_num": 43 + 2,
    "female_num":73 + 2,
    # title embedding
    "title": 134409 + 2
}