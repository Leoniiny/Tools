# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function： 分糖果

class Solution1133:
    def distributeCandies(self, candies: int, num_people: int):
        ans=[0]*num_people
        i = 0
        while candies:
            ans[i % num_people] += min(candies, i + 1)
            candies -= min(candies, i + 1)
            i += 1
        return ans