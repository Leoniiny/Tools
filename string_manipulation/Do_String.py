# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import json


class Do_String:
    def __init__(self):
        pass

    # 将curl中参数字符串转字典
    def translate_str_to_dic(self, string: str):
        str_list = string.split("&")
        params_dic = {}
        for temp_str in str_list:
            temp_list = temp_str.split("=")
            params_dic[temp_list[0]] = temp_list[-1]
        params_str = json.dumps(params_dic)
        return params_str


if __name__ == '__main__':
    obj = Do_String()
    print(obj.translate_str_to_dic("a=1&b=2&c=3"))