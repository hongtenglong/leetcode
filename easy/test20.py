'''
20. 有效的括号
执行用时：40 ms, 在所有 Python3 提交中击败了67.23%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了71.46%的用户
'''

class Solution:
    def isValid(self, s: str) -> bool:
        a = ('{','[','(')
        if(len(s)%2)==1 or s[0] not in a or s[-1] in a:
            return False
        m = {'{':'}','[':']','(':')'}
        l = []
        for i in s[0:]:
            if(i in ('{','[','(')):
                l.append(i)
            else:
                if(len(l)==0 or m.get(l.pop()) != i):
                    return False
        return len(l) ==0

a = Solution
r = a.isValid(a,'()))')
print(r)

# print('(){}[]'[1:])
