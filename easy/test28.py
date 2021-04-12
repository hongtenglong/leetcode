'''
28. 实现 strStr()
执行用时：40 ms, 在所有 Python3 提交中击败了75.13%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了34.68%的用户
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='' or haystack==needle:
            return 0
        if(len(haystack)<len(needle)):
            return -1

        for i in range(0,len(haystack)-len(needle)+1):
            for j in range(0,len(needle)):
                    if(haystack[i+j]!=needle[j]):
                        break
                    elif(j==len(needle)-1):
                        return i
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        s = haystack.split(needle,1)
        return len(s[0]) if len(s[0])<len(haystack) else -1


a = Solution
haystack = "hello"
needle = "oa"
print(a.strStr(a,haystack,needle))