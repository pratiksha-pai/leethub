class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict
        mp = defaultdict(list)
        counter = []
        for s in strs:
            key_val = sorted(Counter(s).items(), key=lambda x: x[0])
            key = ''.join(str(k) + str(v) for k, v in key_val)
            mp[key].append(s)
        
        return [val for key, val in mp.items()]