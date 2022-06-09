// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                temp.append(s[i])
            elif s[i] == ')':
                if temp[-1]=='(':
                    temp.pop()
                else:
                    temp.append(')')
            elif s[i] == '}':
                if temp[-1]=='{':
                    temp.pop()
                else:
                    temp.append('}')
            elif s[i] == ']':
                if temp[-1]=='[':
                    temp.pop()
                else:
                    temp.append(']')
            else:
                pass
        
        if len(temp) > 0:
            return False
        else:
            return True