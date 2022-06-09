// https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount = [0]*26
        magazineCount = [0]*26
        
        for i in range(len(ransomNote)):
            ransomNoteCount[int(ord(ransomNote[i]) - ord('a'))] += 1
        
        for i in range(len(magazine)):
            magazineCount[int(ord(magazine[i]) - ord('a'))] += 1
        
        for i in range(26):
            if ransomNoteCount[i] > magazineCount[i]:
                return False
        
        return True