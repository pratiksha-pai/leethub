class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        def points(y, x, inp=True):
            # y = h, x = m
            
            if inp:
                
                if 1 <= x <= 15:
                    x = 1
                elif 16 <= x <= 30:
                    x = 2
                elif 31 <= x <= 45:
                    x = 3
                elif 46 <= x <= 59:
                    x = 4
                else:
                    x = 0
            else:
                if 0 <= x <= 14:
                    x = 0
                elif 15 <= x <= 29:
                    x = 1
                elif 30 <= x <= 44:
                    x = 2
                else:
                    x = 3
            
            return x + (y*4)
    
        in_hh = int(loginTime.split(':')[0])
        in_mm = int(loginTime.split(':')[1])
        out_hh = int(logoutTime.split(':')[0])
        out_mm = int(logoutTime.split(':')[1])
        
        # print(in_hh, in_mm, out_hh, out_mm)
        
        outp = points(out_hh, out_mm, False)
        inp = points(in_hh, in_mm, True)
        res = outp - inp
        # print(inp, outp)
        # if  out_hh == in_hh and out_mm == in_mm:
        #     return 0
        if out_hh > in_hh or (out_hh == in_hh and out_mm >= in_mm ):
            return  res if res > 0 else 0
        else:
            return outp - inp + (24* 4)
            
            
            
            
            
            
        
        return 0
        