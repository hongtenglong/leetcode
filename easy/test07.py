class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        self.r=''
        if(s[0]=='-'):
            self.r = '-'
            for i in range(len(s)-1,0,-1):
                self.r+=s[i]
        else:
            for i in range(len(s)-1,-1,-1):
                self.r+=s[i]
        r = int(self.r)
        return r if r <= 2147483647 and r >= -2147483648 else 0
a = Solution
i = 1534236469
print(a.reverse(a,i))