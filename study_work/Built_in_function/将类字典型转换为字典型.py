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
    robotFlag:-1
    questionTypeId:12e06ed0339244e5a754dcd32291366e
    oldRobotFlag:-1
    questionTitle:12321
    docLinkflag:0
    answerDesc:<p>123123</p>
    answerFlag:1
    answerTxt:123123
    answerSummary:123123
    auditStatus:2
    usedFlag:0
    effectTime:2023-10-16 00:00:00
    invalidTime:2023-10-16 23:59:59
    timeZone:Asia/Shanghai
    effectTimeAbs:1697385600
    invalidTimeAbs:1697471999
    linkUpdateFlag:0"""
    data = translate_data(string)
    print(data)