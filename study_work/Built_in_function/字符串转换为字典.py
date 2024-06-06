# @Time : 2023/3/20 0020 16:33
# @Author : 雷洋平
# @File : 字符串转换为字典.py
# @Software: PyCharm
# @Function:字符串转换为字典
import json


def translate_str_to_dic(string: str):
    str_list = string.split("&")
    params_dic = {}
    # print(f"str 的结果为{str_list}")
    for temp_str in str_list:
        temp_list = temp_str.split("=")
        params_dic[temp_list[0]] = temp_list[-1]
    params_str = json.dumps(params_dic)
    # print(f"params_dic  的结果为：{params_str},类型为：{type(params_str)}")
    return params_str


if __name__ == '__main__':
    pass
    str ='channelScene=0&operateFlag=0&channelType=0&configId=c87bdb244f5c491781c237d82996d582&id=de2ef2653a5b42939c0bd578b6652409&channelName=%E6%96%B0%E5%A2%9E%E6%A1%8C%E9%9D%A2%E7%BD%91%E7%AB%99-207&channelMark=&managerType=1&isTraceFlag=0'
    params_str = translate_str_to_dic(str)
    print(params_str)

