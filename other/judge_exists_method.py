# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：judge_exists_method.py
def run_if_exists(obj,moudle_name='test'):  # 某个类实例化的对象
    if hasattr(obj, moudle_name):
        get_method = getattr(obj, moudle_name)
        print(f"调用 moudle_name 方法: {get_method}")
        if callable(get_method):
            return get_method()
    return False




