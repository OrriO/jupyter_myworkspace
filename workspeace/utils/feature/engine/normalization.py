#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
normalization.py -- a kind of feature engine 
Author: wanglei <wanglei8@guahao.com>
Create on 2020-01-20.
"""

from utils.feature.engine import FeatureEngine


class MinMaxScaler(FeatureEngine):

    """
    MinMaxScaler 特征处理  
    MinMaxScaler的含义和使用方式，参考：
    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler    
    """

    multi_field = (list,)

    def __init__(self, column_name, **kargs):
        super(MinMaxScaler, self).__init__(column_name)
        self._min_value = kargs.get('min_value', 0)
        self._max_value = kargs.get('max_value', 100)
        self._unknow = kargs.get('unknow', -99)
        assert self._min_value < self._max_value, "上限[%s]下限[%s]设置不合理" %(self._min_value, self._max_value)

    def transform(self, y):
        if isinstance(y, self.multi_field):
            multi_value = []
            for value in y:
                multi_value.append(self._transform(y))
            return multi_value

        if isinstance(y, self.singel_field):
            return self._transform(y)

        return self._unknow

    def _transform(self, y):
        if not isinstance(y, self.value_type):
            self._log.warn("The value type is wrong, please converte to %s before transform" % (
                " or ".join([x.__name__ for x in self.value_type])))
            return self._unknow

        if y < self._min_value or y > self._max_value:
            self._log.warn("The value exceed value range (%s -> %s)" %
                           (self._min_value, self._max_value))

        return (y-self._min_value)*1.0/(self._max_value-self._min_value)
