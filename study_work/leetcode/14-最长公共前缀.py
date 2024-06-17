# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
'''
什么是前缀：字符串的前缀是指不包含最后一个字符的所有以第一个字符（索引为0）开头的连续子串

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''''

# 思路：找出数组中最短和最长的字符串--》》》['aa','bb','bc','ee'] 这种形式的行不通
# class Solution:
#     def longestCommonPrefix(self, strs: list) -> str:
#         string0 = min(strs)
#         string1 = min(strs)
#         for i in range(len(string0)):
#             if string0[i] != string1[i]:
#                 return string0[:i]
#         return string0

# 优化1：解决长度一样的字符串
class Solution1:
    def longestCommonPrefix(self, strs: list):
        min_len = min(len(i) for i in strs)
        rest = ''
        for i in range(min_len):
            if len(set(s[i] for s in strs)) >1:
                break
            rest += strs[0][i]
        return rest


# 优化2：采用zip+set 的方法进行
class Solution2:
    def longestCommonPrefix(self, strs: list):
        rest = ''
        for i in list(zip(*strs)):  # zip 组成的元组会以最短的迭代对象为准。(("a","b","b","e"),("a","b","c","e"))
            print(f"i 的值为{i}")
            if len(set(i)) == 1:    # 说明该组元素相同
                print(len(set(i)) )
                rest += i[0]
            else:
                break
        return rest


if __name__ == '__main__':
    obj = Solution2()
    rest = obj.longestCommonPrefix(['12aabbb','123bbbbb','123bcbb','123eebb'])
    print(f"rest 的值为：{rest}")