
import urllib,time
import requests, re, os
from urllib.parse import urlencode

img_path = r"save_img"
Total = 0
img_list = []


class GetImg:
    def __init__(self,word="水瓶",queryWord="水瓶",num=1):
        self.session = requests.session()
        self.url = "https://image.baidu.com/search/acjson"
        self.method = "get"
        self.params = urlencode(
            {
                "tn": "resulttagjson",
                "logid": "10977334522187396509",
                "ie": "utf-8",
                "fr": "",
                "word": word,
                "ipn": "r",
                "fm": "index",
                "pos": "history",
                "queryWord": queryWord,
                "cl": "2",
                "lm": "-1",
                "oe": "utf-8",
                "adpicid": "",
                "st": "-1",
                "z": "",
                "ic": "",
                "hd": "",
                "latest": "",
                "copyright": "",
                "s": "",
                "se": "",
                "tab": "",
                "width": "",
                "height": "",
                "face": "0",
                "istype": "2",
                "qc": "",
                "nc": "1",
                "expermode": "",
                "nojc": "",
                "isAsync": "true",
                "pn": str(num*30),
                "rn": "30",
                "itg": "1",
                "gsm": "3c",
                "1697012883685": ""
            }
        )
        self.data = None
        self.headers = {
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'BIDUPSID=954506F70474D51E04FBF35BC4FC1C36; PSTM=1694333035; BAIDUID=954506F70474D51EBA66011E7EFAA387:FG=1; newlogin=1; BDSFRCVID=V0AOJeC62wVigTJqKj_GU1Q38Z2WL5vTH6aoi26jbPJsYBZ3MSN0EG0PnU8g0KFMNXNrogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJIjVC05tK83qb8kK4oj5JK_-U702t_XKKOLVh6dtp7keq8CDl6NWfcBKlQiafn8QR6IoKnEMl6WVbr2y5jHhnITMJ5iQtADHmT-LCJaMtTpsIJMWh_WbT8U5fKL0fADaKviaMnjBMb1fIJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe633DH_fJ5FJf5vfL5r_2Rr0jb7GKPnt5KCHbq8sLjOCB2Q-5KL-bMQEeUb_KfR8BU-ADJLeqpIHQ2ttLfbdJJjojD_CM45myRt4LRCeWlJwtgTxoUJ8QCnJhhvDXfTiXRDebPRiXPb9QgbfopQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjAWDTjP; BAIDUID_BFESS=954506F70474D51EBA66011E7EFAA387:FG=1; BDSFRCVID_BFESS=V0AOJeC62wVigTJqKj_GU1Q38Z2WL5vTH6aoi26jbPJsYBZ3MSN0EG0PnU8g0KFMNXNrogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJIjVC05tK83qb8kK4oj5JK_-U702t_XKKOLVh6dtp7keq8CDl6NWfcBKlQiafn8QR6IoKnEMl6WVbr2y5jHhnITMJ5iQtADHmT-LCJaMtTpsIJMWh_WbT8U5fKL0fADaKviaMnjBMb1fIJDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe633DH_fJ5FJf5vfL5r_2Rr0jb7GKPnt5KCHbq8sLjOCB2Q-5KL-bMQEeUb_KfR8BU-ADJLeqpIHQ2ttLfbdJJjojD_CM45myRt4LRCeWlJwtgTxoUJ8QCnJhhvDXfTiXRDebPRiXPb9QgbfopQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjAWDTjP; delPer=0; PSINO=7; BDRCVFR[C5g0hgaJYCf]=DQipRF3PU9bmhFhuMT8mvqV; BA_HECTOR=ah80252l0k80a4248h8l20211iic4rl1o; ZFY=p:BLTSBg8kwRI7Q36tjBoLxnhT8IytFTO6K:B15Zw1Igs:C; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_MzM0OWRjZGJmMzMzMzkwMWU2MTlmOWRjZmE4MjVlM2RiMzMwNjU3N2U2ZmEwZjhhNmRjNjIxOGJlMjUzYjhiYTA1YTRhMGU3MWZhMzdkNGM0MmQyODU2ZjRlODg4ZDMyNWNiOTVjM2I4ZmU5ZDc5MjkxMzUwZTM5NDM3Y2Q4ZmY5ZmRlYWQ3MTAzMjZiMmMzZGM5YzUxY2YzMzAyZWE4MA==; indexPageSugList=%5B%22%E6%B0%B4%E7%93%B6%22%5D; cleanHistoryStatus=0; BAIDUID=C42140B8515D546DCEB2A1D94DCD7750:FG=1; BAIDUID_BFESS=C42140B8515D546DF5064D82380C298A:FG=1; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BIDUPSID=C42140B8515D546DF5064D82380C298A',
            'Pragma': 'no-cache',
            'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1696995553038_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MTEsMCw2LDQsMywxLDUsOCwyLDcsOQ%3D%3D&ie=utf-8&sid=&word=%E6%B0%B4%E7%93%B6',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        self.resp = None

    def send_request(self,**kwargs):
        if kwargs.get('url') is None:
            kwargs['url'] = self.url
        if kwargs.get('method') is None:
            kwargs['method'] = self.method
        if kwargs.get('headers') is None:
            kwargs['headers'] = self.headers
        if kwargs.get('params') is None:
            kwargs['params'] = self.params
        if kwargs.get('data') is None:
            kwargs['data'] = self.data
        self.resp = self.session.request(**kwargs)
        return self.resp

    def deal_pic(self,resp=None):
        img_list = []
        if resp is None:
            resp = self.resp
        pic_url_list = re.findall('src=(.*?)&', resp.text)
        # 去重
        pic_url_list = list(set(pic_url_list))
        if len(pic_url_list) == 0:
          print("没有获取到图片")
        else:
          for i in range(len(pic_url_list)):
            pic_url = pic_url_list[i]
            new_pic_url = urllib.parse.unquote(pic_url)
            if "alicdn" not in new_pic_url:
              img_list.append(new_pic_url)
        print(f"img_list 的值为：{img_list}")
        return img_list

    def save_img(self,img_path=r".\save_img",img_list =None,num=None):
        if not os.path.exists(img_path):
          os.mkdir(img_path)
        if num is None:
            num = 1
        for each in img_list:
            time.sleep(2)
            print(f"正在下载第 {num} 张图片，图片地址为{each}")
            try:
              if each is not None:
                pic = requests.get(each,timeout=7,allow_redirects=False)
              else:
                continue
            except BaseException:
              print("当前图片无法下载")
            else:
              if len(pic.content) < 200:
                continue
              string = img_path + rf"\p_{i}{num} .jpg"
              with open(string,"wb") as f:
                  f.write(pic.content)
                  num += 1


if __name__ == '__main__':
    for i in range(1,21):
        obj = GetImg(num=i)
        obj.send_request()
        pic_list = obj.deal_pic()
        obj.save_img(img_list = pic_list,num=i)

