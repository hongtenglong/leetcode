'''
26. 删除有序数组中的重复项
执行用时：44 ms, 在所有 Python3 提交中击败了79.16%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了69.30%的用户
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)<=1):
            return len(nums)
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                r+=1
        return l+1
print(Solution.removeDuplicates(Solution,[1,2,2,3]))