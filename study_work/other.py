# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(nums[:3])  # [0, 0, 1]
for i in s:
    nums.append(i)
    print(nums)