class Solution:
    def isPalindrome(self,x:int) -> bool:
        i = x
        s = ''
        if x<0:
            return False
        while i >=10:
            s += str(i%10)
            i=i//10
        s+=str(i)
        return int(s)==x

a = Solution
b = a.isPalindrome(a,10)
print(b)