# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import requests
from faker import Faker
fk = Faker(locale="zh_CN")

class GetToken:
    def __init__(self):
        pass

    def get_token(self):
        token = "token.123456&"+fk.ssn()
        # print(f"token的值是：%s "%token)
        return token


if __name__ == '__main__':
    obj = GetToken()
    obj.get_token()