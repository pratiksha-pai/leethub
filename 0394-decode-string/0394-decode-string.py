class Solution:
    def decodeString(self, s: str) -> str:
        
        res, num = [], []
        
        curr_num = ""
        
        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                curr_num = curr_num + s[i]
                # num.append(s[i])
            elif s[i] == "[":
                num.append(curr_num)
                curr_num = ""
                res.append("")
            elif s[i] == "]":
                times = int(num.pop())
                curr = res.pop()
                curr = curr * times
                if len(res) == 0:
                    res.append(curr)
                else:
                    res[-1] = res[-1] + curr
            else:
                if len(res) == 0:
                    res.append(s[i])
                else:
                    res[-1] = res[-1] + s[i]
            # print(i, curr_num, num, res)
            
        # print(res)
        return "".join(res[i] for i in range(len(res)))
                

                
                
        