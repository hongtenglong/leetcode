'''
27. 移除元素
执行用时：48 ms, 在所有 Python3 提交中击败了12.82%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了39.44%的用户
'''
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = nums.count(val)
        for i in range(0,n):
            nums.remove(val)
        return len(nums)

a = Solution
l = [1,2,2,3,4,2]
v = 2
print(a.removeElement(a,l,v))
print(l)