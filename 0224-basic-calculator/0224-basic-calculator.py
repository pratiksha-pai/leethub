class Solution:
    def calculate(self, s: str) -> int:
        stack, num, sign = [], 0, '+'
        s += '+'  # Add a dummy operator to handle the last number
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-':
                if sign == '+':
                    stack.append(num)
                else:
                    stack.append(-num)
                num, sign = 0, ch
            elif ch == '(':
                stack.append(sign)
                stack.append('(')
                sign, num = '+', 0
            elif ch == ')':
                if sign == '+':
                    stack.append(num)
                else:
                    stack.append(-num)
                num = 0
                while stack[-1] != '(':
                    num += stack.pop()
                stack.pop()  # remove '('
                prev_sign = stack.pop() if stack and stack[-1] in '+-' else '+'
                if prev_sign == '+':
                    stack.append(num)
                else:
                    stack.append(-num)
                num = 0
        return sum(stack)