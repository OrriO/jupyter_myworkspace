# coding: utf-8
"""
common.py -- load feature engine from file  
Author: wanglei <wanglei8@guahao.com>
Create on 2020-01-20.
"""

from importlib import import_module
from pkgutil import iter_modules
import inspect
import time
from utils.feature.engine import FeatureEngine

def walk_modules(path):
    mods = []
    mod = import_module(path)
    mods.append(mod)
    if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)
    return mods


def _iter_command_classes(module_name):
    """
        遍历所有存在的类，并判断是否继承了FeatureEngine
    """
    for module in walk_modules(module_name):
        for obj in vars(module).values():
            if inspect.isclass(obj) and \
                    issubclass(obj, FeatureEngine) and \
                    obj.__module__ == module.__name__ and \
                    not obj == FeatureEngine:
                yield obj


def _get_feature_from_module(module):
    """
        对所有合法的类，实例化
    """
    d = {}
    for cmd in _iter_command_classes(module):
        cmdname = cmd.__name__
        d[cmdname] = cmd
    return d


def get_feature_classes():
    """
        获取data_task.process下所有的继承了FeatureEngine类的方法
    """
    cmds = _get_feature_from_module('wylib.feature.engine')
    return cmds
