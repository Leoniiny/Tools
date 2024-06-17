# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
"""
非严格递增排列指的是序列中的元素从小到大排列，但允许元素重复。这与严格递增序列不同，后者不仅要求元素递增，还不允许出现重复的数值。非严格递增序列允许序列中的数字在其周围有重复，例如序列(1,1,1,2,3,4,5,6,6,6,7,8,9)就是一个非严格递增序列的例子

"""

# class Solution:
#     def removeDuplicates(self, nums):
#         k =1
#         for i in range(1,len(nums)):
#             if nums[i-1] != nums[i]:
#                 nums[k] = nums[i]
#                 k +=1
#         return k


class Solution:
    def removeDuplicates(self, nums):
        print(set(nums))
        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)


if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,2,3,4,5,1,1,1,3]
    print(obj.removeDuplicates(nums))