# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：时间相关操作
import arrow,datetime
from datetime import datetime, timedelta


class DoDate:
    def __init__(self):
        self.utc = arrow.utcnow()  # 获取UTC时间

    # 获取某个时间段，并返回毫秒级时间戳。默认是最近7天
    def acquire_time_period(self,days=6):
        # 获取今天的日期
        today = datetime.now()

        # 最近7天的日期
        before_seven_date = today - timedelta(days=days)

        # 设置时间为当天零点
        before_seven_date = before_seven_date.replace(hour=0, minute=0, second=0, microsecond=0)

        # 设置时间为当天23点59分59秒
        end_of_day = today.replace(hour=23, minute=59, second=59, microsecond=0)

        # 转换为时间戳
        before_seven_date_timestamp = int(before_seven_date.timestamp() * 1000)
        end_of_day_timestamp = int(end_of_day.timestamp() * 1000)
        return before_seven_date_timestamp, end_of_day_timestamp

    # 获取当前时间，并返回格式化后的时间。格式：2024-08-24 03:26:00
    def get_date_format(self, format_num =1, formate ="YYYY-MM-DD",interval_format = None,interval_num = 1):
        if format_num == 2:
            formate = "YYYY-MM-DD HH"
        if format_num == 3:
            formate = "YYYY-MM-DD HH:mm"
        if format_num == 4:
            formate = "YYYY-MM-DD HH:mm:ss"
        if interval_format == "weeks":
            show_time = self.utc.shift(weeks = interval_num).format(f"{formate}")
        elif interval_format == "years":
            show_time = self.utc.shift(years = interval_num).format(f"{formate}")
        elif interval_format == "months":
            show_time = self.utc.shift(months = interval_num).format(f"{formate}")
        else:
            show_time = self.utc.shift(days = interval_num).format(f"{formate}")
        print(f"show_time 的值为：{show_time}")
        return show_time

if __name__ == '__main__':
    do_date = DoDate()
    print(do_date.get_date_format(format_num=4,interval_format="weeks",interval_num=1))