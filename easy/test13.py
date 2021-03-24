'''
13.罗马数字转整数
执行用时：52 ms, 在所有 Python3 提交中击败了82.64%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了48.60%的用户
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        r:int = 0
        i = 0
        while i < len(s):
            if(i < len(s)-1 and a.get(s[i]) < a.get(s[i+1])):
                r = r + a.get(s[i+1])-a.get(s[i])
                i = i+2
            else:
                r = r + a.get(s[i])
                i = i+1
        return r

a = Solution
print(a.romanToInt(a,"MCMXCIV"))