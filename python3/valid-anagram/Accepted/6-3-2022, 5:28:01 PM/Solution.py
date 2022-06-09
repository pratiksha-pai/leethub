// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        arr1 = [0] * 26
        arr2 = [0] * 26
        
        for i in range(0, len(s)):
            pos1 = int(ord(s[i]) - ord('a'))
            pos2 = int(ord(t[i]) - ord('a'))
            # print(pos1)
            # print(pos2)
            arr1[pos1] += 1
            arr2[pos2] += 1
        
        for i in range(26):
            if arr1[i] != arr2[i]:
                return False
        
        return True
        