#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
engine.py -- father of all feature tools 
Author: wanglei <wanglei8@guahao.com>
Create on 2020-01-20.
"""



class FeatureEngine(object):
    """

    """
    def __init__(self, column_name):
        self._column_name = column_name

    def transform(self, y):
        raise NotImplementedError
