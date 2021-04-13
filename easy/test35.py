'''
35. 搜索插入位置
执行用时：32 ms, 在所有 Python3 提交中击败了95.22%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了10.54%的用户
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(len(nums)==1):
            return 0 if nums[0]>=target else 1
        if(len(nums)==2):
            if nums[0]>=target:
                return 0
            elif nums[1]>=target:
                return 1

        l = 0
        r = len(nums)-1
        while l<r:
            re = nums[(l+r)//2]
            if(re == target):
                return (l+r)//2
            elif(r-l==1):
                if nums[l]>target:
                    return l-1 if l!=0 else 0
                elif nums[r]<target:
                    return r+1
                else:
                    return r
            elif(re>target):
                r=(r+l)//2
                m=r
            elif(re<target):
                l=(r+l)//2
                m=l
        return m

a = Solution
l = [1,3,5,6]
i = 0
print(a.searchInsert(a,l,i))