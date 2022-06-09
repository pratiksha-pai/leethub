// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = int(len(s)/2)
        n = len(s)
        for i in range(mid):
            if i == n-i:
                return
            if i == n-i-1:
                temp = s[i]
                s[i] = s[n-i-1]
                s[n-i-1] = temp
                return
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp
            i = i+1
        