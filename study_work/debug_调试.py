# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：调试 教程
import time


def debug_study(m):
    time.sleep(0.5)
    print(f"m 的值是{m}")
    return m+1


for i in range(1,11):
    print(f"i 的值为{i}")
    result = debug_study(m=i)
    print(f"result 的值为{result}")
