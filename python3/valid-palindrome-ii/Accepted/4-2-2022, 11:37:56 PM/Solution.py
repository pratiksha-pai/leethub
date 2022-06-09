// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        def validPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right-1
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return validPalindrome(s, left, right-1) or validPalindrome(s, left+1, right)
            left, right = left+1, right-1
        return True
#         flag = False
#         if self.isPalindrome(s):
#             return True
#         n = len(s)
#         low = 0 
#         high = n-1
        
#         while low < high:
#             if s[low] == s[high]:
#                 low = low+1
#                 high = high-1
#             else:
#                 if self.isPalindrome(s[low+1:high]):
#                     return True
#                 if self.isPalindrome(s[low:high-1]):
#                     return True
#                 return False
#         return True