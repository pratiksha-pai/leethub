// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s=re.sub(r'[\W_]+', '', s).lower()
        # s = s.lower().strip()
        # print(s)
        # n = int(len(s)/2)
        n = len(s)
        # print(n)
        for i in range(0, n):
            # print(str(i) + ' ' + str(n-i) )
            if s[i] != s[n-i-1]:
                return False
        
        return True
        