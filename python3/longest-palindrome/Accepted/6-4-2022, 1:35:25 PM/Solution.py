// https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = [0]*64
        
        lp = 0
        
        # print(int(ord('A') - ord('A')))
        # print(int(ord('a') - ord('A')))
        
        for i in range(len(s)):
            res[int(ord(s[i]) - ord('A'))] += 1
        
        for i in range(64):
            if res[i] != 0 and res[i]/2 > 0 :
                lp += int(res[i]/2) * 2
        
        if lp < len(s):
            lp += 1
        
        return lp