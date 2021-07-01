#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
feature.py -- main entrance of feature  
Author: wanglei <wanglei8@guahao.com>
Create on 2020-01-20.
"""
from utils.feature.common import get_feature_classes
import yaml
from copy import copy
import collections
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

class FeatureEngineering:
    """
    特征工程程序的入口  
    调用方法：
        fe = FeatureEngineering()
        fe.init()
        print fe.handle('constellation_name',u'金牛座')
        fe.close()
    """

    def init(self, yamls,file_path=None):
        """
        FeatureEngineering 初始化入口，主要功能：
            从数据库或者yaml加载特征和特征处理方式
            构建特征处理引擎
        """
        self._engine = collections.defaultdict(list)
        self._load_feature_data(yamls,file_path)
        self._create_engine()

    def _load_feature_data(self, yamls, file_path=None):
        self._dict_info = {}
        for yl in yamls:
            if file_path:
                yaml_dir = os.path.join(file_path, 'yamls', yl)
            else:
                yaml_dir = os.path.join(base_dir, 'yamls', yl)
            yaml_file = open(yaml_dir, 'r').read()
            _yl = yaml.load(yaml_file)
            feature_column = _yl['feature_column']
            self._dict_info.update(feature_column)

    def _create_engine(self):
        feature_classes = get_feature_classes()
        for k, vs in self._dict_info.items():
            for _v in vs:
                class_name = _v.pop('engine')
                # 引擎初始化
                tmp_engine = feature_classes[class_name](
                    k, **_v)
                self._engine[k].append(tmp_engine)

    def handle(self, k, v):
        """
        用作特征处理，其中参数的含义：
            k:需要处理的字段
            v:字段的值
        """
        return self._handle(k, v)

    def _handle(self, k, v):
        tmp_v = copy(v)
        for engine in self._engine[k]:
            tmp_v = engine.transform(tmp_v)
        return tmp_v

    def close(self):
        """
        用来关闭数据库链接和之前占用的内存
        """
        del self._engine
        del self._dict_info


if __name__ == '__main__':
    yamls = ['user_base.yaml']

    fe = FeatureEngineering()
    fe.init(yamls)
    print (fe.handle('constellation_name', u'金牛座'))
    fe.close()
