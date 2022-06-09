// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        m = len(a)
        n = len(b)
        
        a = a[::-1]
        b = b[::-1]
        
        carry = 0
        if m<n:
            for i in range(m):
                temp = int(a[i]) + int(b[i]) + carry 
                if temp > 2:
                    # c.append('1')
                    c = c + '1'
                    carry  = 1
                elif temp == 2:
                    # c.apppend('0')
                    c = c + '0'
                    carry = 1
                elif temp == 1:
                    # c.append('1')
                    c = c + '1'
                    carry = 0
                elif temp == 0 :
                    # c.append('0')
                    c = c + '0'
                    carry = 0
                else:
                    pass
        else:
            for i in range(n):
                temp = int(a[i]) + int(b[i]) + carry 
                if temp > 2:
                    # c.append('1')
                    c = c + '1'
                    carry  = 1
                elif temp == 2:
                    # c.apppend('0')
                    c = c + '0'
                    carry = 1
                elif temp == 1:
                    # c.append('1')
                    c = c + '1'
                    carry = 0
                elif temp == 0 :
                    # c.append('0')
                    c = c + '0'
                    carry = 0
                else:
                    pass
        if m>n:
            for i in range(n, m):
                temp = int(a[i]) + carry 
                if temp > 2:
                    # c.append('1')
                    c = c + '1'
                    carry  = 1
                elif temp == 2:
                    # c.apppend('0')
                    c = c + '0'
                    carry = 1
                elif temp == 1:
                    # c.append('1')
                    c = c + '1'
                    carry = 0
                elif temp == 0 :
                    # c.append('0')
                    c = c + '0'
                    carry = 0
                else:
                    pass
                pass
            pass
        else:
            for i in range(m, n):
                temp = int(b[i]) + carry 
                if temp > 2:
                    # c.append('1')
                    c = c + '1'
                    carry  = 1
                elif temp == 2:
                    # c.apppend('0')
                    c = c + '0'
                    carry = 1
                elif temp == 1:
                    c = c + '1'
                    carry = 0
                elif temp == 0 :
                    c = c + '0'
                    carry = 0
                else:
                    pass
                pass
            pass
        
        if carry == 1:
            c = c + '1'
        
        # print(c)
        # c= reversed(c)
        c = c[::-1]
        # print(c)
        return c
        
        