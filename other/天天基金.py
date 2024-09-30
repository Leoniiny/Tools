# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：天天基金
import re
import requests
from do_document import *

class TTJJ:
    def __init__(self):
        self.session = requests.session()

    def get_fund_list(self,fcodes:str="161725,005827,512680,000831"):
        url = "https://api.fund.eastmoney.com/favor/GetFundsInfo?"
        payload = {
            "fcodes":fcodes
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'qgqp_b_id=facbde272f4ac99dca61167a28351d79; st_si=72163862105801; st_pvi=53746786368731; st_sp=2024-09-30%2016%3A16%3A52; st_inirUrl=; st_sn=1; st_psi=20240930161651785-119146300572-6044008178; st_asi=delete',
            'Referer': 'https://favor.fund.eastmoney.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
        }
        resp = self.session.post(url, headers=headers, data=payload)
        data = resp.text
        data_str = re.findall("\[(.*?)\]",data)
        for item in range(len(data_str)):
            print(f"这是第{item+1}行数据\n",data_str[item])

        # print(len(data_str))

    def query_fund(self, key = "广发中证军工"):
        url = "https://fundsuggest.eastmoney.com/FundSearch/api/FundSearchAPI.ashx"
        data = {
                      "callback":" jQuery18309554697902459091_1727685741784",
                    "m":" 9",
                    "key":key,
                    "_":" 1727686240506",
        }
        headers = {
            'Cookie': 'qgqp_b_id=facbde272f4ac99dca61167a28351d79; st_si=72163862105801; st_asi=delete; st_pvi=53746786368731; st_sp=2024-09-30%2016%3A16%3A52; st_inirUrl=https%3A%2F%2Ffavor.fund.eastmoney.com%2F; st_sn=4; st_psi=20240930164221635-119146300572-2930904928',
            'Referer': 'https://favor.fund.eastmoney.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
        }
        response = self.session.post(url, headers=headers, data=data)
        print(response.text)


if __name__ == '__main__':
    ttjj = TTJJ()
    ttjj.get_fund_list()

