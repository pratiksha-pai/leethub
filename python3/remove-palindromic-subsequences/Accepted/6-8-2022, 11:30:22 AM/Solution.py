// https://leetcode.com/problems/remove-palindromic-subsequences

class Solution:
    def isPalindrome(self, s:str) -> bool:
        t=s[::-1]
        if s == t:
            return True
        return False
        
    def removePalindromeSub(self, s: str) -> int:
        if self.isPalindrome(s):
            return 1
        return 2