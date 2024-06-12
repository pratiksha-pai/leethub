class Solution:
    def isValid(self, strs: str) -> bool:
        mp = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for s in strs:
            if s in ["(", "{", "["]:
                stack.append(s)
            else:
                if not stack:
                    return False
                elif mp[stack[-1]] != s:
                    return False
                stack.pop()
        
        return True if len(stack) == 0 else False