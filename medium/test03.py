class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.max = 0
        list=[]
        list[:0]=s
        print(list)

        for i in range(0,len(list)):
            for j in range(i+1,len(list)):
                if(list[i]!=list[j] and j==len(list)-1):
                    break


        return self.max
s = "abcbbc"
a = Solution
r = a.lengthOfLongestSubstring(a,s)
print(r)
# list=[]
# list[:0] = s
# print(s)
