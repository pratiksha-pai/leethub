class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def get_target_index(s, t):
            si, ti = 0, 0
            while si < len(s) and ti < len(t):
                if s[si] == t[ti]:
                    ti+=1
                si+=1
            
            return ti
        
        i = 0
        count = 0
        while i<len(target):
            pos = get_target_index(source, target[i:])
            if pos == 0:
                return -1
            i += pos
            count +=1
        return count