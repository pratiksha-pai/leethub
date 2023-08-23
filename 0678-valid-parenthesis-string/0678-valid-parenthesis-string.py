class Solution:
    def checkValidString(self, s: str) -> bool:
        # First pass: treat '*' as '('
        balance = 0
        for char in s:
            if char in '(*':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        # Second pass: treat '*' as ')'
        balance = 0
        for char in reversed(s):
            if char in '*)':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True