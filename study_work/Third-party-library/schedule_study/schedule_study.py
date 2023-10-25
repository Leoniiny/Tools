# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：定时任务 schedule 三方库学习
import time
import schedule


def job():
    print("正在执行任务.....")


# 你能用day的地方一定能用days其他也一样
# 如果every()里面值不为1或者空时候必须用他复数


schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)   # 每分钟 的第17秒

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
