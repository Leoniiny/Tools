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
    # print(f"params_dic  的结果为：{params_dic}")
    params_str = json.dumps(params_dic)
    # print(f"params_dic  的结果为：{params_str},类型为：{type(params_str)}")
    return params_str


if __name__ == '__main__':
    pass
    str = "pageNo=1&pagerSize=15&keyFlag=1&orderType=1&questionTypeId=-1&typeShowFlag=0&usedFlag=0&robotFlag=-1&createTimeStartAbs=1696082400&createTimeEndAbs=1698757199&updateTimeStartAbs=1696082400&updateTimeEndAbs=1698757199&effectTimeStartAbs=1696082400&effectTimeEndAbs=1698757199&invalidTimeStartAbs=1696082400&invalidTimeEndAbs=1698757199&createStartTime=2023-10-01+00:00:00&createEndTime=2023-10-31+23:59:59&updateStartDate=2023-10-01+00:00:00&updateEndDate=2023-10-31+23:59:59&effectStartDate=2023-10-01+00:00:00&effectEndDate=2023-10-31+23:59:59&invalidStartDate=2023-10-01+00:00:00&invalidEndDate=2023-10-31+23:59:59&keyWordsArr=[]"
    params_str = translate_str_to_dic(str)
    print(params_str)

