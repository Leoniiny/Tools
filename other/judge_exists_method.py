# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：judge_exists_method.py
def run_if_exists(obj,moudle_name='test'):
    """
    判断某个类中是否存在某个方法、属性
    :param obj: 某个类实例化的对象
    :param moudle_name: 方法名
    :return:
    """
    if hasattr(obj, moudle_name):
        get_method = getattr(obj, moudle_name)
        print(f"调用 moudle_name 方法: {get_method}")
        if callable(get_method):
            return get_method()
    return False




