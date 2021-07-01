#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
preprocess.py -- a kind of feature engine 
Author: wanglei <wanglei8@guahao.com> 
Create on 2020-02-04.
"""

from utils.feature.engine import FeatureEngine


class MultiValueGenerator(FeatureEngine):

    """
    MultiValueGenerator 处理多值字段,默认使用","做分割
    """

    value_type = (str, unicode)

    def __init__(self, column_name, **kargs):
        super(MultiValueGenerator, self).__init__(column_name)
        self._sep = kargs.get('sep', ',')
        assert isinstance(self._sep, self.value_type), "分隔符必须为字符串类型" 

    def transform(self, y):
        """
        特征转换入口，y代表需要转换的值
        """
        if not isinstance(y, self.value_type):
            self._log.warn("The value type is wrong, please converte to %s before transform" % (
                " or ".join([x.__name__ for x in self.value_type])))
            return y

        if self._sep not in y:
            self._log.warn("seperator [%s] not in [%s]" %
                           (self._sep, y))
        return y.split(self._sep)
