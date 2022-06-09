// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        flag = False
        flag = self.isPalindrome(s)
        if flag is True:
            return True
        n = len(s)
        for i in range(0, n):
            if flag is True:
                return True
            # print('i is {}'.format(i))
            # print('check for {} and {} '.format(s[:i], s[i+1:]))
            flag = self.isPalindrome(s[:i] + s[i+1:])
        return flag