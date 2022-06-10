class Solution:
    def getMax(self, a:int, b:int) -> int:
        if a>b:
            return a
        return b
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
#         n=len(s)
#         if n==0:
#             return 0
#         if n==1:
#             return 1
        
#         lv={} #last visited
#         lols=[]
#         for i in range(n):
#             lv[s[i]]=-1
#             lols.append(1)
        
#         lv[s[0]] = 0
#         print('', end="  ")
#         for i in range(1,n):
#             if lv[s[i]] != -1:
#                 print('r', end=" ")
#                 lols[i] = lols[i-1]+1-lols[lv[s[i]]]
#                 # self.getMax(lols[i-1]+1-lols[lv[s[i]]], lols[i-1])
#                 lv[s[i]] = i
#             else:
#                 print('u', end=" ")
#                 lols[i] = lols[i-1]+1
#                 lv[s[i]] = i
        
#         print()
#         for i in range(n):
#             print(lols[i], end=" ")
#         return lols[n-1]