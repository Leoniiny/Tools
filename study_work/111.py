# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
str_list = ["d22og","racecar","car","raceca12312r","raceca12312r","racec12312ar","12311","racec232ar"]
min_len = min(len(i) for i in str_list)
print(min_len)
print(list(zip(*str_list)))

