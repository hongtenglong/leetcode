from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        s = strs[0]
        for l in strs:
            if(len(s)>len(l)):
                s = l
        if(len(s)==0):
            return ''
        for i in range(0,len(s)):
            for l in strs:
                if(l[i]!=s[i]):
                    return s[0:i]
        return s



a = Solution
r = a.longestCommonPrefix(a,["ab","a"])
print(r)