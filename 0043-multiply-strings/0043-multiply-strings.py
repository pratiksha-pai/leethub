class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if nums1 == "0" or nums2 == "0":
            return "0"
        
        nums1, nums2 = nums1[::-1], nums2[::-1]
        n1, n2 = len(nums1), len(nums2)
        
        res = [0] * (n1+n2)
        for i in range(n1):
            for j in range(n2):
                res[i+j] += int(nums1[i]) * int(nums2[j])
                if res[i+j] >=10:
                    res[i+j+1] += res[i+j] // 10
                    res[i+j] %= 10
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        
        return ''.join(map(str, res[::-1]))
                