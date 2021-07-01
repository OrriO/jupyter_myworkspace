#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
encode.py -- a kind of feature engine 
Author: wanglei <wanglei8@guahao.com>
Create on 2020-01-20.
"""

from utils.feature.engine import FeatureEngine



class LabelEncoder(FeatureEngine):

    """
    LabelEncoder 特征处理  
    LabelEncoder的含义和使用方式，参考：
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder
    """
    multi_field = (list,)
    singel_field = (str, int, float)

    def __init__(self, column_name, **kargs):
        super(LabelEncoder, self).__init__(column_name)
        self._encoder_table = kargs.get('encoder_table', {})
        self._unknow = kargs.get('unknow', -99)
        assert isinstance(self._encoder_table, dict),"encoder_table必须为字典"
        assert isinstance(self._unknow, (int, float,)),"默认填充必须为数值型"

    def transform(self, y):
        """
        特征转换入口，y代表需要转换的值
        """
        if isinstance(y, self.multi_field):
            multi_value = []
            for value in y:
                multi_value.append(self._transform(value))
            return multi_value

        if isinstance(y, self.singel_field):
            return self._transform(y)

        return self._unknow

    def _transform(self, y):
        """
        处理单个特征
        """
        feature_code = self._encoder_table.get(y)
        if feature_code is not None:
            return feature_code
        else:
            self._log.warn("[%s] not featured in column [%s] and using [%s] for default" %
                           (y, self._column_name, self._unknow))
            return self._unknow
