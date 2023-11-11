# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：测试微信轰炸
from pynput.keyboard import Key,Controller
import time


keyboard = Controller()
text = input("请输入内容：")
run_num = eval(input("循环次数："))

time.sleep(1)
for i in range(3):
    print(f"距离轰炸还有{3-i}秒")
    time.sleep(1)

for i in range(run_num):
    keyboard.type(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
print("循环结束")

