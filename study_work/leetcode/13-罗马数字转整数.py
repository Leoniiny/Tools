# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
class Solution:
    def romanToInt(self, s: str):
        rm_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rest = 0
        for i in range(len(s)-1):
            if rm_dic[s[i]]  < rm_dic[s[i+1]] :
                rest -=rm_dic[s[i]]
            else:
                rest += rm_dic[s[i]]
        rest += rm_dic[s[-1]]   # 最后一位罗马数字一定大于等于前一位数字
        return rest


if __name__ == '__main__':
    obj = Solution()
    print(obj.romanToInt("LVIII"))