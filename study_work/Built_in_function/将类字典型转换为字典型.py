# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：将参数转换成字典
def translate_data(string:str):
    new_list = string.split()
    dic = {}
    for new_string in new_list:
        list1 = new_string.split(":")
        dic[list1[0]] = list1[-1]
    return dic


if __name__ == '__main__':
    string = """
robotFlag: -1
isInterCompany: 1
"""
    data = translate_data(string)
    print(data)